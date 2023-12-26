<script setup>
import { ref } from 'vue'
const videoElement = ref(null)
const canvasElement = ref(null)
const photoUrl = ref('')
const imgData = ref('')
const tracks = ref('')
const emit = defineEmits(['confirm', 'imgData'])

navigator.mediaDevices
  .getUserMedia({ video: true })
  .then(function (stream) {
    tracks.value = stream
    videoElement.value.srcObject = stream
  })
  .catch(function (error) {
    console.error('获取摄像头权限失败:', error)
  })

// 确定照片
const checkPhoto = () => {
  // 停止流
  tracks.value.getTracks().forEach((track) => track.stop())
  // 取消当前窗口
  emit('confirm', false)
  emit('imgData', imgData.value)
}

// 拍照事件处理
function capturePhoto() {
  const video = videoElement.value
  const canvas = canvasElement.value
  const context = canvas.getContext('2d')
  context.drawImage(video, 0, 0, canvas.width, canvas.height)
  // 将拍照结果转换为DataURL
  const photoDataUrl = canvas.toDataURL('image/png')
  imgData.value = photoDataUrl.replace(/^data:image\/(png|jpg);base64,/, '')
  photoUrl.value = photoDataUrl
}
</script>
<template>
  <div class="container">
    <h1>人脸信息注册</h1>
    <div class="video-wrapper">
      <video ref="videoElement" autoplay style="transform: scaleX(-1)"></video>
      <canvas ref="canvasElement"></canvas>
    </div>
    <button @click="capturePhoto">拍照</button>
    <button v-show="photoUrl != ''" @click="checkPhoto">确定</button>
    <h2 v-show="photoUrl != ''">拍照结果</h2>
    <img v-show="photoUrl != ''" :src="photoUrl" alt="" />
  </div>
</template>
<style scoped>
h1 {
  color: #fff;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.video-wrapper {
  width: 30%;
  height: 35%;
  position: relative;
}
video,
canvas {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}
video {
  z-index: 2;
}
button {
  margin-top: 10px;
}
img {
  transform: scaleX(-1);
  width: 24%;
  height: 28%;
  margin-bottom: 5%;
}
button {
  width: 70px;
  padding: 5px 10px;
  border-radius: 20px;
  background-color: #257bc4;
  border: none;
  color: #fff;
  font-size: 1rem;
  letter-spacing: 2px;
  transition: background-color ease-out 0.2s;
  cursor: pointer;
}
button:hover {
  background-color: #71a8d8;
}
</style>
