<template>
  <q-form>
    <div class="q-pa-sm q-gutter-md">
      <q-card v-for="(group, groupIndex) in formStore.eventgroups" :key="groupIndex" bordered>
        <q-card-section>
          <div class="row items-center q-mb-sm">
            <div class="text-h5 col">Category</div>
            <q-btn
              color="negative"
              icon="delete"
              flat
              dense
              :disable="formStore.eventgroups.length <= 1"
              @click="formStore.removeEventGroup(groupIndex)"
            />
          </div>
          <div class="row q-col-gutter-sm q-mb-md">
            <div class="col-6 col-md-3">
              <q-input v-model="group.name" label="Name" dense />
            </div>
            <div class="col-6 col-md-3">
              <q-input v-model="group.title" label="Title" dense />
            </div>
          </div>

          <q-table :columns="eventColumns" :rows="group.events" row-key="id" dense>
            <template v-slot:body-cell-action="props">
              <q-td :props="props">
                <q-btn color="negative" icon="delete" flat dense @click="removeEvent(groupIndex, props.rowIndex)" />
              </q-td>
            </template>
          </q-table>

          <q-form class="row q-col-gutter-sm q-mt-sm items-end" @submit.prevent="addEvent(groupIndex)">
            <div class="col-6 col-md-3">
              <q-input v-model="newEvent[groupIndex].title" label="Event Title" dense />
            </div>
            <div class="col-6 col-md-3">
              <q-input v-model="newEvent[groupIndex].id" label="Event Id" dense />
            </div>
            <div class="col-6 col-md-2">
              <q-toggle
                v-model="newEvent[groupIndex].priority"
                :true-value="PriorityEnum._1"
                :false-value="PriorityEnum._0"
                label="Priority"
              />
            </div>
            <div class="col-6 col-md-2">
              <q-input v-model="newEvent[groupIndex].hotkey" label="Hotkey" maxlength="1" dense />
            </div>
            <div class="col-6 col-md-2">
              <q-btn type="submit" color="primary" label="Add Event" dense />
            </div>
          </q-form>
        </q-card-section>
      </q-card>

      <q-btn color="primary" icon="add" label="Add Category" @click="addEventGroup" />
    </div>
  </q-form>
</template>

<script setup lang="ts">
import { reactive, watch } from 'vue';
import type { QTableColumn } from 'quasar';
import type { Event } from '../types';
import { PriorityEnum } from '../types';
import { useCreateNewEventGroupsStore } from '../stores/create-new-eventgroups-store';

defineOptions({
  name: 'CreateEventGroupsStep',
});

const formStore = useCreateNewEventGroupsStore();

const eventColumns: QTableColumn<Event>[] = [
  { name: 'title', label: 'Title', field: 'title', align: 'left' },
  { name: 'id', label: 'Id', field: 'id', align: 'left' },
  { name: 'priority', label: 'Priority', field: 'priority', align: 'left' },
  { name: 'hotkey', label: 'Hotkey', field: 'hotkey', align: 'left' },
  { name: 'action', label: 'Delete', field: 'id' },
];

const blankEvent = (): Event => ({ title: '', id: '', priority: PriorityEnum._0, hotkey: '' });
const newEvent = reactive<Event[]>(formStore.eventgroups.map(() => blankEvent()));

// Keep newEvent in sync when categories are added/removed
watch(
  () => formStore.eventgroups.length,
  (length) => {
    while (newEvent.length < length) newEvent.push(blankEvent());
    newEvent.length = length;
  },
);

function addEvent(groupIndex: number) {
  formStore.eventgroups[groupIndex]?.events.push({ ...newEvent[groupIndex] });
  newEvent[groupIndex] = blankEvent();
}

function removeEvent(groupIndex: number, eventIndex: number) {
  formStore.eventgroups[groupIndex]?.events.splice(eventIndex, 1);
}

function addEventGroup() {
  formStore.addEventGroup();
}
</script>
