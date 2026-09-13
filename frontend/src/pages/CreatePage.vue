<template>
  <q-page padding>
    <label>Create new-scenario-store</label>
    <create-scenario-stepper></create-scenario-stepper>
  </q-page>
</template>

<script setup lang="ts">
import CreateScenarioStepper from 'src/components/CreateScenarioStepper.vue';

defineOptions({
  name: 'CreatePage',
});
</script>
