import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/login', component: () => import('@/views/login/LoginPage.vue') },
    {
      path: '/',
      component: () => import('@/views/layout/index.vue'),
      children: [
        // 会议室基础面板
        {
          path: '/base',
          component: () => import('@/views/layout/BasePage.vue')
        },
        // 个人信息
        {
          path: '/UserInfo',
          component: () => import('@/views/layout/userInfo.VUE')
        },
        // 使用须知
        {
          path: '/read',
          component: () => import('@/views/layout/NeedRead.vue')
        },
        // 会议室使用说明
        {
          path: 'rule',
          component: () => import('@/views/layout/RoomRule.vue')
        }
      ]
    }
  ]
})

export default router
