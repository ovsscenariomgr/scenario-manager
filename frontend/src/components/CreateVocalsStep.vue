<template>
  <div class="q-pa-sm">
    <q-card bordered>
      <q-card-section>
        <div class="q-ma-sm text-h5">Vocals</div>
        <q-uploader
          ref="uploader"
          label="Add vocal files (.wav)"
          accept=".wav,audio/wav"
          multiple
          :auto-upload="false"
          @added="onFilesAdded"
        />

        <q-table :columns="columns" :rows="formStore.vocals" row-key="title" class="q-mt-md">
          <template v-slot:body-cell-title="props">
            <q-td :props="props">
              <q-input v-model="props.row.title" dense borderless />
            </q-td>
          </template>
          <template v-slot:body-cell-action="props">
            <q-td :props="props">
              <q-btn color="negative" icon="delete" flat dense @click="formStore.removeVocal(props.rowIndex)" />
            </q-td>
          </template>
        </q-table>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { QTableColumn, QUploader } from 'quasar';
import type { PendingVocalFile } from '../stores/create-new-vocals-store';
import { useCreateNewVocalsStore } from '../stores/create-new-vocals-store';

defineOptions({
  name: 'CreateVocalsStep',
});

const formStore = useCreateNewVocalsStore();
const uploader = ref<QUploader | null>(null);

const columns: QTableColumn<PendingVocalFile>[] = [
  { name: 'title', label: 'Title', field: 'title', align: 'left' },
  { name: 'file', label: 'File', field: (row) => row.file.name, align: 'left' },
  { name: 'action', label: 'Delete', field: 'title' },
];

function onFilesAdded(files: readonly File[]) {
  formStore.addFiles(files);
  uploader.value?.reset();
}
</script>
