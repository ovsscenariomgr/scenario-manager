import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Header, Title } from '../types';

export const useCreateNewHeaderStore = defineStore('CreateNewHeaderStore', {
  state: () => ({
    // Header
    header: {
      author: 'ovsscenariomgr',
      date_of_creation: new Date().toISOString(),
      description: 'An Open Vet Sim scenario created by OVS Scenario Manager',
      title: {
        name: 'Open Vet Sim Scenario Title',
        top: 0,
        left: 0
      } as Title,
    } as Header,
  }),
  getters: {},
  actions: {}
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewHeaderStore, import.meta.hot));
}
