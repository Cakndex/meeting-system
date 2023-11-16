<script setup>
// import { ref } from 'vue'
const userInfo = localStorage.getItem('userInfo')
const isAdmin = userInfo.isAdmin === '非管理员' ? false : true
</script>

<template>
  <NavIndex v-if="isAdmin"></NavIndex>
  <AdminNavIndex v-else></AdminNavIndex>
  <router-view></router-view>
</template>

<style scoped></style>
