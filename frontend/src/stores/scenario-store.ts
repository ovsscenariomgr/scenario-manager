import { defineStore, acceptHMRUpdate } from 'pinia';
import { api } from 'boot/axios';
import { Notify } from 'quasar';
import type { Scenario, ScenarioTableRow } from '../types';

export const useScenarioStore = defineStore('scenarios', {
  state: () => ({
    scenarios: [] as Scenario[],
  }),

  getters: {
    getScenarios(state): Scenario[] {
      return state.scenarios;
    },
    getScenarioHeaders(state): ScenarioTableRow[] {
      return state.scenarios.map(({ id, header }) => ({ id, header }));
    },
  },

  actions: {
    fetchScenarios() {
      api
        .get<Scenario[]>('/api/v1/scenarios', { headers: { 'Content-Type': 'application/json' } })
        .then((response) => {
          this.scenarios = response.data;
        })
        .catch(() => {
          Notify.create({
            color: 'negative',
            position: 'top',
            message: 'Could not fetch scenarios, is backend running?',
            icon: 'report_problem',
          });
        });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useScenarioStore, import.meta.hot));
}
