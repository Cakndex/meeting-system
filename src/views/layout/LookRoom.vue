<script setup>
import { ref, onMounted, getCurrentInstance } from 'vue'
import request from '@/utils/request'
import { useRouter } from 'vue-router'
const router = useRouter()
const meetId = ref()
const instance = getCurrentInstance()
const meetinglist = ref([])
onMounted(() => {
  // 转数字
  meetId.value = +instance.proxy.$route.params.id
  // 使用路由参数
  console.log('meetId:', meetId.value)
  request
    .get('/meeting/list')
    .then(function (response) {
      console.log(response.data)
      meetinglist.value = response.data
      const foundMeeting = meetinglist.value.find(
        (item) => item.meetingId === meetId.value
      )

      if (foundMeeting) {
        // 找到了满足条件的元素
        const facilityArray = foundMeeting.facility.split(',')
        form.value = {
          ID: foundMeeting.meetingId,
          name: foundMeeting.name,
          status: true,
          facilities: facilityArray,
          address: foundMeeting.address
        }
      } else {
        // 没有找到满足条件的元素
        console.log('未找到满足条件的元素')
      }
    })
    .catch(function (error) {
      console.log(error)
    })
})

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
    .post('/meeting/change', {
      id: form.value.ID,
      name: form.value.name,
      address: form.value.address,
      facilities: form.value.facilities
    })
    .then(function (response) {
      console.log(form.value)
      console.log(response)
      alert('修改成功')
      cancel()
      router.go(-1)
    })
    .catch(function (error) {
      alert('post(/meeting/change)请求失败')
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
    <template #content>查看会议室</template>
  </HeadTitle>
  <section id="body">
    <h3 @click="router.go(-1)">返回</h3>
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
        <el-button type="primary" @click="onSubmit">Finish</el-button>
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
h3 {
  width: max-content;
  cursor: pointer;
  margin-left: 50px;
  color: #1890ff;
  padding: 5px 10px;
  border: #1890ff 2px solid;
  border-radius: 20px;
}
</style>
