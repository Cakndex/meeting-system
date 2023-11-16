/* 封装axios用于发送请求 */
// import store from '@/store'
import axios from 'axios'
// import router from '../router'
import useUserStore from '@/stores/user.js'
// import { Toast } from 'vant'
// 创建一个新的axios实例
const userStore = useUserStore()
const request = axios.create({
  baseURL: 'http://192.168.1.111:63000/',
  timeout: 5000
})

// 添加请求拦截器
request.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    const token = userStore.token
    console.log(token)
    if (token) {
      // console.log(token)
      config.headers.Authorization = 'Bearer ' + token
    }
    return config
  },
  function (error) {
    // 对请求错误做些什么

    return Promise.reject(error)
  }
)

// // 添加响应拦截器
// request.interceptors.response.use(
//   function (response) {
//     // 对响应数据做点什么
//     const res = response.data
//     if (res.status !== 200) {
//       return Promise.reject(res.message)
//     }
//     return res
//   },
//   function (error) {
//     // 对响应错误做点什么
//     if (error.response.status === 403) {
//       router.push('login')
//     }
//     alert('数据相应失败')
//     return Promise.reject(error)
//   }
// )

export default request
