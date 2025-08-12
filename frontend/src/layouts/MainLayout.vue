<template>
  <div class="q-pa-md">
    <q-layout view="hHh Lpr lff" class="shadow-2 rounded-borders">
      <q-header elevated :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'">
        <q-toolbar>
          <q-btn dense flat round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />
          <q-toolbar-title>
            <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          OVS Scenario Manager
        </q-toolbar-title>
        <div class="q-pa-sm">
          <q-toggle
            v-model="darkMode"
            dark
            label="Dark Mode"
            color="grey"
            :icon="$q.dark.isActive ? 'bi-moon' : 'bi-brightness-high'"
            @click="$q.dark.toggle()"
          />
        </div>
        <q-separator dark vertical />
        <div class="q-pa-sm">Quasar v{{ $q.version }}</div>
        </q-toolbar>
      </q-header>

      <q-drawer
        v-model="leftDrawerOpen"
        show-if-above

        :mini="miniState"
        @mouseenter="miniState = false"
        @mouseleave="miniState = true"
        mini-to-overlay

        :width="200"
        :breakpoint="500"
        bordered
        :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
      >
        <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: '' }">
          <q-list padding>
            <q-item clickable v-ripple @click="$router.push('/')">
              <q-item-section avatar>
                <q-icon name="table_rows" />
              </q-item-section>

              <q-item-section>
                Scenarios
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple @click="$router.push('create')">
              <q-item-section avatar>
                <q-icon name="add" />
              </q-item-section>

              <q-item-section>
                Create
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple @click="$router.push('export')">
              <q-item-section avatar>
                <q-icon name="file_download" />
              </q-item-section>

              <q-item-section>
                Export
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple @click="$router.push('import')">
              <q-item-section avatar>
                <q-icon name="upload" />
              </q-item-section>

              <q-item-section>
                Import
              </q-item-section>
            </q-item>

            <q-separator />

            <q-item v-if="!appAuthStore.loggedOut" clickable v-ripple @click="appAuthStore.logout()">
              <q-item-section avatar>
                <q-icon name="logout" />
              </q-item-section>

              <q-item-section>
                 Logout
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
      </q-drawer>

      <q-page-container>
        <router-view />
      </q-page-container>
      <LoginForm></LoginForm>
    </q-layout>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import LoginForm from 'components/auth/LoginForm.vue';
import { useAppAuthStore } from '../stores/app-auth-store';

defineOptions({
  name: 'MainLayout',
});

const appAuthStore = useAppAuthStore();
const leftDrawerOpen = ref(false);
const darkMode = ref(false);
const miniState = ref(true)

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
