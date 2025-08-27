import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Avatar, Summary, Control, Profile } from '../types';

export const CreateNewProfileStore = defineStore('CreateNewProfileStore', {
  state: () => ({
    // Avatar
    avatar: {
      filename: null,
      height_pct: 100,
      width_pct: 100,
    } as Avatar,
    summary: {
      description: 'Scenario Summary',
      breed: '',
      gender: '',
      weight: '',
      species: '',
      symptoms: 'Scenario Symptoms',
      image: null,
    } as Summary,
    controls: [] as Control[],
    profile: {
      color: '#000000',
    } as Profile,
  }),
  getters: {},
  actions: {
    saveProfile() {
      this.profile.avatar = this.avatar
      this.profile.summary = this.summary
      this.profile.controls = this.controls
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(CreateNewProfileStore, import.meta.hot));
}
