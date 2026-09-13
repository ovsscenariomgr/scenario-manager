import { defineStore, acceptHMRUpdate } from 'pinia';
import { Notify } from 'quasar';
import { api } from 'boot/axios';
import { useCreateNewHeaderStore } from './create-new-header-store';
import { useCreateNewProfileStore } from './create-new-profile-store';
import { useCreateNewVocalsStore } from './create-new-vocals-store';
import { useCreateNewMediaStore } from './create-new-media-store';
import { useCreateNewScenarioInitStore } from './create-new-scenario-init-store';
import { useCreateNewEventGroupsStore } from './create-new-eventgroups-store';
import { useCreateNewScenesStore } from './create-new-scenes-store';
import type { Scenario } from '../types';

export const useNewScenarioStore = defineStore('NewScenarioStore', {
  state: () => ({
    newScenario: {} as Scenario,
    submitting: false,
    createdId: null as number | null,
  }),
  getters: {},
  actions: {
    saveScenarioData() {
      const newHeader = useCreateNewHeaderStore();
      const newProfile = useCreateNewProfileStore();
      const newScenarioInit = useCreateNewScenarioInitStore();
      const newEventGroups = useCreateNewEventGroupsStore();
      const newScenes = useCreateNewScenesStore();

      this.newScenario.header = newHeader.header;
      this.newScenario.profile = newProfile.profile;
      this.newScenario.init = newScenarioInit.scenarioInit;
      this.newScenario.eventgroups = newEventGroups.eventgroups;
      this.newScenario.scenes = newScenes.scenes;
      // Files ride along separately after the scenario id exists (ADR-0002)
      this.newScenario.vocalfiles = [];
      this.newScenario.mediafiles = [];
    },

    async submitScenario(): Promise<number | null> {
      this.saveScenarioData();
      this.submitting = true;
      const newProfile = useCreateNewProfileStore();
      const newVocals = useCreateNewVocalsStore();
      const newMedia = useCreateNewMediaStore();

      try {
        const createResp = await api.post<Scenario>('/api/v1/scenarios', this.newScenario, {
          headers: { 'Content-Type': 'application/json' },
        });
        const id = createResp.data.id;
        this.createdId = id;

        if (newProfile.avatarFile || newProfile.summaryImageFile) {
          const imagesData = new FormData();
          if (newProfile.avatarFile) imagesData.append('avatar', newProfile.avatarFile);
          if (newProfile.summaryImageFile) imagesData.append('summary', newProfile.summaryImageFile);
          await api.patch(`/api/v1/images/${id}`, imagesData);
        }

        for (const vocal of newVocals.vocals) {
          const vocalData = new FormData();
          vocalData.append('title', vocal.title);
          vocalData.append('filename', vocal.file);
          await api.put(`/api/v1/vocals/${id}`, vocalData);
        }

        for (const media of newMedia.media) {
          const mediaData = new FormData();
          mediaData.append('title', media.title);
          mediaData.append('filename', media.file);
          await api.put(`/api/v1/media/${id}`, mediaData);
        }

        Notify.create({ color: 'positive', position: 'top', message: 'Scenario created successfully' });
        return id;
      } catch (error) {
        Notify.create({
          color: 'negative',
          position: 'top',
          message: 'Could not create scenario, check the form for errors',
          icon: 'report_problem',
        });
        console.error(error);
        return null;
      } finally {
        this.submitting = false;
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useNewScenarioStore, import.meta.hot));
}
