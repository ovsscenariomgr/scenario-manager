<template>
  <div class="q-pa-sm">
    <q-card bordered>
      <q-card-section>
        <div class="q-ma-sm text-h5">Media</div>
        <q-uploader ref="uploader" label="Add media files" multiple :auto-upload="false" @added="onFilesAdded" />

        <q-table :columns="columns" :rows="formStore.media" row-key="title" class="q-mt-md">
          <template v-slot:body-cell-title="props">
            <q-td :props="props">
              <q-input v-model="props.row.title" dense borderless />
            </q-td>
          </template>
          <template v-slot:body-cell-action="props">
            <q-td :props="props">
              <q-btn color="negative" icon="delete" flat dense @click="formStore.removeMedia(props.rowIndex)" />
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
import type { PendingMediaFile } from '../stores/create-new-media-store';
import { useCreateNewMediaStore } from '../stores/create-new-media-store';

defineOptions({
  name: 'CreateMediaStep',
});

const formStore = useCreateNewMediaStore();
const uploader = ref<QUploader | null>(null);

const columns: QTableColumn<PendingMediaFile>[] = [
  { name: 'title', label: 'Title', field: 'title', align: 'left' },
  { name: 'file', label: 'File', field: (row) => row.file.name, align: 'left' },
  { name: 'action', label: 'Delete', field: 'title' },
];

function onFilesAdded(files: readonly File[]) {
  formStore.addFiles(files);
  uploader.value?.reset();
}
</script>
