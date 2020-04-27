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
                        <div id="id_test1" class="grid-content bg-purple"></div>
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
              <el-row>
                <div class="body_in">
                    <div class="top">德阳电视包可视化-Echarts</div>
                    <div class="middle">
                        <div class="middle_left">
                            <div class="middle_left_top">
                                <div id = "bar_tv_user" style="height: 100%;widht:100%;"></div>
                                <div class="middle_left_top_footer"></div>
                            </div>
                            <div class="middle_left_mid">
                                <div id = "bar_tv_user_new" style="height: 100%;widht:100%;"></div>
                                <div class="middle_left_top_footer"></div>
                            </div>
                            <div class="middle_left_bottom">
                                <div class="middle_left_bottom_left">
                                    <div id = "pie_watching_time" style="height: 100%;widht:100%;"></div>
                                    <div class="middle_right_right_footer"></div>
                                </div>
                                <div class="middle_left_bottom_mid">
                                    <div id = "pie_family_num" style="height: 100%;widht:100%;"></div>
                                    <div class="middle_right_right_footer"></div>
                                </div>
                                <div class="middle_left_bottom_right">
                                    <div id = "pie_family_stb_num" style="height: 100%;widht:100%;"></div>
                                    <div class="middle_right_right_footer"></div>
                                </div>
                            </div>
                        </div>
                        <div class="middle_right">
                            <div class="middle_right_left">
                                <h5>区县&nbsp;&nbsp;活跃家庭数</h5>
                                <h6>&nbsp;罗江&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19760</h6>
                                <h6>&nbsp;中江&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;78183</h6>
                                <h6>&nbsp;广汉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;53822</h6>
                                <h6>&nbsp;什邡&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;43328</h6>
                                <h6>&nbsp;旌阳&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;70746</h6>
                                <h6>&nbsp;绵竹&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;51691</h6>
                            </div>
                            <div  class="middle_right_right">
                                <div id = "geo_deyang" style="height: 100%;widht:100%;"></div>
                                <div class="middle_right_right_footer"></div>
                            </div>
                        </div>
                    </div>
                    <div class="bottom">
                        <div class="bottom_left">
                            <div id = "bar_bottom_left" style="height: 100%;widht:100%;"></div>
                            <div class="middle_right_right_footer"></div>
                        </div>
                        <div class="bottom_mid">
                            <div id = "bar_bottom_mid" style="height: 100%;widht:100%;"></div>
                            <div class="middle_right_right_footer"></div>
                        </div>
                        <div class="bottom_right">
                            <div id = "bar_bottom_right" style="height: 100%;widht:100%;"></div>
                            <div class="middle_right_right_footer"></div>
                        </div>
                    </div>
                </div>
              </el-row>
        </el-card>
    </div>

</template>



<script>
    import {optionTest,optionMap} from  '../../assets/js/deyang_tvb.js'
    import '../../assets/js/deyang.js'
    let echarts = require('echarts/lib/echarts')
    export default {
        data(){
            return {
                userlist:[],
                total:0
            }
        },
        created(){
            this.getUserList()
            console.log(optionTest)
            console.log(optionMap)
        },
        //此时，页面上的元素，已经被渲染完毕了
        mounted(){
            this.initChart("main",optionTest)
            this.initChart("main2",optionTest)
            this.initChart("main3",optionTest)
            this.initChart("main4",optionTest)
            this.initChart("geo_deyang",optionMap)
            this.initChart("id_test1",optionTest)
            
        },
        methods:{
            async getUserList(){
                const {data:res} = await this.$http.get('student_list');
                console.log(res)
                this.userlist = res
                this.total = res.length
                console.log(this.total)
            },
            initChart(container,option){
                var myChart = echarts.init(document.getElementById(container));
                myChart.setOption(option);
                //1.自适应方法1
                // window.addEventListener('resize', () => {
                // // 自动渲染echarts
                //     myChart.resize();
                // })
                //2.自适应方法2
                setTimeout(function (){
                    window.onresize = function () {
                        myChart.resize();
                    }
                },200);
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