<template>
  <div class="q-ma-auto" style="width: 700px; max-width: 80vw;" bordered>
    <q-form @submit.prevent="addControl()">
        <q-card class="q-ma-auto">
          <q-card-section>
            <div class="text-h5">Add Control</div>
            <q-field class="q-ma-sm" label="Id" stack-label :dense="false">
              <q-select v-model="control.id" :options="options" emit-value/>
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
            <q-btn type="submit" label="Add Control" />
          </q-card-section>
        </q-card>
    </q-form>
  </div>
</template>

<script setup lang="ts">
import type { Control } from 'src/types';
import { IdEnum } from 'src/types';
import { CreateNewProfileStore } from '../stores/create-new-profile-store';
defineOptions({
  name: 'AddControl',
});

const control = {
  id: IdEnum.VOCALS_DOG_CONTROL,
  title: IdEnum.VOCALS_DOG_CONTROL,
  top: 0,
  left: 0,
} as Control

const options = Object.entries(IdEnum).map(([key, value]) => ({ label: key, value }))

const formStore = CreateNewProfileStore();

const addControl = () => formStore.controls.push({ ...control })

</script>
