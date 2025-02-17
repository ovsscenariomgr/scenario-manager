import { defineStore } from 'pinia'
import { api } from 'boot/axios'
import { Notify } from 'quasar'
import { Scenario } from '../types'

export const scenarioStore = defineStore('scenarios', {
  state: () => ({
    scenarios: [] as Scenario[],
  }),
  getters: {
    getScenarios: (state) => state.scenarios,
    getScenarioHeaders: (state) => state.scenarios.map(({ id, header }) => ({ id, header }))
  },
  actions: {
    fetchScenarios() {
      api.get<Scenario[]>('/api/v1/scenarios', { headers: { 'Content-Type': 'application/json' }})
      .then((response) => {
        this.scenarios = response.data
      })
      .catch(() => {
        Notify.create({
          color: 'negative',
          position: 'top',
          message: 'Could not fetch scenarios, is backend running?',
          icon: 'report_problem'
        })
      })
    }
  }
})
