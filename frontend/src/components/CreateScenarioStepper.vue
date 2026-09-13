<template>
  <div class="q-pa-md">
    <q-stepper v-model="step" ref="stepper" color="primary" animated>
      <q-step :name="1" title="Header" icon="settings" :done="step > 1">
        <create-header-step></create-header-step>
      </q-step>

      <q-step :name="2" title="Profile" icon="settings" :done="step > 2">
        <create-profile-step></create-profile-step>
      </q-step>

      <q-step :name="3" title="Vocals" icon="mic" :done="step > 3">
        <create-vocals-step></create-vocals-step>
      </q-step>

      <q-step :name="4" title="Media" icon="perm_media" :done="step > 4">
        <create-media-step></create-media-step>
      </q-step>

      <q-step :name="5" title="Scenario Init" icon="favorite" :done="step > 5">
        <create-scenario-init-step></create-scenario-init-step>
      </q-step>

      <q-step :name="6" title="Events" icon="event" :done="step > 6">
        <create-event-groups-step></create-event-groups-step>
      </q-step>

      <q-step :name="7" title="Scenes" icon="movie" :done="step > 7">
        <create-scenes-step></create-scenes-step>
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn
            @click="handleContinue()"
            color="primary"
            :loading="newScenarioStore.submitting"
            :label="step === 7 ? 'Finish' : 'Continue'"
          />
          <q-btn v-if="step > 1" flat color="primary" @click="stepper?.previous()" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import type { QStepper } from 'quasar';
import { useRouter } from 'vue-router';
import { useScenarioStore } from '../stores/scenario-store';
import { useNewScenarioStore } from '../stores/new-scenario-store';
import CreateHeaderStep from './CreateHeaderStep.vue';
import CreateProfileStep from './CreateProfileStep.vue';
import CreateVocalsStep from './CreateVocalsStep.vue';
import CreateMediaStep from './CreateMediaStep.vue';
import CreateScenarioInitStep from './CreateScenarioInitStep.vue';
import CreateEventGroupsStep from './CreateEventGroupsStep.vue';
import CreateScenesStep from './CreateScenesStep.vue';

defineOptions({
  name: 'CreateScenarioStepper',
});

const LAST_STEP = 7;

const step = ref(1);
const stepper = ref<QStepper | null>(null);
const store = useScenarioStore();
const newScenarioStore = useNewScenarioStore();
const router = useRouter();

const handleContinue = async () => {
  if (step.value === LAST_STEP) {
    const id = await newScenarioStore.submitScenario();
    if (id !== null) {
      await router.push('/');
    }
    return;
  }
  stepper.value?.next();
};

onBeforeMount(() => {
  store.fetchScenarios();
  newScenarioStore.$reset();
});
</script>
