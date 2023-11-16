<script setup>
import { ref } from 'vue'
const user = JSON.parse(localStorage.getItem('userInfo'))
const userInfo = ref({
  username: user.username, // 用户昵称
  password: user.password, // 用户密码
  telephone: user.telephone, // 用户电话
  isAdmin: user.isAdmin, // 用户是否为管理员
  job: user.job // 用户职位
})

const isDisabled = ref(true) // 输入框禁用状态

const formRules = {
  username: [
    { required: true, message: '请输入昵称', trigger: 'blur' },
    { min: 2, max: 10, message: '昵称长度在2-10之间', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是6-15位的非空字符',
      trigger: 'blur'
    }
  ]
}

const userInfoForm = ref()
const toggleDisabled = () => {
  isDisabled.value = !isDisabled.value
  if (isDisabled.value) {
    // 取消编辑时重置表单
    userInfoForm.value.resetFields()
  }
}

const saveChanges = () => {
  userInfoForm.value.validate((valid) => {
    if (valid) {
      // 提交表单数据
      // 在此处处理确认修改的逻辑
      console.log('Form data is valid. Submitting changes...')
      localStorage.setItem('userInfo', JSON.stringify(userInfo.value))
      console.log(JSON.stringify(userInfo.value))
      isDisabled.value = true
      location.reload()
    } else {
      // 表单校验不通过
      console.log('Form data is invalid. Please check the input fields.')
    }
  })
}
</script>

<template>
  <HeadTitle>
    <template #content>个人信息</template>
  </HeadTitle>

  <section id="body">
    <div>
      <el-form
        ref="userInfoForm"
        :model="userInfo"
        :rules="formRules"
        label-width="100px"
      >
        <el-form-item label="" class="avatar">
          <div class="avatar-container">
            <!-- 在此处展示头像 -->
            <img src="@/assets/bg2.jpg" alt="" />
          </div>
        </el-form-item>
        <el-form-item label="昵称" prop="username">
          <el-input
            v-model="userInfo.username"
            :disabled="isDisabled"
            style="width: 15vw"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="userInfo.password"
            :disabled="isDisabled"
            show-password
            style="width: 15vw"
          ></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="telephone">
          <el-input
            v-model="userInfo.telephone"
            :disabled="isDisabled"
            style="width: 10vw"
          ></el-input>
        </el-form-item>
        <el-form-item label="管理权限" prop="isAdmin">
          <el-input
            v-model="userInfo.isAdmin"
            :disabled="isDisabled"
            style="width: 10vw"
          ></el-input>
        </el-form-item>
        <el-form-item label="职位" prop="job">
          <el-input
            v-model="userInfo.job"
            :disabled="isDisabled"
            style="width: 15vw"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="toggleDisabled" type="primary">{{
            isDisabled ? '编辑' : '取消编辑'
          }}</el-button>
          <el-button @click="saveChanges" type="primary" v-show="!isDisabled"
            >确认修改</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </section>
</template>

<style scoped lang="less">
#body {
  position: fixed;
  top: 22vh;
  left: 17vw;
  width: 81vw;
  height: 75vh;
  background-color: #fff;
}
// 头像
.avatar-container {
  margin-top: 5vh;
  margin-bottom: 5vh;
  margin-left: 2vw;
  height: 150px;
  img {
    width: 150px;
    height: 100%;
    border-radius: 50%;
  }
}
</style>
