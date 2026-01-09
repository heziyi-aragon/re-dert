//后端接口映射为前端函数
import request from "@/utils/request"
export function login(data){
    return request({
        url:'/login',
        method:'post',
        data
    })
}
export function getHomeData(){
    return request({
        url:'/home',
        method:'get'
    })
}