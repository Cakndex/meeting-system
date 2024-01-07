<script setup>
import { ref, onMounted } from 'vue'
import request from '@/utils/request'
import { useRouter } from 'vue-router'
const router = useRouter()
// 查看会议室
const editmeeting = (id) => {
  console.log(id)
  router.push({ path: '/lookroom/' + id, params: { id: id } })
}
const meetinglist = ref([])
// 获取会议室
const getmeeting = () => {
  request
    .get('/meeting/list')
    .then(function (response) {
      console.log(response)
      meetinglist.value = response.data
    })
    .catch(function (error) {
      console.log(error)
    })
}
onMounted(() => {
  getmeeting()
})
// 删除会议
const deletemeeting = (id) => {
  console.log(`/meeting/delete/${'{' + id + '}'}`)
  request
    .post(`/meeting/delete/${'{' + id + '}'}`, {
      meetId: id
    })
    .then(function (response) {
      console.log(response)
      getmeeting()
    })
    .catch(function (error) {
      console.log(error)
    })
}
</script>

<template>
  <HeadTitle>
    <template #content>会议室基础</template>
  </HeadTitle>
  <section id="body">
    <br /><br /><br />
    <el-table
      :data="meetinglist"
      :border="true"
      style="margin-left: 10%; width: 80%"
    >
      <el-table-column fixed prop="name" label="Name" width="120" />
      <el-table-column prop="meetingId" label="ID" width="120" />
      <el-table-column prop="facility" label="facility" width="200" />
      <el-table-column prop="address" label="Address" width="600" />
      <el-table-column fixed="right" label="Operations" width="120">
        <template #default="scope">
          <el-button
            link
            type="primary"
            size="small"
            @click="editmeeting(scope.row.meetingId)"
            >Detail</el-button
          >
          <el-button
            link
            type="primary"
            size="small"
            @click="deletemeeting(scope.row.meetingId)"
            >Delete</el-button
          >
        </template>
      </el-table-column>
    </el-table>
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
