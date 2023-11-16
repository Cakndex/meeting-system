import { defineStore } from 'pinia'
import { ref } from 'vue'

// 用户模块
const useUserStore = defineStore(
  'user',
  () => {
    const token = ref(localStorage.getItem('token') || '') // 从本地存储获取 token 的初始值

    const setToken = (t) => {
      token.value = t
      localStorage.setItem('token', t) // 将 token 存储到本地存储
    }

    return { token, setToken }
  },
  {
    persist: true // 持久化
  }
)

export default useUserStore
