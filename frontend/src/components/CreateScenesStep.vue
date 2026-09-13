<template>
  <q-form>
    <div class="q-pa-sm q-gutter-md">
      <q-card v-for="(scene, sceneIndex) in formStore.scenes" :key="sceneIndex" bordered>
        <q-card-section>
          <div class="row items-center q-mb-sm">
            <div class="text-h5 col">Scene</div>
            <q-btn
              color="negative"
              icon="delete"
              flat
              dense
              :disable="formStore.scenes.length <= 1"
              @click="formStore.removeScene(sceneIndex)"
            />
          </div>
          <div class="row q-col-gutter-sm q-mb-md">
            <div class="col-6 col-md-3">
              <q-input v-model="scene.title" label="Title" dense />
            </div>
            <div class="col-6 col-md-3">
              <q-input v-model.number="scene.id" type="number" label="Id" dense />
            </div>
            <div class="col-6 col-md-3">
              <q-input v-model.number="scene.triggers_needed" type="number" label="Triggers Needed" dense />
            </div>
          </div>

          <cardiac-respiration-general-fields
            v-if="scene.init"
            v-model:cardiac="scene.init.cardiac"
            v-model:respiration="scene.init.respiration"
            v-model:general="scene.init.general"
          />

          <div class="text-subtitle1 q-mt-md">Timeout</div>
          <q-toggle
            :model-value="!!scene.timeout"
            label="Has timeout (leave off for a terminal scene)"
            @update:model-value="(val) => formStore.setHasTimeout(sceneIndex, val)"
          />
          <div v-if="scene.timeout" class="row q-col-gutter-sm q-mb-md">
            <div class="col-6 col-md-3">
              <q-input v-model.number="scene.timeout.timeout_value" type="number" label="Timeout Value (s)" dense />
            </div>
            <div class="col-6 col-md-3">
              <q-select
                v-model.number="scene.timeout.scene_id"
                :options="formStore.sceneIds"
                label="Go to Scene Id"
                dense
              />
            </div>
          </div>

          <div class="text-subtitle1 q-mt-md">Triggers</div>
          <div
            v-for="(trigger, triggerIndex) in scene.triggers"
            :key="triggerIndex"
            class="row q-col-gutter-sm q-mb-sm items-center"
          >
            <div class="col-6 col-md-2">
              <q-select v-model.number="trigger.scene_id" :options="formStore.sceneIds" label="Go to Scene Id" dense />
            </div>
            <div class="col-6 col-md-2">
              <q-select
                v-model="trigger.event_id"
                :options="eventIdOptions"
                label="Event Id (optional)"
                clearable
                dense
              />
            </div>
            <div class="col-6 col-md-2">
              <q-select
                v-model="trigger.test"
                :options="testOptions"
                emit-value
                map-options
                label="Test"
                clearable
                dense
              />
            </div>
            <div class="col-6 col-md-2">
              <q-input v-model.number="trigger.cpr_duration" type="number" label="CPR Duration (s)" clearable dense />
            </div>
            <div class="col-6 col-md-2">
              <q-input v-model.number="trigger.group" type="number" label="Group" clearable dense />
            </div>
            <div class="col-6 col-md-1">
              <q-btn
                color="negative"
                icon="delete"
                flat
                dense
                @click="formStore.removeTrigger(sceneIndex, triggerIndex)"
              />
            </div>
          </div>
          <q-btn color="primary" icon="add" label="Add Trigger" dense @click="formStore.addTrigger(sceneIndex)" />
        </q-card-section>
      </q-card>

      <q-btn color="primary" icon="add" label="Add Scene" @click="formStore.addScene()" />
    </div>
  </q-form>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { TestEnum } from '../types';
import { useCreateNewScenesStore } from '../stores/create-new-scenes-store';
import { useCreateNewEventGroupsStore } from '../stores/create-new-eventgroups-store';
import CardiacRespirationGeneralFields from './CardiacRespirationGeneralFields.vue';

defineOptions({
  name: 'CreateScenesStep',
});

const formStore = useCreateNewScenesStore();
const eventGroupsStore = useCreateNewEventGroupsStore();

const eventIdOptions = computed(() =>
  eventGroupsStore.eventgroups.flatMap((group) =>
    group.events.map((event) => event.id).filter((id): id is string => !!id),
  ),
);

const testOptions = Object.values(TestEnum).map((value) => ({ label: value, value }));
</script>
