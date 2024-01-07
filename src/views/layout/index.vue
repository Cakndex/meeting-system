<script setup>
// import { ref } from 'vue'
const userInfo = JSON.parse(localStorage.getItem('userInfo'))
// const isAdmin = userInfo.isAdmin === '管理员' ? true : false
console.log(userInfo)
</script>

<template>
  <AdminNavIndex v-if="true"></AdminNavIndex>
  <NavIndex v-else></NavIndex>

  <router-view></router-view>
</template>

<style scoped></style>
