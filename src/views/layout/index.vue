<script setup>
// import { ref } from 'vue'
const userInfo = localStorage.getItem('userInfo')
const isAdmin = userInfo.isAdmin === '非管理员' ? false : true
console.log(isAdmin)
</script>

<template>
  <AdminNavIndex v-if="isAdmin"></AdminNavIndex>
  <NavIndex v-else></NavIndex>

  <router-view></router-view>
</template>

<style scoped></style>
