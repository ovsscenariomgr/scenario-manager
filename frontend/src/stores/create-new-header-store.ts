import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Header, Title } from '../types';

export const CreateNewHeaderStore = defineStore('CreateNewHeaderStore', {
  state: () => ({
    // Header
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
  }),
  getters: {},
  actions: {
    saveHeader() {
      this.header.title = this.title
    },
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(CreateNewHeaderStore, import.meta.hot));
}
