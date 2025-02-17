<template>
  <div class="q-pa-md">
    <q-table
      title="Scenarios"
      :columns="columns"
      :rows="rows"
      row-key="id"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from 'boot/axios'
import { QTableProps, useQuasar } from 'quasar'
import { Scenario, Header } from '../types'

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
    label: 'Title',
    align: 'left',
    field: row => row.header.title.name,
    sortable: true
  },
  {
    name: 'author',
    label: 'Author',
    align: 'left',
    field: row => row.header.author,
    sortable: true
  },
  {
    name: 'description',
    label: 'Description',
    align: 'left',
    field: row => row.header.description,
    sortable: true
  },
  {
    name: 'date_of_creation',
    label: 'Created Date',
    align: 'left',
    field: row => row.header.date_of_creation,
    sortable: true
  }
]

interface TableRow {
  id: number,
  header: Header,
}

const rows = ref<TableRow[]>([])

function getScenarioHeaders() {
  api
  .get<Scenario[]>('/api/v1/scenarios', { headers: { 'Content-Type': 'application/json' }})
  .then((response) => {
    rows.value = response.data.map(({ id, header }) => ({ id, header }))
  })
  .catch(() => {
    $q.notify({
      color: 'negative',
      position: 'top',
      message: 'Could not fetch scenarios, is backend running?',
      icon: 'report_problem'
    })
  })
}

onMounted(() => {
  getScenarioHeaders()
})

</script>
