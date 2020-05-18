<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>客户满意</el-breadcrumb-item>
            <el-breadcrumb-item>不满意客户</el-breadcrumb-item>
          </el-breadcrumb>
          <el-card>
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
            <!-- <div id="main" style="width: 600px;height:400px;"></div> -->
            <el-row :gutter="20">
                <el-col :span="12">
                    <div id="main" ref="main" style="width: 100%;height:400px;"></div>
                </el-col>
                <el-col :span="12">
                    <div id="main2" ref="main2" style="width: 100%;height:400px;"></div>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                    <div id="main3" ref="main3" style="width: 100%;height:400px;"></div>
                </el-col>
                <el-col :span="12">
                    <div id="main4" ref="main4" style="width: 100%;height:400px;"></div>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                    <el-row>
                        <div id="id_test1" ref="id_test1" class="grid-content bg-purple"  style="width: 100%;height:400px;"></div>
                    </el-row>
                </el-col>
                <el-col :span="12">
                  <div id="id_test2" ref="id_test2" class="grid-content bg-purple" style="width: 100%;height:200px;"></div>
                  <div id="id_test3" ref="id_test3" class="grid-content bg-purple" style="width: 100%;height:200px;"></div>
                </el-col>
              </el-row>
        </el-card>
    </div>

</template>



<script>
    import {optionTest,optionMap,optionBar_newtv_user,option_bar_tv_user,
      option_pie_watching_time,option_pie_family_num,option_pie_family_stb_num,option_bar_bottom_left,
      option_bar_bottom_mid,option_bar_bottom_right} from  '../../assets/js/deyang_tvb.js'
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
            this.initChart("id_test2",optionTest)
            this.initChart("id_test3",optionTest)
            this.initChart("bar_tv_user_new",optionBar_newtv_user)
            this.initChart("bar_tv_user",option_bar_tv_user)
            this.initChart("pie_watching_time",option_pie_watching_time)
            this.initChart("pie_family_num",option_pie_family_num)
            this.initChart("pie_family_stb_num",option_pie_family_stb_num)

            option_bar_bottom_left.series[0].itemStyle.normal.color=
            new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
              offset: 0,
              color: 'rgba(0,255,0)'
          }, {
              offset: 1,
              color: 'rgb(215 ,255,0)'
          }])
          this.initChart("bar_bottom_left",option_bar_bottom_left)

          option_bar_bottom_mid.series[0].itemStyle.normal.color=
          new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
            offset: 0,
            color: 'rgb(126, 177, 8)'
        }, {
            offset: 1,
            color: 'rgb(8, 177, 45)'
        }])
        this.initChart("bar_bottom_mid",option_bar_bottom_mid)
        
        option_bar_bottom_right.series[0].itemStyle.normal.color=
        new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
          offset: 0,
          color: 'rgba(0,255,0)'
      }, {
          offset: 1,
          color: 'rgb(215 ,255,0)'
      }])
      this.initChart("bar_bottom_right",option_bar_bottom_right)
      this.init()

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
                //setTimeout(function (){
                 //   window.onresize = function () {
                 //       myChart.resize();
                 //   }
                //},200);
            },
            init() {
              const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
              setTimeout(() => {
                window.onresize = function() {
                    self.main = echarts.init(self.$refs.main);
                    self.main.resize();
                    self.main2 = echarts.init(self.$refs.main2);
                    self.main2.resize();
                    self.main3 = echarts.init(self.$refs.main3);
                    self.main3.resize();
                    self.main4 = echarts.init(self.$refs.main4);
                    self.main4.resize();
                    self.id_test1 = echarts.init(self.$refs.id_test1);
                    self.id_test1.resize();
                    self.id_test2 = echarts.init(self.$refs.id_test2);
                    self.id_test2.resize();
                    self.id_test3 = echarts.init(self.$refs.id_test3);
                    self.id_test3.resize();
                }
              },20)
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