<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
// 路由
const router = useRouter()
// 获取用户信息
const userInfo = JSON.parse(localStorage.getItem('userInfo'))
const username = ref(userInfo.username)
// 获取当前路由地址
const currentPath = ref(router.currentRoute.value.path)
const getpath = (path) => {
  router.push(path)
  console.log(path)
  currentPath.value = path
}
</script>
<template>
  <header>
    <div class="container">
      <h3 class="title">
        <span class="green0">🍇树莓派</span
        ><span class="green">🥂智能会议</span>
        <span class="green1">⚙️管理系统</span>
      </h3>
      <div class="icon">
        <img src="@/assets/bg2.jpg" alt="用户头像" class="avatar" />
        <h3 class="username">{{ username }}</h3>
      </div>
    </div>
  </header>
  <nav>
    <p>⚙️管理员</p>
    <section id="meeting">
      <h1>🪸会议室</h1>
      <div>
        <a
          :class="{ active: currentPath === '/base' }"
          @click="getpath('/base')"
          >🤝会议室基础</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/schedule' }"
          @click="getpath('/schedule')"
          >✍️预定会议</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/check' }"
          @click="getpath('/check')"
          >🔎审核会议</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/lookmeeting' }"
          @click="getpath('/lookmeeting')"
          >🧐查看会议</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/lookroom' }"
          @click="getpath('/lookroom')"
          >👓查看会议室</a
        >
      </div>
    </section>
    <section id="info">
      <div>
        <a
          :class="{ active: currentPath === '/UserInfo' }"
          @click="getpath('/UserInfo')"
          >🧑‍💻个人信息</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/read' }"
          @click="getpath('/read')"
          >❗使用须知</a
        >
      </div>
      <div>
        <a
          :class="{ active: currentPath === '/rule' }"
          @click="getpath('/rule')"
          >📑会议室使用说明</a
        >
      </div>
    </section>
  </nav>
</template>

<style scoped lang="less">
* {
  padding: 0;
  margin: 0;
}
// 头部导航
header {
  position: fixed;
  top: 0;
  left: 15vw;
  width: 85vw;
  height: 10vh;
  background-color: #1890ff;
  .container {
    // 垂直居中
    line-height: 10vh;
    .title {
      float: left;
      margin-left: 10px;
      .green0 {
        color: #c3edda;
      }
      .green {
        color: #19e88b;
      }
      .green1 {
        color: #34435c;
      }
    }
    .icon {
      float: right;
      width: 12vw;
      height: 10vh;
      margin-right: 10%;

      .avatar {
        float: left;
        margin: 2vh;
        width: 6vh;
        height: 6vh;
        border-radius: 50%;
      }

      .username {
        float: right;
        line-height: 10vh;
        font-weight: bold;
      }
    }
  }
}
// 左侧导航
nav {
  width: 15vw;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  background-color:rgba(0, 0, 0, 0.8);
  color: #fff;
  p {
    text-align: center;
    font-weight: 600;
    margin-top: 10%;
  }
  div {
    height: 50px;
  }
  a {
    display: block;
    text-decoration: none;
    text-align: center;
    color: #fff;
    font-weight: 700;
    width: 100%;
    height: 100%;
    line-height: 50px;
    transition: background-color ease-out 0.2s;
    cursor: pointer;
  }
  a:hover {
    background-color: #1890ff;
  }
  #meeting {
    display: flex;
    flex-direction: column;
    margin-top: 15%;
    h1 {
      font-size: 1.5rem;
      padding-left: 10%;
      margin-bottom: 10%;
    }
  }
  #info {
    margin-top: 30%;
  }
}
// 点击链接
.active {
  background-color: #1890ff;
}
</style>
