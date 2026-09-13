<template>
  <q-form @submit.prevent="saveStepData()">
    <div class="q-pa-sm row items-start q-gutter-md">
      <div class="col-md-4">
        <!-- Avatar -->
        <q-card bordered>
          <q-card-section>
            <div class="q-pa-sm text-h5">Avatar</div>
            <q-uploader
              label="Avatar Image"
              accept="image/*"
              :auto-upload="false"
              @added="(files) => onAvatarFileAdded(files[0])"
            />
            <q-field label="Height Percentage">
              <q-input v-model="formStore.profile.avatar.height_pct" type="number" hide-underline />
            </q-field>
            <q-field label="Width Percentage">
              <q-input v-model="formStore.profile.avatar.width_pct" type="number" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4">
        <!-- Color -->
        <q-card bordered>
          <q-card-section>
            <div class="q-pa-sm text-h5">Color</div>
            <q-field class="q-ma-sm" label="Filename" stack-label :dense="false">
              <q-input v-model="formStore.profile.color" type="text" />
            </q-field>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4">
        <!-- Summary -->
        <q-card bordered>
          <q-card-section>
            <div class="q-pa-sm text-h5">Summary</div>
            <q-field class="q-ma-sm" label="Summary Description">
              <q-input v-model="formStore.profile.summary.description" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Breed">
              <q-input v-model="formStore.profile.summary.breed" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Gender">
              <q-input v-model="formStore.profile.summary.gender" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Weight">
              <q-input v-model="formStore.profile.summary.weight" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Species">
              <q-input v-model="formStore.profile.summary.species" type="text" />
            </q-field>
            <q-field class="q-ma-sm" label="Symptoms">
              <q-input v-model="formStore.profile.summary.symptoms" type="text" />
            </q-field>
            <q-uploader
              label="Summary Image"
              accept="image/*"
              :auto-upload="false"
              @added="(files) => onSummaryFileAdded(files[0])"
            />
          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-5">
        <!-- Controls -->
        <q-card bordered>
          <q-card-section>
            <div class="q-pa-sm text-h5">Controls</div>
            <div class="q-pa-sm">
              <q-table :columns="formStore.controlColumns" :rows="formStore.profile.controls" row-key="id">
                <template v-slot:body-cell-action="props">
                  <q-td :props="props">
                    <q-btn color="negative" icon="delete" flat dense @click="deleteControl(props.row.id)" />
                  </q-td>
                </template>
              </q-table>
            </div>
            <div class="q-pa-sm">
              <add-control></add-control>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-form>
</template>

<script setup lang="ts">
import type { IdEnum } from 'src/types';
import { useCreateNewProfileStore } from '../stores/create-new-profile-store';
import AddControl from './AddControl.vue';
defineOptions({
  name: 'CreateProfileStep',
});

const formStore = useCreateNewProfileStore();

const deleteControl = (id: IdEnum) => {
  const index = formStore.profile.controls.findIndex((row) => row.id === id);
  if (index !== -1) {
    formStore.profile.controls.splice(index, 1);
  }
};

const onAvatarFileAdded = (file: File | undefined) => {
  formStore.avatarFile = file ?? null;
};

const onSummaryFileAdded = (file: File | undefined) => {
  formStore.summaryImageFile = file ?? null;
};

const saveStepData = () => {
  console.log(`${JSON.stringify(formStore.profile)}`);
};
</script>
