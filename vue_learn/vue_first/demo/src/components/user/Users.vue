<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>客户满意</el-breadcrumb-item>
            <el-breadcrumb-item>不满意客户</el-breadcrumb-item>
          </el-breadcrumb>
          <el-card>
            <!-- <div id="main" style="width: 600px;height:400px;"></div> -->
            <el-row :gutter="20">
                <el-col :span="11">
                    <div id="main" style="width: 600px;height:400px;"></div>
                </el-col>
                <el-col :span="11">
                    <div id="main2" style="width: 600px;height:400px;"></div>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="11">
                    <div id="main3" style="width: 600px;height:400px;"></div>
                </el-col>
                <el-col :span="11">
                    <div id="main4" style="width: 600px;height:400px;"></div>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="6">
                    <el-row>
                        <div class="grid-content bg-purple"></div>
                    </el-row>
                    <el-row type="flex"  justify="center">
                        <div class="grid-content bg-purple"></div>
                    </el-row>
                </el-col>
                <el-col :span="6" :offset="6"><div class="grid-content bg-purple"></div></el-col>
              </el-row>
              <el-row :gutter="20" type="flex"  justify="center">
                <el-col :span="12" :offset="6">
                    <el-row>
                    <div class="grid-content bg-purple"></div>
                    </el-row>
                    <el-row>
                        <div class="grid-content bg-purple"></div>
                        </el-row>
                </el-col>
              </el-row>
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
            var myChart2 = echarts.init(document.getElementById('main2'));
            
            var myChart3 = echarts.init(document.getElementById('main3'));
            
            var myChart4 = echarts.init(document.getElementById('main4'));
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
            
            myChart2.setOption(option);
            myChart3.setOption(option);
            myChart4.setOption(option);
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

.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>