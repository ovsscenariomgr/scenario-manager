<template>
  <div class="q-pa-md">
    <q-stepper
      v-model="step"
      ref="stepper"
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="Add Header"
        icon="settings"
        :done="step > 1"
      >
        <create-header-step></create-header-step>
      </q-step>

      <q-step
        :name="2"
        title="Add Profile"
        icon="settings"
        :done="step > 2"
      >
        <create-profile-step></create-profile-step>
      </q-step>

      <q-step
        :name="3"
        title="Ad template"
        icon="assignment"
        disable
      >
        This step won't show up because it is disabled.
      </q-step>

      <q-step
        :name="4"
        title="Create an ad"
        icon="add_comment"
      >
        Try out different ad text to see what brings in the most customers, and learn how to
        enhance your ads using features like ad extensions. If you run into any problems with
        your ads, find out how to tell if they're running and how to resolve approval issues.
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn @click="stepper.next()" color="primary" :label="step === 4 ? 'Finish' : 'Continue'" />
          <q-btn v-if="step > 1" flat color="primary" @click="stepper.previous()" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { scenarioStore } from '../stores/scenario-store';
import { NewScenarioStore } from '../stores/new-scenario-store';
import CreateHeaderStep from './CreateHeaderStep.vue'
import CreateProfileStep from './CreateProfileStep.vue';
// import { Scenario } from 'src/types';

defineOptions({
  name: 'ScenarioTableComponent',
});

const step = ref(1)
const stepper = ref(null)
const store = scenarioStore();
const formsStore = NewScenarioStore();

onBeforeMount(() => {
  store.fetchScenarios();
  formsStore.$reset()
});
</script>
