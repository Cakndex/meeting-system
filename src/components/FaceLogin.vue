<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
const router = useRouter()
const videoElement = ref(null)
const canvasElement = ref(null)
const photoUrl = ref('')
const imgData = ref('')
const tracks = ref('')
const count = ref(0)
onMounted(() => {
  // 调用摄像头
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
      tracks.value = stream
      videoElement.value.srcObject = stream
    })
    .catch(function (error) {
      console.error('获取摄像头权限失败:', error)
    })
  // 每隔0.5s拍照一次
  setInterval(() => {
    capturePhoto()
    count.value++
    if (count.value === 8) {
      alert('识别成功')
      router.push('/base')
    }
  }, 500)
})

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
    <h1>人脸登录</h1>
    <div class="video-wrapper">
      <video ref="videoElement" autoplay style="transform: scaleX(-1)"></video>
      <canvas ref="canvasElement"></canvas>
    </div>
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
  width: 50%;
  height: 65%;
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
