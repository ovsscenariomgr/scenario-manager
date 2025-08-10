<template>
  <!-- <pre>{{ appAuthStore.user }}</pre> -->
  <q-btn
    v-if="!appAuthStore.loggedOut"
    label="Logout"
    color="primary"
    @click="appAuthStore.logout()"
  />
  <div class="q-pa-md">
    <q-table
      v-if="!appAuthStore.loggedOut"
      title="Scenarios"
      :columns="columns"
      :rows="store.getScenarioHeaders"
      row-key="id"
    />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import type { QTableProps } from 'quasar'
import { scenarioStore } from '../stores/scenario-store'
import { useAppAuthStore } from '../stores/app-auth-store'

const appAuthStore = useAppAuthStore()

defineOptions({
  name: 'ScenarioTableComponent'
});

const store = scenarioStore()

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

onMounted(() => {
  store.fetchScenarios()
})

</script>
