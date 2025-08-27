<template>
  <q-form @submit.prevent="saveStepData()">
    <div class="q-pa-sm row items-start q-gutter-md">
      <q-card class="q-ma-auto" style="width: 700px; max-width: 80vw;" bordered>
        <q-card-section>
          <div class="text-h5">Avatar</div>
          <q-field class="q-ma-sm" label="Filename" stack-label :dense="false">
            <q-input v-model="formStore.avatar.filename" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Height Percentage" >
            <q-input v-model="formStore.avatar.height_pct" type="number" />
          </q-field>
          <q-field class="q-ma-sm" label="Width Percentage">
            <q-input v-model="formStore.avatar.width_pct" type="number" />
          </q-field>
        </q-card-section>
      </q-card>
      <q-card class="q-ma-auto" style="width: 700px; max-width: 80vw;" bordered>
        <q-card-section>
          <div class="text-h5">Color</div>
          <q-field class="q-ma-sm" label="Filename" stack-label :dense="false">
            <q-input v-model="formStore.profile.color" type="text" />
          </q-field>
        </q-card-section>
      </q-card>
      <q-card class="q-ma-auto" style="width: 700px; max-width: 80vw;" bordered>
        <q-card-section>
          <div class="text-h5">Summary</div>
          <q-field class="q-ma-sm" label="Summary Description">
            <q-input v-model="formStore.summary.description" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Breed" >
            <q-input v-model="formStore.summary.breed"  type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Gender">
            <q-input v-model="formStore.summary.gender" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Weight">
            <q-input v-model="formStore.summary.weight" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Species">
            <q-input v-model="formStore.summary.gender" type="text" />
          </q-field>
          <q-field class="q-ma-sm" label="Symptoms">
            <q-input v-model="formStore.summary.symptoms" type="text" />
          </q-field>
        </q-card-section>
      </q-card>

    </div>


    <q-btn type="submit" label="Save Step" />
  </q-form>
</template>

<script setup lang="ts">
import { CreateNewProfileStore } from '../stores/create-new-profile-store';
defineOptions({
  name: 'CreateProfileStep',
});

const formStore = CreateNewProfileStore();

const saveStepData = () => {
  formStore.saveProfile()
  console.log(`${JSON.stringify(formStore.profile)}`)
}
</script>
