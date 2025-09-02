<template>
  <q-form @submit.prevent="saveStepData()">
    <div class="q-pa-sm row items-start q-gutter-md">
      <div class="col-md-4">
        <!-- Avatar -->
        <q-card class="q-ma-auto" bordered>
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
      </div>
      <div class="col-md-4">
        <!-- Color -->
        <q-card class="q-ma-auto" bordered>
          <q-card-section>
            <div class="text-h5">Color</div>
            <q-field class="q-ma-sm" label="Filename" stack-label :dense="false">
              <q-input v-model="formStore.profile.color" type="text" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4">
        <!-- Summary -->
        <q-card class="q-ma-auto" bordered>
          <q-card-section>
            <div class="text-h5">Summary</div>
            <q-field class="q-ma-sm" label="Summary Description">
              <q-input v-model="formStore.summary.description" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Breed" >
              <q-input v-model="formStore.summary.breed" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Gender">
              <q-input v-model="formStore.summary.gender" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Weight">
              <q-input v-model="formStore.summary.weight" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Species">
              <q-input v-model="formStore.summary.species" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Symptoms">
              <q-input v-model="formStore.summary.symptoms" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Image">
              <q-input v-model="formStore.summary.image" type="text" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4">
        <!-- Controls -->
        <q-card class="q-ma-auto" bordered>
          <q-card-section>
            <div class="q-ma-auto text-h5">Controls</div>
            <div class="q-pa-sm row items-start q-gutter-md">
              <q-table
                :columns="formStore.controlColumns"
                :rows="formStore.controls"
                row-key="id"
              >
                <template v-slot:body-cell-action="props">
                  <q-td :props="props">
                    <q-btn
                      color="negative"
                      icon="delete"
                      flat
                      dense
                      @click="deleteControl(props.row.id)"
                    />
                  </q-td>
                </template>
              </q-table>
              <q-separator />
              <add-control class="q-pa-sm" ></add-control>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <q-btn type="submit" label="Save Step" />
  </q-form>
</template>

<script setup lang="ts">
import { CreateNewProfileStore } from '../stores/create-new-profile-store';
import AddControl from './AddControl.vue';
defineOptions({
  name: 'CreateProfileStep',
});

const formStore = CreateNewProfileStore();

const deleteControl= (id) => {
  const index = formStore.controls.findIndex(row => row.id === id);
  if (index !== -1) {
    formStore.controls.splice(index, 1);
  }
}

const saveStepData = () => {
  formStore.saveProfile()
  console.log(`${JSON.stringify(formStore.profile)}`)
}
</script>
