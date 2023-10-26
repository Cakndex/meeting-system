import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/login', component: () => import('@/views/login/LoginPage.vue') },
    {
      path: '/',
      component: () => import('@/views/layout/index.vue'),
      children: [
        {
          path: '/base',
          component: () => import('@/views/layout/BasePage.vue')
        },
        {
          path: '/UserInfo',
          component: () => import('@/views/layout/userInfo.VUE')
        }
      ]
    }
  ]
})

export default router
