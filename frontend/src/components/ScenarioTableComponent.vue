<template>
  <div class="q-pa-md">
    <q-table
      title="Scenarios"
      :columns="columns"
      :rows="scenarios"
      row-key="id"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from 'boot/axios'
import { QTableProps, useQuasar } from 'quasar'
import { Scenario } from '../types'

defineOptions({
  name: 'ScenarioTableComponent'
});

const $q = useQuasar()

const columns: QTableProps['columns'] = [
  {
    name: 'id',
    required: true,
    label: 'Scenario ID',
    align: 'left',
    field: row => row.id,
    // format: val => `${val}`,
    sortable: true
  },
  {
    name: 'title',
    label: 'Scenario Title',
    align: 'left',
    field: row => row.header.title.name,
    sortable: true
  }
]

const scenarios = ref<Scenario[]>([])

function getScenarios() {
  api
  .get<Scenario[]>('http://localhost:8000/api/v1/scenarios', { headers: { 'Content-Type': 'application/json' }})
  .then((response) => scenarios.value = response.data)
  .catch(() => {
    $q.notify({
      color: 'negative',
      position: 'top',
      message: 'Loading failed',
      icon: 'report_problem'
    })
  })
}

onMounted(() => {
  getScenarios()
})

</script>
