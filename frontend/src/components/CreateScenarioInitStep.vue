<template>
  <q-form>
    <div class="q-pa-sm">
      <q-card bordered>
        <q-card-section>
          <div class="q-ma-sm text-h5">Scenario Init</div>
          <div class="row q-col-gutter-sm q-mb-md">
            <div class="col-6 col-md-3">
              <q-input
                v-model.number="formStore.scenarioInit.initial_scene"
                type="number"
                label="Initial Scene"
                dense
              />
            </div>
            <div class="col-6 col-md-3">
              <q-toggle v-model="formStore.scenarioInit.record" :true-value="1" :false-value="0" label="Record" />
            </div>
          </div>
          <cardiac-respiration-general-fields
            v-model:cardiac="formStore.scenarioInit.cardiac"
            v-model:respiration="formStore.scenarioInit.respiration"
            v-model:general="formStore.scenarioInit.general"
          />
        </q-card-section>
      </q-card>
    </div>
  </q-form>
</template>

<script setup lang="ts">
import { useCreateNewScenarioInitStore } from '../stores/create-new-scenario-init-store';
import CardiacRespirationGeneralFields from './CardiacRespirationGeneralFields.vue';

defineOptions({
  name: 'CreateScenarioInitStep',
});

const formStore = useCreateNewScenarioInitStore();
</script>
