<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 500px">
      <div class="text-h5 q-mb-md">Export Scenario Archive</div>
      <q-select v-model="selectedId" :options="scenarioOptions" emit-value map-options label="Scenario" />
      <q-btn
        class="q-mt-md"
        color="primary"
        label="Download"
        icon="download"
        :loading="downloading"
        :disable="selectedId === null"
        @click="doExport"
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, computed, onBeforeMount } from 'vue';
import { Notify } from 'quasar';
import { api } from 'boot/axios';
import { useScenarioStore } from '../stores/scenario-store';

defineOptions({
  name: 'ExportPage',
});

const store = useScenarioStore();
const selectedId = ref<number | null>(null);
const downloading = ref(false);

const scenarioOptions = computed(() =>
  store.getScenarioHeaders.map((row) => ({ label: `${row.header.title.name} (#${row.id})`, value: row.id })),
);

async function doExport() {
  if (selectedId.value === null) return;
  downloading.value = true;
  try {
    const resp = await api.get(`/api/v1/export/${selectedId.value}`, { responseType: 'blob' });
    const url = window.URL.createObjectURL(new Blob([resp.data as BlobPart]));
    const link = document.createElement('a');
    link.href = url;
    link.download = `scenario-${selectedId.value}.zip`;
    link.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    Notify.create({
      color: 'negative',
      position: 'top',
      message: 'Could not export scenario',
      icon: 'report_problem',
    });
    console.error(error);
  } finally {
    downloading.value = false;
  }
}

onBeforeMount(() => {
  store.fetchScenarios();
});
</script>
