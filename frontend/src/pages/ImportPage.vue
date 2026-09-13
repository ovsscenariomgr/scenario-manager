<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 500px">
      <div class="text-h5 q-mb-md">Import Scenario Archive</div>
      <q-uploader
        label="Scenario Archive (.zip)"
        accept=".zip,application/zip"
        :auto-upload="false"
        :max-files="1"
        @added="(files) => onFileAdded(files[0])"
      />
      <q-btn
        class="q-mt-md"
        color="primary"
        label="Import"
        :loading="importing"
        :disable="!archiveFile"
        @click="doImport"
      />

      <q-banner v-if="errorMessage" class="bg-negative text-white q-mt-md">
        {{ errorMessage }}
        <ul v-if="missingFiles.length">
          <li v-for="filename in missingFiles" :key="filename">{{ filename }}</li>
        </ul>
      </q-banner>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Notify } from 'quasar';
import { api } from 'boot/axios';
import type { Scenario } from 'src/types';

defineOptions({
  name: 'ImportPage',
});

const router = useRouter();
const archiveFile = ref<File | null>(null);
const importing = ref(false);
const errorMessage = ref('');
const missingFiles = ref<string[]>([]);

function onFileAdded(file: File | undefined) {
  archiveFile.value = file ?? null;
}

interface ImportErrorData {
  detail?: string;
  missing?: Record<string, string[]>;
  archive?: string[];
  [key: string]: unknown;
}

async function doImport() {
  if (!archiveFile.value) return;
  importing.value = true;
  errorMessage.value = '';
  missingFiles.value = [];

  const formData = new FormData();
  formData.append('archive', archiveFile.value);

  try {
    const resp = await api.post<Scenario>('/api/v1/import', formData);
    Notify.create({ color: 'positive', position: 'top', message: 'Scenario imported successfully' });
    await router.push('/');
    return resp.data;
  } catch (error) {
    const data = (error as { response?: { data?: ImportErrorData } }).response?.data;
    if (data?.missing) {
      errorMessage.value = data.detail ?? 'Archive references files that are missing from the zip';
      missingFiles.value = Object.values(data.missing).flat();
    } else if (data?.detail) {
      errorMessage.value = data.detail;
    } else if (data?.archive) {
      errorMessage.value = data.archive.join(' ');
    } else {
      errorMessage.value = data ? JSON.stringify(data) : 'Import failed';
    }
    return null;
  } finally {
    importing.value = false;
  }
}
</script>
