//通过状态管理Vuex 存储当前登录的用户
import {createStore} from 'vuex'
export default createStore({
    //状态
    state:{
        user:JSON.parse(localStorage.getItem('user'))||null,
        isLoggedIn:!!localStorage.getItem('user')
    },
    //修改状态的方法
    mutations:{
        SET_USER(state,user){
            state.user=user
            state.isLoggedIn=true
            localStorage.setItem('user',JSON.stringify(user))
        },
        //登出
        LOGOUT(state){
            state.user=null
            state.isLoggedIn=false
            localStorage.removeItem('user')
        }
    }
    //action:{//可以放异步操作}
})