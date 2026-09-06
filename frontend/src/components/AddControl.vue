<template>
  <q-form @submit.prevent="addControl()">
      <q-card>
        <q-card-section>
          <div class="q-ma-sm text-h5">Add Control</div>
          <q-field class="q-ma-sm" label="Id" stack-label :dense="false">
            <q-select v-model="control.id" :options="options" emit-value @update:model-value="updateTitle"/>
          </q-field>
          <q-field class="q-ma-sm" label="Title" >
            <q-input v-model="control.title" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Top">
            <q-input v-model="control.top" type="number" />
          </q-field>
          <q-field class="q-ma-sm" label="Left">
            <q-input v-model="control.left" type="number" />
          </q-field>
          <q-btn type="submit" color="primary" label="Add Control" />
        </q-card-section>
      </q-card>
  </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Control } from 'src/types';
import { IdEnum } from 'src/types';
import { useCreateNewProfileStore } from '../stores/create-new-profile-store';
defineOptions({
  name: 'AddControl',
});

const control = ref({
  id: IdEnum.VOCALS_DOG_CONTROL,
  title: IdEnum.VOCALS_DOG_CONTROL,
  top: 0,
  left: 0,
} as Control)

const options = Object.entries(IdEnum).map(([key, value]) => ({ label: key, value }))

const formStore = useCreateNewProfileStore();

const addControl = () => formStore.profile.controls.push({ ...control.value })

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const updateTitle = (newValue: { label: string, value: string }) => {
  control.value.title = control.value.id
}

</script>
