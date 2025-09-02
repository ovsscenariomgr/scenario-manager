import type { QTableColumn } from 'quasar';
import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Avatar, Summary, Control, Profile } from '../types';

export const useCreateNewProfileStore = defineStore('CreateNewProfileStore', {
  state: () => ({
    // Profile (actual state)
    profile: {
      color: '#000000',
      // Avatar
      avatar: {
        filename: null,
        height_pct: 100,
        width_pct: 100,
      } as Avatar,
      // Summary
      summary: {
        description: 'Scenario Summary',
        breed: '',
        gender: '',
        weight: '',
        species: '',
        symptoms: 'Scenario Symptoms',
        image: null,
      } as Summary,
      // Controls
      controls: [] as Control[],
    } as Profile,

    controlColumns: [
      { name: 'id', label: 'Id', field: 'id',  sortable: true },
      { name: 'title', label: 'Title', field: 'title', sortable: true },
      { name: 'top', label: 'Top', field: 'top', sortable: false },
      { name: 'left', label: 'Left', field: 'left',  sortable: false },
      { name: 'action', label: 'Delete' }
    ] as QTableColumn<Control>[],
  }),
  getters: {},
  actions: {}
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewProfileStore, import.meta.hot));
}
