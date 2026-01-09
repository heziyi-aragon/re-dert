import {createRouter,createWebHistory} from 'vue-router'
import store from '../store'

const routes=[
    {
        path:"/login",
        name:"Login",
        component:()=>import('../views/Login.vue')
    },
    {
        path:"/",
        name:"Home",
        component:()=>import('../views/Home.vue'),
        meta:{requiresAuth:true}
    }
]

const router=createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to,from,next)=>{
    const isAuthenticated=store.state.isLoggedIn
    if (to.meta.requiresAuth && !isAuthenticated) {
        // 如果要去需要权限的页面，且未登录，跳转登录页
        next('/login')
      } else {next()}
})
export default router