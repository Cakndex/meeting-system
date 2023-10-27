<script setup></script>

<template>
  <HeadTitle>
    <template #content>使用须知</template>
  </HeadTitle>

  <section id="body">
    <div class="content">
      <h1>使用须知</h1>

      <h2>主要功能</h2>
      <ul>
        <li>
          <span
            >查看会议：可以查看系统中已安排的会议信息，包括会议名称、时间、地点等。</span
          >
        </li>
        <li>
          <span
            >审核会议：具有审核权限的用户可以审核待安排的会议，确保会议信息的准确性。</span
          >
        </li>
        <li>
          <span
            >添加会议：具有添加权限的用户可以添加新的会议，包括会议名称、时间、地点等信息。</span
          >
        </li>
        <li>
          <span
            >查看会议室：可以查看系统中的会议室信息，包括会议室名称、容纳人数、设备等。</span
          >
        </li>
      </ul>

      <h2>使用说明</h2>
      <p>以下是树莓派智能会议管理系统的使用说明：</p>
      <ol>
        <li><span>登录系统：使用你的用户名和密码登录系统。</span></li>
        <li>
          <span
            >查看会议：在主菜单中选择“查看会议”功能，系统将显示已安排的会议列表</span
          >。
        </li>
        <li>
          <span
            >审核会议：如果你具有审核权限，在主菜单中选择“审核会议”功能，可以对待安排的会议进行审核。</span
          >
        </li>
        <li>
          <span
            >添加会议：如果你具有添加权限，在主菜单中选择“添加会议”功能，填写会议信息并保存。</span
          >
        </li>
        <li>
          <span
            >查看会议室：在主菜单中选择“查看会议室”功能，系统将显示会议室列表。</span
          >
        </li>
      </ol>

      <p>请确保你具有相应的权限才能执行对应的操作。</p>
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
.content {
  font-family: Arial, sans-serif;
  margin: 20px;
  margin-left: 50px;
  h1 {
    text-align: center;
    color: #333;
  }

  h2 {
    color: #1890ff;
  }

  p {
    color: #999;
  }

  ul {
    list-style-type: disc;
    margin-left: 20px;
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
