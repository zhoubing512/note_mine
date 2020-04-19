//柱状图1
(function(){
    var myChart = echarts.init(document.getElementById('geo_deyang'));


var mydata = [  
    {name: '旌阳区',value: '70746' },{name: '中江县',value: '78182' },  
    {name: '罗江县',value: '19760' },{name: '绵竹市',value: '51691' },  
    {name: '什邡市',value: '43328' },{name: '广汉市',value: '53822' }];
var optionMap = {  
    //backgroundColor: '#FFFFFF',  
    title: {  
        text: '德阳电视客户区县分布',  
        subtext: '',  
        x:'center', 
        textStyle:{
            color: '#FFFFFF'
        }
    },  
    tooltip : {  
        trigger: 'item'  
    },  
    
    //左侧小导航图标  
    visualMap: {
        min: 0,
        max: 80000,
        text: ['高', '低'], // 文本，默认为数值文本
        calculable: true,
        inRange:{
           color: ['#edfbfb','lightskyblue', '#215096']
        },
        textStyle: {
            color: '#ffffff'
        },
        bottom: "0",
        left: "5%",
    },
    //配置属性
    series: [{  
        name: '数据',  
        type: 'map',  
        mapType: 'deyang',   
        roam: true,  
        label: {  
            normal: {  
                show: true  //省份名称  
            },  
            emphasis: {  
                show: false  
            }  
        },  
        data:mydata  //数据
    }]  
};  
//使用制定的配置项和数据显示图表
myChart.setOption(optionMap);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    date_data = [

    ]
    var option = {
        title: {  
            text: '电视包新增客户',  
            subtext: '',  
            x:'center', 
            textStyle:{
                color: '#FFFFFF'
            }
        }, 
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            orient: 'vertical',
            color: ["#1651aa", "#bba00a", "#7a86a1", "#9da007", "#5607a0", "#07a065"],
            data: ['广汉', '旌阳', '罗江','绵竹','什邡','中江'],
            right: '3%',
            y: 'center',
            textStyle:{
                fontSize: 15,//字体大小
                color: '#ffffff'//字体颜色
            },
        },
        grid: {
            top: '5%',
            left: '5%',
            right: '15%',
            bottom: '10%',
            height: '80%',
            containLabel: false
        },
        xAxis: {
            type: 'category',
            data: ['3.22','3.23','3.24','3.25','3.26','3.27','3.28','3.29','3.30','3.31'],
            axisLine: {
                lineStyle: {
                    color: "#999"
                }
            },
            axisTick:{ //轴刻度线
                show:false
                },
        },
        yAxis: {
            
            name:"ddddd",
            type: 'value',
    
            splitLine: {
                show:false,
                lineStyle: {
                    type: 'dashed',
                    color: '#DDD'
                }
            },
            axisLine: {
                show: false,
                lineStyle: {
                    color: "#FFFFFF"
                },
            },
            axisTick:{ //轴刻度线
                show:false
                },
            nameTextStyle: {
                color: "#FFFFFF"
            },
            splitArea: {
                show: false
            }
        },
        series: [{
                name: '广汉',
                type: 'line',
                data: [30,35,33,35,26,26,36,27,23,24],
                color: "#1651aa",
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#1651aa',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#1651aa"
                    }
                },
            },
            {
                name: '旌阳',
                type: 'line',
                data: [38,35,32,33,30,24,35,29,39,27],
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#bba00a',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#bba00a"
                    }
                },
            },
            {
                name: '罗江',
                type: 'line',
                data: [17,14,15,7,9,12,12,8,32,17],
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#7a86a1',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#7a86a1"
                    }
                },
            },
            {
                name: '绵竹',
                type: 'line',
                data: [25,22,29,31,31,18,21,22,23,31],
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#9da007',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#9da007"
                    }
                },
            },
            {
                name: '什邡',
                type: 'line',
                data: [28,24,18,28,31,15,31,19,20,18],
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#5607a0',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#5607a0"
                    }
                },
            },
            {
                name: '中江',
                type: 'line',
                data: [81,67,64,63,45,35,65,54,44,38],
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#07a065',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#07a065"
                    }
                },
            }
        ]
    };
//初始化
    var myChart = echarts.init(document.getElementById('bar_tv_user_new'));
    //使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    date_data = [

    ]
    var option = {
        title: {  
            text: '电视包活跃客户',  
            subtext: '',  
            x:'center', 
            textStyle:{
                color: '#FFFFFF'
            }
        }, 
        tooltip: {
            trigger: 'axis'
        },
        grid: {
            top: '25%',
            left: '5%',
            right: '5%',
            bottom: '10%',
            height: '57%',
            containLabel: false
        },
        xAxis: {
            type: 'category',
            data: ['3.7','3.8','3.29','3.9','3.11','3.12','3.13','3.14','3.15','3.16','3.17','3.18','3.19','3.20','3.21','3.22','3.23','3.24','3.25','3.26','3.27','3.28','3.29','3.30','3.31'],
            axisLine: {
                lineStyle: {
                    color: "#999"
                }
            },
            axisTick:{ //轴刻度线
                show:false
                },
        },
        yAxis: {
            max:28,
            min:23,
            name:"单位：万",
            type: 'value',
    
            splitLine: {
                show:false,
                lineStyle: {
                    type: 'dashed',
                    color: '#DDD'
                }
            },
            axisLine: {
                show: false,
                lineStyle: {
                    color: "#FFFFFF"
                },
            },
            axisTick:{ //轴刻度线
                show:false
                },
            nameTextStyle: {
                color: "#FFFFFF"
            },
            splitArea: {
                show: false
            }
        },
        series: [{
                name: '',
                type: 'line',
                data: [26.0338,26.3591,27.1261,26.5887,26.4019,26.2292,26.3149,25.4306,25.4344,26.374,25.8778,25.6838,25.7126,25.8118,25.1558,25.1381,25.5065,25.4212,25.1658,25.3167,25.2022,25.1557,24.4582,25.383,24.9165],
                color: "#bba00a",
                lineStyle: {
                    normal: {
                        width: 3,
                        
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#bba00a',
                        borderWidth: 5,
                        /*shadowColor: 'rgba(72,216,191, 0.3)',
                         shadowBlur: 100,*/
                        borderColor: "#bba00a"
                    }
                },
            }
        ]
    };
//初始化
    var myChart = echarts.init(document.getElementById('bar_tv_user'));
    //使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    const colorList = ['#47A2FF ', '#53C8D1', '#59CB74', '#FBD444', '#7F6AAD', '#585247',"#1651aa"]

    var option = {
        title: {
            text: '观\n \n看\n \n时\n \n长\n \n',
            // subtext: '(单位：小时)',
            textStyle: {
                fontSize: 16,
                color: '#fff',
                lineHeight: 20
            },
            // subtextStyle: {
            //     fontSize: 2,
            //     color: '#fff'
            // },
            textAlign: 'center',
            left: '10%',
            top: '10%'
        },
        tooltip: {
            trigger: 'item',
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: '0',
            y: 'center',
            itemGap: 8,
            selectedMode: false,
            icon: 'pin',
            data: ['0-1', '1-3', '3-5', '5-10', '10-15','15-24'],
            textStyle: {
                color: '#fff',
                rich: {
                    uname: {
                        width: 35
                    },
                    unum: {
                        color: '#4ed139',
                        width: 1,
                        align: 'right'
                    }
                }
            },
            formatter(name,value) {
                return `{uname|${name}}`
            }
        },
        color: colorList,
        series: [
            {
                name: '观看时长人数',
                type: 'pie',
                radius: ['40%', '70%'],
                center: ['45%', '50%'],
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                itemStyle: {
                    borderWidth: 2,
                    borderColor: '#fff'
                },
                data: [
                    {name: '0-1', value: 78341},
                    {name: '1-3', value: 94831},
                    {name: '3-5', value: 46179},
                    {name: '5-10', value: 43320},
                    {name: '10-15', value: 14341},
                    {name: '15-24', value: 30292},
                ],
            }
        ]
    };
    //初始化
    var myChart = echarts.init(document.getElementById('pie_watching_time'));
    //使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    const colorList = ['#47A2FF ', '#53C8D1', '#59CB74', '#FBD444', '#7F6AAD', '#585247',"#1651aa"]

    var option = {
        title: {
            text: '家\n \n庭\n \n成\n \n员\n \n',
            // subtext: '(单位：小时)',
            textStyle: {
                fontSize: 16,
                color: '#fff',
                lineHeight: 20
            },
            // subtextStyle: {
            //     fontSize: 2,
            //     color: '#fff'
            // },
            textAlign: 'center',
            left: '10%',
            top: '10%'
        },
        tooltip: {
            trigger: 'item',
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: '0',
            y: 'center',
            itemGap: 8,
            selectedMode: false,
            icon: 'pin',
            data: ["1人", '2人', '3人', '4人', '5人','6人'],
            textStyle: {
                color: '#fff',
                rich: {
                    uname: {
                        width: 35
                    },
                    unum: {
                        color: '#4ed139',
                        width: 1,
                        align: 'right'
                    }
                }
            },
            formatter(name,value) {
                return `{uname|${name}}`
            }
        },
        color: colorList,
        series: [
            {
                name: '家庭成员数',
                type: 'pie',
                center: ['45%', '50%'],
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                itemStyle: {
                    borderWidth: 2,
                    borderColor: '#fff'
                },
                data: [
                    {name: '1人', value: 200534},
                    {name: '2人', value: 113165},
                    {name: '3人', value: 239510},
                    {name: '4人', value: 47587},
                    {name: '5人', value: 5681},
                    {name: '6人', value: 758},
                ],
            }
        ]
    };
    //初始化
    var myChart = echarts.init(document.getElementById('pie_family_num'));
    //使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    const colorList = ['#47A2FF ', '#53C8D1', '#59CB74', '#FBD444', '#7F6AAD', '#585247',"#1651aa"]

    var option = {
        title: {
            text: '家\n \n庭\n \n机\n \n顶\n \n盒',
            // subtext: '(单位：小时)',
            textStyle: {
                fontSize: 16,
                color: '#fff',
                lineHeight: 20
            },
            // subtextStyle: {
            //     fontSize: 2,
            //     color: '#fff'
            // },
            textAlign: 'center',
            left: '10%',
            top: '0%'
        },
        tooltip: {
            trigger: 'item',
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: '0',
            y: 'center',
            itemGap: 8,
            selectedMode: false,
            icon: 'pin',
            data: ['0个', '1个', '2个', '3个'],
            textStyle: {
                color: '#77899c',
                rich: {
                    uname: {
                        width: 35
                    },
                    unum: {
                        color: '#4ed139',
                        width: 1,
                        align: 'right'
                    }
                }
            },
            formatter(name,value) {
                return `{uname|${name}}`
            }
        },
        color: colorList,
        series: [
            {
                name: '家庭机顶盒数',
                type: 'pie',
                radius: ['40%', '70%'],
                center: ['45%', '50%'],
                label: {
                    show: false
                },
                labelLine: {
                    show: false
                },
                itemStyle: {
                    borderWidth: 2,
                    borderColor: '#fff'
                },
                data: [
                    {name: '0个', value: 70635},
                    {name: '1个', value: 529053},
                    {name: '2个', value: 5879},
                    {name: '3个', value: 114},
                ],
            }
        ]
    };
    //初始化
    var myChart = echarts.init(document.getElementById('pie_family_stb_num'));
    //使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
    window.onresize = function () {
        myChart.resize();
    }
},200);
})();

(function(){
    var data = [1619, 913, 810, 744, 653, 637, 470, 373, 340, 248];
    var titlename = ['黄金会员月包（合约版）', '酷喵影视', 'VIP黄金会员', '奇异果TV', '云视听TV', '体育生活频道包', '影视少儿频道包', 'VIP少儿包', 'VIP影视包', 'NewTV专区单月包'];
    var myColor = ['#1089E7', '#F57474', '#56D0E3', '#1089E7', '#F57474', '#56D0E3', '#F8B448', '#8B78F6', '#F8B448', '#8B78F6'];
    option = {
        
        title: {
            text: '热门电视包',
            // x: 'left',
            textStyle: {
                fontSize:15,
                color: '#fff'
            },
            textAlign:'center',
            left: '50%',
            // top: '10%'
        },
        //图标位置
        grid: {
            top: '15%',
            left: '35%',
            bottom:"1%",
            right:'0%'
    
        },
        xAxis: {
            show: false,
        },
        yAxis: [{
            show: true,
            data: titlename,
            inverse: true,
            axisLine: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },

            axisLine: {
                show: false,
                lineStyle: {
                    color: "#FFFFFF"
                },
            },
        }],
        series: [{
                name: '条',
                type: 'bar',
                yAxisIndex: 0,
                data: data,
                barWidth: 10,
                label: {
                    normal: {
                        show: false,
                        position: 'right',
                        textStyle: {
                            color: '#333',
                            fontSize: '16',
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        barBorderRadius: 20,
                        // color:'#1089E7',
                        // color: function(params) {
                        //     var num = myColor.length;
                        //     return myColor[params.dataIndex % num]
                        // },
                        // 渐变色
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: 'rgba(0,255,0)'
                        }, {
                            offset: 1,
                            color: 'rgb(215 ,255,0)'
                        }]),
                        
                    }
                },
    
            },
        ]
    };

//初始化
var myChart = echarts.init(document.getElementById('bar_bottom_left'));
//使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
window.onresize = function () {
    myChart.resize();
}
},200);
})();

(function(){
    var data = [101565.5, 90331.53, 84355.62, 67667.98, 63608.61, 59022.68, 54876.12, 47373.32, 35152.98, 33057.68];
    var titlename = ['CCTV-1', '四川影视文艺-高清', 'CCTV-6', 'CCTV-13', 'CCTV-8', 'CCTV-3', '四川经济', 'CCTV-4', '湖南卫视', '四川公共'];
    var myColor = ['#1089E7', '#F57474', '#56D0E3', '#1089E7', '#F57474', '#56D0E3', '#F8B448', '#8B78F6', '#F8B448', '#8B78F6'];
    option = {
        
        title: {
            text: '热门频道',
            // x: 'left',
            textStyle: {
                fontSize:15,
                color: '#fff'
            },
            textAlign:'center',
            left: '50%',
            // top: '10%'
        },
        //图标位置
        grid: {
            top: '15%',
            left: '35%',
            bottom:"1%",
            right:'0%'
    
        },
        xAxis: {
            show: false,
        },
        yAxis: [{
            show: true,
            data: titlename,
            inverse: true,
            axisLine: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },

            axisLine: {
                show: false,
                lineStyle: {
                    color: "#FFFFFF"
                },
            },
        }],
        series: [{
                name: '条',
                type: 'bar',
                yAxisIndex: 0,
                data: data,
                barWidth: 10,
                label: {
                    normal: {
                        show: false,
                        position: 'right',
                        textStyle: {
                            color: '#333',
                            fontSize: '16',
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        barBorderRadius: 20,
                        // color:'#F8B448',
                        // color: function(params) {
                        //     var num = myColor.length;
                        //     return myColor[params.dataIndex % num]
                        // },
                        // 渐变色
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: 'rgb(126, 177, 8)'
                        }, {
                            offset: 1,
                            color: 'rgb(8, 177, 45)'
                        }]),
                        
                    }
                },
    
            },
        ]
    };

//初始化
var myChart = echarts.init(document.getElementById('bar_bottom_mid'));
//使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
window.onresize = function () {
    myChart.resize();
}
},200);
})();


(function(){
    var data = [14463.94,7606.5,5416.69,5270.42,5168.04,4758.86,3902.51,3544.89,3519.52,3063.31];
    var titlename = ['庆余年','小马宝莉','小马宝莉友谊的魔力 合集','三生三世枕上书','汪汪队立大功','哪吒之魔童降世','海绵宝宝合集','一剑横空','海绵宝宝（01-104）'];
    var myColor = ['#1089E7', '#F57474', '#56D0E3', '#1089E7', '#F57474', '#56D0E3', '#F8B448', '#8B78F6', '#F8B448', '#8B78F6'];
    option = {
        
        title: {
            text: '热门影视',
            // x: 'left',
            textStyle: {
                fontSize:15,
                color: '#fff'
            },
            textAlign:'center',
            left: '50%',
            // top: '10%'
        },
        //图标位置
        grid: {
            top: '15%',
            left: '35%',
            bottom:"1%",
            right:'0%'
    
        },
        xAxis: {
            show: false,
        },
        yAxis: [{
            show: true,
            data: titlename,
            inverse: true,
            axisLine: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },

            axisLine: {
                show: false,
                lineStyle: {
                    color: "#FFFFFF"
                },
            },
        }],
        series: [{
                name: '条',
                type: 'bar',
                yAxisIndex: 0,
                data: data,
                barWidth: 10,
                label: {
                    normal: {
                        show: false,
                        position: 'right',
                        textStyle: {
                            color: '#333',
                            fontSize: '16',
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        barBorderRadius: 20,
                        // color:'#1089E7',
                        // color: function(params) {
                        //     var num = myColor.length;
                        //     return myColor[params.dataIndex % num]
                        // },
                        // 渐变色
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: 'rgba(0,255,0)'
                        }, {
                            offset: 1,
                            color: 'rgb(215 ,255,0)'
                        }]),
                        
                    }
                },
    
            },
        ]
    };

//初始化
var myChart = echarts.init(document.getElementById('bar_bottom_right'));
//使用制定的配置项和数据显示图表
myChart.setOption(option);
setTimeout(function (){
window.onresize = function () {
    myChart.resize();
}
},200);
})();


