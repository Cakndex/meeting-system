<script setup>
import { computed, ref, onMounted } from 'vue'
import request from '@/utils/request.js'
import {
  Iphone,
  Location,
  OfficeBuilding,
  Tickets,
  User
} from '@element-plus/icons-vue'
const userlist = ref('[]')
// 获取使用者
onMounted(() => {
  request
    .get('/user/all')
    .then(function (response) {
      userlist.value = response.data.list
      console.log(userlist.value)
    })
    .catch(function (error) {
      console.log(error)
    })
})

const size = ref('')
const iconStyle = computed(() => {
  const marginMap = {
    large: '8px',
    default: '6px',
    small: '4px'
  }
  return {
    marginRight: marginMap[size.value] || marginMap.default
  }
})
// 切换状态
const change = (id) => {
  request
    .post(
      '/user/banned',
      {
        userId: id,
        value: false
      },
      {
        headers: {
          'Access-Control-Allow-Origin': '*'
        }
      }
    )
    .then(function (response) {
      console.log(response.data)
      alert('删除成功')
    })
    .catch(function (error) {
      console.log(error)
    })
}
</script>

<template>
  <HeadTitle>
    <template #content>人员管理</template>
  </HeadTitle>
  <section id="body">
    <h1>这是人员管理</h1>
    <el-descriptions
      class="margin-top container"
      v-for="(item, index) in userlist"
      :key="item.id"
      :title="`人员${index + 1}`"
      :column="3"
      :size="size"
      border
    >
      <template #extra>
        <el-button type="primary" @click="change(item.id)">remove</el-button>
      </template>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon :style="iconStyle">
              <user />
            </el-icon>
            Username
          </div>
        </template>
        {{ item.username }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon :style="iconStyle">
              <iphone />
            </el-icon>
            Telephone
          </div>
        </template>
        {{ item.telephone }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon :style="iconStyle">
              <location />
            </el-icon>
            status
          </div>
        </template>
        {{ item.banned === false ? '正常' : '禁用' }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon :style="iconStyle">
              <tickets />
            </el-icon>
            Remarks
          </div>
        </template>
        <el-tag size="small">User</el-tag>
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon :style="iconStyle">
              <office-building />
            </el-icon>
            Address
          </div>
        </template>
        No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
      </el-descriptions-item>
    </el-descriptions>
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
.el-descriptions {
  margin-top: 20px;
}
.cell-item {
  display: flex;
  align-items: center;
}
.margin-top {
  margin-top: 20px;
}
.container {
  padding: 0 40px;
}
</style>
