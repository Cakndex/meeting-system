<script setup>
import { User, Lock } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
const isRegister = ref(true)
const formModel = ref({
  username: '',
  password: '',
  repassword: ''
})

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 2, max: 10, message: '用户名必须是5-10位的字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是6-15位的非空字符',
      trigger: 'blur'
    }
  ],
  repassword: [
    { required: true, message: '请再次输入密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是6-15的非空字符',
      trigger: 'blur'
    },
    {
      validator: (rule, value, callback) => {
        if (value !== formModel.value.password) {
          callback(new Error('两次输入密码不一致!'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ]
}

// 注册
const register = (username, password) => {
  localStorage.setItem(
    'userInfo',
    JSON.stringify({
      username: username,
      password: password
    })
  )
  alert('注册成功！')
  isRegister.value = true
}
// 判断是否注册
onMounted(() => {
  const user = localStorage.getItem('userInfo')
  console.log(user)
  if (user) {
    isRegister.value = false
  }
})
// 注册校验
const form = ref()
const preregister = async () => {
  await form.value.validate()
}
</script>

<template>
  <main class="login-page">
    <div class="bg-col">
      <h1 class="title">
        <span class="green0">🍇树莓派</span
        ><span class="green">🥂智能会议</span>
        <span class="green1">⚙️管理系统</span>
      </h1>
      <div class="form-body">
        <el-form
          :model="formModel"
          :rules="rules"
          ref="form"
          size="large"
          autocomplete="off"
          v-if="isRegister"
        >
          <el-form-item>
            <h1 class="title">注册</h1>
          </el-form-item>
          <el-form-item prop="username">
            <el-input
              v-model="formModel.username"
              :prefix-icon="User"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model="formModel.password"
              :prefix-icon="Lock"
              type="password"
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item prop="repassword">
            <el-input
              v-model="formModel.repassword"
              :prefix-icon="Lock"
              type="password"
              placeholder="请输入再次密码"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              class="button"
              type="primary"
              auto-insert-space
              @click="
                register(formModel.username, formModel.password), preregister()
              "
            >
              注册
            </el-button>
          </el-form-item>
          <el-form-item class="flex">
            <el-link type="info" :underline="false" @click="isRegister = false">
              ← 返回
            </el-link>
          </el-form-item>
        </el-form>
        <el-form
          :model="formModel"
          ref="form"
          size="large"
          autocomplete="off"
          :rules="rules"
          v-else
        >
          <el-form-item>
            <h1 class="title">登录</h1>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="formModel.username"
              :prefix-icon="User"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="formModel.password"
              name="password"
              :prefix-icon="Lock"
              type="password"
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item class="flex">
            <div class="flex">
              <el-checkbox>记住我</el-checkbox>
              <br />
              <el-link type="primary" :underline="false">忘记密码？</el-link>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button class="button" type="primary" auto-insert-space
              >登录</el-button
            >
          </el-form-item>
          <el-form-item class="flex">
            <el-link type="info" :underline="false" @click="isRegister = true">
              注册 →
            </el-link>
          </el-form-item>
        </el-form>
      </div>
    </div>
    <div class="form"></div>
  </main>
</template>

<style lang="less" scoped>
.login-page {
  display: flex;
  height: 100vh;
  background-color: #fff;
  .bg-col {
    margin-left: -5%;
    width: 50vw;
    position: relative;
    clip-path: polygon(0% 0%, 90% 0%, 100% 100%, 0% 100%);
    background-color: rgba(243, 186, 243, 0.25);
    .title {
      margin-top: 15%;
      text-align: center;
      color: #162b22;
      .green0 {
        color: #afdec9;
      }
      .green {
        color: #43ba85;
      }
      .green1 {
        color: #34435c;
      }
    }
    .bg {
      position: absolute;
      left: 20%;
      top: 30%;
      width: 60%;
      border-radius: 20px;
    }

    .form-body {
      width: 50%;
      border: #fff 2px solid;
      margin-left: 25%;
      padding: 20px;
      background: rgba(255, 255, 255, 0.7);
      border-radius: 20px;
      transition: background-color linear 0.15s;

      .title {
        margin: 0 auto;
      }
      .button {
        width: 100%;
      }
    }
  }
  .form-body:hover {
    background: rgba(255, 255, 255, 0.95);
  }
  .form {
    width: 60vw;
    background: url('@/assets/bg1.jpg') no-repeat center / cover;
  }
}
</style>
