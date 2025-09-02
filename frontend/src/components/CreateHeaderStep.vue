<template>
  <q-form @submit.prevent="saveStepData()">
    <div class="q-pa-sm row items-start q-gutter-md">
      <div class="col-md-4">
        <q-card class="q-ma-auto" bordered>
          <q-card-section>
            <div class="q-ma-sm text-h5">Header</div>
            <q-field class="q-ma-sm" label="Author" stack-label :dense="false">
              <q-input v-model="formStore.header.author" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Date of Creation" stack-label :dense="false" >
              <template v-slot:label>
                <span class="q-mb-sm" style="font-size: 18px;">Date of Creation</span>
              </template>
              <template v-slot:control>
                <q-date class="q-mt-sm" v-model="formStore.header.date_of_creation" minimal label="Date" />
              </template>
            </q-field>
            <q-field class="q-ma-sm">
              <q-input v-model="formStore.header.description" label="Description" type="text" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4">
        <q-card class="q-ma-auto" bordered>
          <q-card-section>
            <div class="q-ma-sm text-h5">Title</div>
            <q-field class="q-ma-sm">
              <q-input v-model="formStore.header.title.name" label="Title Name" type="text" />
            </q-field>
            <q-field class="q-ma-sm">
              <q-input v-model="formStore.header.title.top" label="Title Top" type="number" />
            </q-field>
            <q-field class="q-ma-sm">
              <q-input v-model="formStore.header.title.left" label="Title Left" type="number" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-form>
</template>

<script setup lang="ts">
import { useCreateNewHeaderStore } from '../stores/create-new-header-store';
defineOptions({
  name: 'CreateHeaderStep',
});

const formStore = useCreateNewHeaderStore();

const saveStepData = () => {
  console.log(`${JSON.stringify(formStore.header)}`)
}
</script>
