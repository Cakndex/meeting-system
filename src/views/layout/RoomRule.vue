<script setup></script>

<template>
  <HeadTitle>
    <template #content>会议室使用说明</template>
  </HeadTitle>

  <section id="body">
    <h1>会议室使用说明</h1>
    <div class="content">
      <h2>会议室设施</h2>
      <p>我们的会议室提供以下设施：</p>
      <ul>
        <li><span>投影设备和屏幕</span></li>
        <li><span>音频设备和扬声器</span></li>
        <li><span>会议桌和椅子</span></li>
        <li><span>白板和标记工具</span></li>
        <li><span>高速无线互联网连接</span></li>
      </ul>

      <h2>开放时间</h2>
      <p>会议室对注册用户开放，并在以下时间段内提供预定：</p>
      <ul>
        <li><span>工作日：上午 9:00 - 下午 6:00</span></li>
        <li><span>周末：上午 10:00 - 下午 4:00</span></li>
      </ul>

      <h2>预定流程</h2>
      <p>以下是预定会议室的流程：</p>
      <ol>
        <li><span>登录系统：使用你的用户名和密码登录系统。</span></li>
        <li>
          <span
            >查看会议室：在主菜单中选择“查看会议室”功能，系统将显示可用的会议室列表。</span
          >
        </li>
        <li><span>选择会议室：根据你的需求选择一个适合的会议室。</span></li>
        <li><span>选择时间：选择会议室的预定时间段。</span></li>
        <li><span>提交预定：确认预定信息并提交预定请求。</span></li>
        <li>
          <span
            >等待审核：你的预定请求将被审核，你将收到预定确认或拒绝的通知。</span
          >
        </li>
        <li>
          <span>预定成功：如果预定被确认，你将收到会议室的预定确认通知。</span>
        </li>
      </ol>

      <h2>注意事项</h2>
      <ul>
        <li><span>请提前预定会议室以确保可用性。</span></li>
        <li><span>请按时使用会议室，并在使用完毕后及时离开。</span></li>
        <li><span>请保持会议室的整洁和设备的完好。</span></li>
        <li><span>禁止在会议室内吸烟或食用饭菜。</span></li>
        <li><span>请遵守会议室使用规定和公司的行为准则。</span></li>
      </ul>
    </div>
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
h1 {
  text-align: center;
  color: #333;
}

.content {
  font-family: Arial, sans-serif;
  margin: 20px;
  margin-left: 50px;

  h2 {
    color: #1890ff;
  }

  p {
    color: #999;
  }

  ul {
    list-style-type: disc;
  }
  li {
    margin: 20px auto;
    list-style-type: disc;
    color: #1890ff;
    span {
      color: #333;
    }
  }
}
</style>
