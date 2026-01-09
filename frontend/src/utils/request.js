import axios from 'axios'
import {ElMessage} from 'element-plus'

//axios实例
const service=axios.create({
    baseURL:"/api",  //baseURL必须写规范
    timeout:50000
})
//请求拦截器
service.interceptors.request.use(
    config=>{
        return config
    },
    error=>{
        return Promise.reject(error)
    }
)
//响应拦截器
service.interceptors.response.use(
    response=>{
        const res=response.data//不要忘记写const
        if (res.code!=200){
            ElMessage.error(res.msg||'Error')
            return Promise.reject(new Error(res.msg||'Error'))
        }else{
            return res
        }
    },
    error=>{
        console.log("error"+error)
        ElMessage.error(error.message)
        return Promise.reject(error)
    }
)
export default service