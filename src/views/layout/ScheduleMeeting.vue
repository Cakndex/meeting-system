<script setup></script>

<template>
  <HeadTitle>
    <template #content>预定会议</template>
  </HeadTitle>
  <section id="body">
    <h1>预定会议</h1>
  </section>
</template>

<style scoped lang="less">
#body {
  z-index: -1;
  position: fixed;
  top: 22vh;
  left: 17vw;
  width: 81vw;
  height: 75vh;
  background-color: #fff;
  overflow-y: scroll;
}
</style>
