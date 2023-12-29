<script setup>
import { User, Lock } from '@element-plus/icons-vue'
// import axios from 'axios'
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import request from '@/utils/request'
import useUserStore from '@/stores/user.js'
const userStore = useUserStore()
const router = useRouter()
const isRegister = ref(true) //判断是否注册
const formModel = ref({
  isAdmin: '',
  username: '',
  password: '',
  repassword: '',
  telephone: '',
  job: '',
  imgurl: ''
})
const registercheck = ref(false) // 摄像头遮罩
// 子传父人脸url
const sendurl = (url) => {
  formModel.value.imgurl = url
  console.log(formModel.value.imgurl)
  face_value.value = '人脸已注册'
}
const face_value = ref('人脸注册')
// 数据校验规则
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
  ],

  telephone: [{ required: true, message: '请输入电话号码', trigger: 'blur' }],
  job: [{ required: true, message: '请输入职位', trigger: 'blur' }]
}

// 注册
const register = (username, password, isAdmin, telephone, job, imgurl) => {
  if (username && password && isAdmin && telephone && job && imgurl) {
    request
      .post('/user/register', {
        isAdmin: isAdmin === '非管理员' ? false : true,
        password: password,
        telephone: telephone,
        username: username
        // todo:需要上传url地址
      })
      .then(function (response) {
        console.log(response)
        localStorage.setItem(
          'userInfo',
          JSON.stringify({
            access: response.data.access,
            username: username,
            password: password,
            isAdmin: isAdmin,
            telephone: telephone,
            job: job
          })
        ),
          console.log(localStorage.getItem('userInfo'))
      })
      .catch(function (error) {
        console.log(error)
      })
    alert('注册成功！')
    isRegister.value = true
    // router.push('/') // 跳转到根路由
  }
}
// 判断是否注册
onMounted(() => {
  const user = localStorage.getItem('userInfo')
  const userObj = JSON.parse(user)
  if (userObj != null) {
    isRegister.value = false
  }
})
// 注册校验
const form = ref()
const preregister = async () => {
  await form.value.validate()
}

// 登录
const login_username = ref('')
const login_password = ref('')
const login = () => {
  request
    .post('/user/login', {
      password: login_password.value,
      username: login_username.value
    })
    .then(function (response) {
      console.log(response)
      if (response.status === 200) {
        alert('登录成功')
        // console.log(response)
        userStore.setToken(response.data.access)
        router.push('/')
      }
    })
    .catch(function (error) {
      alert('登录失败！请检查用户名或密码')
      console.log(error)
    })
}
// 人脸识别
const face_login = ref(false)
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
        <!-- 注册 -->
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
          <el-radio-group v-model="formModel.isAdmin" prop="isAdmin">
            <el-radio label="管理员" />
            <el-radio label="非管理员" />
          </el-radio-group>
          <el-form-item label="电话" prop="telephone">
            <el-input v-model="formModel.telephone" placeholder="请输入年龄" />
          </el-form-item>
          <el-form-item label="职位" prop="job">
            <el-input v-model="formModel.job" placeholder="请输入职位" />
          </el-form-item>
          <el-form-item>
            <el-button
              class="button"
              type="primary"
              auto-insert-space
              @click="registercheck = true"
              :disabled="formModel.imgurl != ''"
            >
              {{ face_value }}
            </el-button>
          </el-form-item>
          <el-form-item>
            <el-button
              class="button"
              type="primary"
              auto-insert-space
              @click="
                register(
                  formModel.username,
                  formModel.password,
                  formModel.isAdmin,
                  formModel.telephone,
                  formModel.job,
                  formModel.imgurl
                ),
                  preregister()
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
        <!-- 登录 -->
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
              v-model="login_username"
              :prefix-icon="User"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="login_password"
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
            <el-button
              class="button"
              type="primary"
              auto-insert-space
              @click="face_login = true"
              >人脸登录</el-button
            >
          </el-form-item>
          <el-form-item>
            <el-button
              class="button"
              type="primary"
              auto-insert-space
              @click="login()"
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
  <div id="mask" v-if="registercheck">
    <VideoIndex
      :registercheck="registercheck"
      @confirm="registercheck = false"
      @imgData="sendurl"
    ></VideoIndex>
  </div>
  <div id="face_login" v-if="face_login">
    <FaceLogin></FaceLogin>
  </div>
</template>

<style lang="less" scoped>
.login-page {
  display: flex;
  height: 97.5vh;
  background-color: #fff;
  overflow: hidden;
  .bg-col {
    margin-left: -5%;
    width: 50vw;
    position: relative;
    clip-path: polygon(0% 0%, 90% 0%, 100% 100%, 0% 100%);
    background-color: rgba(243, 186, 243, 0.25);
    .title {
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
#mask,
#face_login {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  background-color: rgba(0, 0, 0, 0.5);
}
</style>
