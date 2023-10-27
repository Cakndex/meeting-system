<script setup></script>

<template>
  <section id="bg">
    <div class="content">
      <p>管理员 > 会议室管理 > <slot name="content"></slot></p>
      <p><slot name="content" class="title"></slot></p>
    </div>
  </section>
</template>

<style scoped lang="less">
#bg {
  position: fixed;
  right: 0;
  z-index: -1;
  width: 100vw;
  height: 100vh;
  background-color: #e8e8e8;
  .content {
    z-index: 5;
    position: fixed;
    right: 0;
    top: 10vh;
    height: 10vh;
    width: 85vw;
    background-color: #fff;
    p:nth-child(1) {
      margin-left: 2vw;
      font-size: 0.9rem;
      color: #b9b7c4;
    }
    p:nth-child(2) {
      margin-left: 2vw;
      font-weight: 600;
      font-size: 1rem;
      letter-spacing: 2px;
    }
  }
}
</style>
