import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Header, Title, Scenario } from '../types';

export const newScenarioStore = defineStore('newScenarioStore', {
  state: () => ({
    header: {
      author: 'ovsscenariomgr',
      date_of_creation: new Date().toISOString(),
      description: 'An Open Vet Sim scenario created by OVS Scenario Manager',
    } as Header,
    title: {
      name: 'Open Vet Sim Scenario Title',
      top: 0,
      left: 0
    } as Title,
    newScenario: {} as Scenario,
  }),
  getters: {},
  actions: {
    saveHeader() {
      this.header.title = this.title
      this.newScenario.header = this.header
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(newScenarioStore, import.meta.hot));
}
