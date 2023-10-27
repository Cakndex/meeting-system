import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/login', component: () => import('@/views/login/LoginPage.vue') },
    {
      path: '/',
      component: () => import('@/views/layout/index.vue'),
      redirect: '/base',
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
        },
        // 预定会议
        {
          path: '/schedule',
          component: () => import('@/views/layout/ScheduleMeeting.vue')
        },
        // 审核会议
        {
          path: '/check',
          component: () => import('@/views/layout/CheckMeeting.vue')
        },
        // 查看会议
        {
          path: '/lookmeeting',
          component: () => import('@/views/layout/LookMeeting.vue')
        },
        // 查看会议室
        {
          path: '/lookRoom',
          component: () => import('@/views/layout/LookRoom.vue')
        }
      ]
    }
  ]
})

export default router
