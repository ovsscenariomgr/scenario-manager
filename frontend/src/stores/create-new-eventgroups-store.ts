import { defineStore, acceptHMRUpdate } from 'pinia';
import type { EventGroup } from '../types';

const defaultEventGroup = (): EventGroup => ({
  name: '',
  title: '',
  events: [],
});

export const useCreateNewEventGroupsStore = defineStore('CreateNewEventGroupsStore', {
  state: () => ({
    eventgroups: [defaultEventGroup()] as EventGroup[],
  }),
  getters: {},
  actions: {
    addEventGroup() {
      this.eventgroups.push(defaultEventGroup());
    },
    removeEventGroup(index: number) {
      this.eventgroups.splice(index, 1);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewEventGroupsStore, import.meta.hot));
}
