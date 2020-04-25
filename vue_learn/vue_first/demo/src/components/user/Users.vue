<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>客户满意</el-breadcrumb-item>
            <el-breadcrumb-item>不满意客户</el-breadcrumb-item>
          </el-breadcrumb>
          <el-card>
            <div id="main" style="width: 600px;height:400px;"></div>
        </el-card>
    </div>

</template>



<script>
    //const echarts = require('echarts');
    export default {
        data(){
            return {
                userlist:[],
                total:0
            }
        },
        created(){
            this.getUserList()
        },
        //此时，页面上的元素，已经被渲染完毕了
        mounted(){
            var myChart = echarts.init(document.getElementById('main'));
            //准备数据和配置项
            var option = {
                title: {
                    text: 'ECharts 入门示例'
                },
                tooltip: {},
                legend: {
                    data:['销量']
                },
                xAxis: {
                    data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                },
                yAxis: {},
                series: [{
                    name: '销量',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20]
                }]
            };
            myChart.setOption(option);
        },
        methods:{
            async getUserList(){
                const {data:res} = await this.$http.get('student_list');
                console.log(res)
                this.userlist = res
                this.total = res.length
                console.log(this.total)
            }
        }
    }
</script>

<style lang="less" scoped>
@import '../../assets/css/deyang_tvb.less';
</style>