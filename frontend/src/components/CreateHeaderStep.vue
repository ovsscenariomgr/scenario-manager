<template>
  <q-form @submit.prevent="saveStepData()">
    <div class="q-pa-sm row items-start q-gutter-md">
      <q-card class="q-mt-sm q-mr-sm" style="width: 700px; max-width: 80vw;" bordered>
        <q-card-section>
          <div class="text-h5">Header</div>
          <q-field outlined label="Author" stack-label :dense="false">
            <q-input no-outline v-model="formStore.header.author" type="text" />
          </q-field>
          <q-field label="Date of Creation" stack-label :dense="false">
            <template v-slot:control>
              <q-date class="q-mt-sm" v-model="formStore.header.date_of_creation" minimal label="Date" />
            </template>
          </q-field>
          <q-field>
            <q-input v-model="formStore.header.description" label="Description" type="text" />
          </q-field>
        </q-card-section>
      </q-card>
      <q-separator vertical />
      <q-card class="q-mt-sm q-mr-sm" style="width: 700px; max-width: 80vw;" bordered>
        <q-card-section>
          <div class="text-h5">Title</div>
          <q-input v-model="formStore.title.name" label="Title Name" type="text" />
          <q-input v-model="formStore.title.top" label="Title Top" type="number" />
          <q-input v-model="formStore.title.left" label="Title Left" type="number" />
        </q-card-section>
      </q-card>
    </div>


    <q-btn type="submit" label="Save Step" />
  </q-form>
</template>

<script setup lang="ts">
import { newScenarioStore } from '../stores/new-scenario-store';
defineOptions({
  name: 'CreateHeaderStep',
});

const formStore = newScenarioStore();

const saveStepData = () => {
  formStore.saveHeader()
  console.log(`${JSON.stringify(formStore.newScenario)}`)
}
</script>

<style lang="sass" scoped>
.header-card
  width: 100%
  max-width: 250px
</style>
