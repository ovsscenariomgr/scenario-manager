import { defineStore, acceptHMRUpdate } from 'pinia';

export interface PendingMediaFile {
  file: File;
  title: string;
}

export const useCreateNewMediaStore = defineStore('CreateNewMediaStore', {
  state: () => ({
    media: [] as PendingMediaFile[],
  }),
  getters: {},
  actions: {
    addFiles(files: readonly File[]) {
      for (const file of files) {
        this.media.push({ file, title: file.name });
      }
    },
    removeMedia(index: number) {
      this.media.splice(index, 1);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewMediaStore, import.meta.hot));
}
