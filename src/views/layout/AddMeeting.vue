<script setup>
import { ref } from 'vue'

// do not use same name with ref
const form = ref({
  ID: '',
  name: '',
  status: false,
  facilities: [],
  address: ''
})

const cancel = () => {
  form.value = {
    ID: '',
    name: '',
    status: false,
    facilities: [],
    address: ''
  }
}

const onSubmit = () => {
  console.log('submit!')
}
</script>

<template>
  <HeadTitle>
    <template #content>添加会议室</template>
  </HeadTitle>
  <section id="body">
    <h1>添加会议室</h1>
    <el-form :model="form" label-width="120px">
      <el-form-item label="会议室ID">
        <el-input v-model="form.ID" style="width: 150px" />
      </el-form-item>
      <el-form-item label="会议室名称">
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
      <el-form-item label="address">
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
