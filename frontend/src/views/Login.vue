<template>
  <div class="login-container">
    <el-card class="login-card">
      <template #header>
        <div class="card-header">
          <span>RT-DETR 系统登录</span>
        </div>
      </template>
      
      <el-form :model="loginForm" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="loginForm.username" placeholder="请输入用户名 (admin)" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="loginForm.password" type="password" placeholder="请输入密码 (123456)" show-password />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin" :loading="loading">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { login } from '@/api/user'
import { ElMessage } from 'element-plus'

const store = useStore()
const router = useRouter()

const loading = ref(false)
const loginForm = reactive({
  username: '',
  password: ''
})

const handleLogin = async () => {
  if(!loginForm.username || !loginForm.password) {
    ElMessage.warning('请输入用户名和密码')
    return
  }

  loading.value = true
  try {
    // 调用 API
    const res = await login(loginForm)
    // 存入 Vuex
    store.commit('SET_USER', res.data)
    ElMessage.success('登录成功')
    // 跳转首页
    router.push('/')
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}
.login-card {
  width: 400px;
}
.card-header {
  text-align: center;
  font-weight: bold;
}
</style>