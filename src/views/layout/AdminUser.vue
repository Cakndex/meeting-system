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
const getuser = () => {
  request
    .get('/user/all')
    .then(function (response) {
      userlist.value = response.data.list
      console.log(userlist.value)
    })
    .catch(function (error) {
      console.log(error)
    })
}
onMounted(() => {
  getuser()
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
const change = (id, value) => {
  console.log(id)
  request
    .post('/user/banned', {
      userId: id,
      value: !value
    })
    .then(() => {
      alert('删除成功')
      getuser()
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
        <el-button type="primary" @click="change(item.userId, item.banned)"
          >remove</el-button
        >
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
        <span :class="{ banned: item.banned === true }">{{
          item.username
        }}</span>
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
        <span :class="{ banned: item.banned === true }">{{
          item.telephone
        }}</span>
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
        <span> {{ item.banned === false ? '正常' : '禁用' }}</span>
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
        <span :class="{ banned: item.banned === true }"
          >No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu
          Province</span
        >
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
.banned {
  color: #e8e8e8;
}
</style>
