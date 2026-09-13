import { defineStore, acceptHMRUpdate } from 'pinia';

export interface PendingVocalFile {
  file: File;
  title: string;
}

export const useCreateNewVocalsStore = defineStore('CreateNewVocalsStore', {
  state: () => ({
    vocals: [] as PendingVocalFile[],
  }),
  getters: {},
  actions: {
    addFiles(files: readonly File[]) {
      for (const file of files) {
        this.vocals.push({ file, title: file.name });
      }
    },
    removeVocal(index: number) {
      this.vocals.splice(index, 1);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewVocalsStore, import.meta.hot));
}
