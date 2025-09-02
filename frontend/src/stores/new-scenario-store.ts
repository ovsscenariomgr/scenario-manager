import { defineStore, acceptHMRUpdate } from 'pinia';
import { useCreateNewHeaderStore } from './create-new-header-store'
import { useCreateNewProfileStore } from './create-new-profile-store'
import type { Scenario } from '../types';

export const useNewScenarioStore = defineStore('NewScenarioStore', {
  state: () => ({
    newScenario: {} as Scenario,
  }),
  getters: {},
  actions: {
    saveScenarioData() {
      const newHeader = useCreateNewHeaderStore()
      const newProfile = useCreateNewProfileStore()
      this.newScenario.header = newHeader.header
      this.newScenario.profile = newProfile.profile
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useNewScenarioStore, import.meta.hot));
}
