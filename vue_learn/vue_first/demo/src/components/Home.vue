<template>
    <el-container class="home-container">
        <!-- 头部区域 -->
        <el-header>
            <div>
                <img src="../assets/heima.png" alt="">
                <span>营销导航系统</span>
            </div>
            <el-button type="info" @click="logout">退出</el-button>
        </el-header>
        <!-- 页面主题区域 -->
        <el-container>
            <!-- 侧边栏 -->
            <el-aside :width="isCollapse?'64px':'200px'">
                <div class="toggle-button" @click="toggleCollapse">|||</div>
                <!-- 侧边栏菜单区域 -->
                <el-menu background-color="#333744"  text-color="#fff"  active-text-color="#409BFF" 
                :unique-opened="true" :collapse="isCollapse" :collapse-transition="false" :router="true" :default-active="activePath">
                    <!-- 一级菜单 -->
                <el-submenu :index="item.id+''" v-for="item in menulist" :key="item.id">
                    <!-- 一级菜单模板区域 -->
                    <template slot="title">
                        <!-- 图标 -->
                    <i :class="iconsObj[item.id]"></i>
                    <!-- 文本 -->
                    <span>{{item.authName}}</span>
                    </template>
                    <!-- 二级菜单 -->
                    <el-menu-item :index="'/'+subitem.path" v-for="subitem in item.children" :key="subitem.id" 
                    @click="saveNavState('/'+subitem.path)">
                        <template slot="title">
                            <!-- 图标 -->
                        <i class="el-icon-menu"></i>
                        <!-- 文本 -->
                        <span>{{subitem.authName}}</span>
                        </template>
                    </el-menu-item>
                </el-submenu>
                </el-menu>
            </el-aside>
            <!-- 右侧内容主体 -->
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
export default {
    data(){
        return{
            //被激活的链接地址
            activePath:'',
            //是否折叠
            isCollapse:false,
            iconsObj:{
                '101':'el-icon-user-solid',
                '201':'el-icon-info',
                '301':'el-icon-upload',
                '401':'el-icon-thumb'
            },
            menulist:[{
                "id": 101,
                "authName": "客户满意",
                "path": null,
                "children": [
                    {
                        "id": 1011,
                        "authName": "不满意客户",
                        "path": "unsatisfy",
                    },
                    {
                        "id": 1012,
                        "authName": "不稳定客户",
                        "path": "unstable",
                    },
                    {
                        "id": 1013,
                        "authName": "客户投诉",
                        "path": "complaint",
                    },
                    {
                        "id": 1014,
                        "authName": "客户关怀",
                        "path": "care",
                    }
                ]
            },
            {
                "id": 201,
                "authName": "市场掌控",
                "path": null,
                "children": [
                    {
                        "id": 2011,
                        "authName": "渠道分级展示",
                        "path": "grading",
                    },
                    {
                        "id": 2012,
                        "authName": "渠道能力评估",
                        "path": "ability",
                    },
                    {
                        "id": 2013,
                        "authName": "微网格展示",
                        "path": "grid",
                    },
                    {
                        "id": 2014,
                        "authName": "渠道效益评估",
                        "path": "benefit",
                    }
                ]
            },
            {
                "id": 301,
                "authName": "价值提升",
                "path": null,
                "children": [
                    {
                        "id": 3011,
                        "authName": "营销机会",
                        "path": "marketing",
                    }
                ]
            },
            {
                "id": 401,
                "authName": "竞争掌控",
                "path": null,
                "children": [
                    {
                        "id": 4011,
                        "authName": "竞争信息",
                        "path": "competition",
                    }
                ]
            }
            ]
        }
    },
    created(){
        this.getMenuList()
        this.activePath=window.sessionStorage.getItem('activePath')
    },
    methods:{
        logout(){
            this.$router.push('/login')
        },
        //获取所有的菜单
        getMenuList(){
        },
        //点击按钮，切换菜单的折叠展开
        toggleCollapse(){
            this.isCollapse = !this.isCollapse
        },
        saveNavState(activePath){
            window.sessionStorage.setItem('activePath',activePath)
            this.activePath=activePath
        }
    }
}
</script>
<style lang="less" scoped>
.home-container{
    height: 100%;
}
.el-header{
    background-color: #373d41;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    color: #ffffff;
    font-size: 20px;
    > div {
        display: flex;
        align-items:center;
        span{
            margin-left:15px;
        }
    }
}
.el-aside{
    background-color: #333744;
    .el-menu{
        border-right: none;
    }
}
.el-main{
    background-color: #eaedf1;
}
.toggle-button{
    background-color: #4A5064;
    font-size: 10px;
    line-height: 24px;
    color: #ffffff;
    text-align: center;
    letter-spacing: 0.2em;
    cursor: pointer;
}
</style>