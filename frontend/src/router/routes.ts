import type { RouteRecordRaw } from 'vue-router';
import IndexPage from 'pages/IndexPage.vue';
import CreatePage from 'pages/CreatePage.vue';
import ExportPage from 'pages/ExportPage.vue';
import ImportPage from 'pages/ImportPage.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: IndexPage },
      { path: 'create', component: CreatePage },
      { path: 'export', component: ExportPage },
      { path: 'import', component: ImportPage }
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
