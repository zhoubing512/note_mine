<template>
    <div class="login_container">
        <div class="login_box">
            <!-- 头像区域 -->
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
            </div>
            <!-- 登录表单区域 -->
            <el-form ref="loginFormRef" :model="login_form" :rules="loginFormRules" label-width="0px" class="login_form">
                <!-- 用户名 -->
                <el-form-item  prop="username">
                    <el-input v-model="login_form.username" prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input v-model="login_form.password" prefix-icon="el-icon-lock" type="password"></el-input>
                </el-form-item>
                <!-- 提交按钮 -->
                <el-form-item class="btns">
                    <el-button type="primary" @click="login">登录</el-button>
                    <el-button type="info"  @click="resetLoginForm">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return {
            login_form:{
                username:'zhoubing',
                password:'zbzbaa',
            },
            // 表单的验证规则
            loginFormRules:{
                username:[
                    {required:true,message:'请输入登录名',trigger:'blur'},
                    {min: 3 ,max: 10 ,message:'长度在3 到 10个字符之间', trigger:'blur'}
                ],
                password:[
                    {required:true,message:'请输入登录密码',trigger:'blur'},
                    {min: 6 ,max: 15 ,message:'长度在6 到 15个字符之间', trigger:'blur'}
                ],
            }
        }
    },
    methods:{
        resetLoginForm(){
            // console.log(this)
            this.$refs.loginFormRef.resetFields();
        }, 
        login(){
            this.$refs.loginFormRef.validate(async valid => {
                // console.log(valid)
                if(!valid) return ;
                // const result = this.$http.get('student_list');
                // console.log(result);
                const {data:res} = await this.$http.get('student_list');
                console.log(res);
                this.$router.push("/home");
            })
        }
    }
}
</script>

<style lang="less" scoped>
.login_container{
    background: #42b983;
    height: 100%;
}
.login_box{
    width: 450px;
    height: 300px;
    background-color: #ffffff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.avatar_box{
    height: 130px;
    width: 130px;
    border:1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color: #fff;
    img{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;
    }
}
.login_form{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
}
.btns{
    display: flex;
    justify-content: flex-end;
}
</style>
