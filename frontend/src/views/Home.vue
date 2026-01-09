<template>
  <div class="home-container">
    <el-container>
      <el-header class="header">
        <h2>飞行目标检测系统 - 控制台</h2>
        <el-button type="danger" size="small" @click="handleLogout">退出登录</el-button>
      </el-header>
      
      <el-main>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-card>
              <template #header>系统状态</template>
              <div v-if="systemData">
                <p>模型: {{ systemData.model }}</p>
                <p>状态: <el-tag type="success">{{ systemData.system_status }}</el-tag></p>
                <p>当前FPS: {{ systemData.fps }}</p>
              </div>
              <div v-else>加载中...</div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card>
              <template #header>用户信息</template>
              <p>当前用户: {{ user.username }}</p>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { getHomeData } from '@/api/user'

const store = useStore()
const router = useRouter()
const systemData = ref(null)

// 从 Vuex 获取当前用户信息
const user = computed(() => store.state.user)

// 页面加载时获取后端数据
onMounted(async () => {
  try {
    const res = await getHomeData()
    systemData.value = res.data
  } catch (e) {
    console.error(e)
  }
})

const handleLogout = () => {
  store.commit('LOGOUT')
  router.push('/login')
}
</script>

<style scoped>
.header {
  background-color: #409EFF;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}
</style>