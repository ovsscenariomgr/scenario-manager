import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Scenario } from '../types';

export const NewScenarioStore = defineStore('NewScenarioStore', {
  state: () => ({
    newScenario: {} as Scenario,
  }),
  getters: {},
  actions: {
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(NewScenarioStore, import.meta.hot));
}
