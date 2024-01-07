<script setup>
import { ref } from 'vue'
import request from '@/utils/request'

// do not use same name with ref
const form = ref({
  ID: '',
  name: '',
  status: false,
  facilities: [],
  address: ''
})
// 取消
const cancel = () => {
  form.value = {
    ID: '',
    name: '',
    status: false,
    facilities: [],
    address: ''
  }
}
// 提交
const onSubmit = () => {
  request
    .post('/meeting/add', {
      id: form.value.ID,
      name: form.value.name,
      address: form.value.address,
      facilities: form.value.facilities
    })
    .then(function (response) {
      console.log(response)
      alert('添加成功')
      cancel()
    })
    .catch(function (error) {
      alert('post(/meeting/add)请求失败')
      console.log(error)
    })
}
// 配置表单校验
const rules = {
  ID: [{ required: true, message: '请输入ID', trigger: 'blur' }],
  name: [{ required: true, message: '请输入会议室名称', trigger: 'blur' }],
  address: [{ required: true, message: '请输入会议室地址', trigger: 'blur' }]
}
</script>

<template>
  <HeadTitle>
    <template #content>添加会议室</template>
  </HeadTitle>
  <section id="body">
    <br />
    <br />
    <br />
    <br />
    <el-form :model="form" label-width="120px" :rules="rules">
      <el-form-item label="会议室ID" prop="ID">
        <el-input v-model="form.ID" style="width: 150px" />
      </el-form-item>
      <el-form-item label="会议室名称" prop="name">
        <el-input v-model="form.name" style="width: 300px" />
      </el-form-item>
      <el-form-item label="使用状态">
        <el-switch v-model="form.status" />
      </el-form-item>
      <el-form-item label="facilities">
        <el-checkbox-group v-model="form.facilities">
          <el-checkbox label="空调" name="type" />
          <el-checkbox label="投影仪" name="type" />
          <el-checkbox label="黑板" name="type" />
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="address" prop="address">
        <el-input v-model="form.address" type="textarea" style="width: 500px" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Create</el-button>
        <el-button @click="cancel()">Cancel</el-button>
      </el-form-item>
    </el-form>
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
