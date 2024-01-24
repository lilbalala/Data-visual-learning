var chartDom = document.getElementById('map');
var myChartmap = echarts.init(chartDom);

myChartmap.setOption({
    title: {
        text: 'China Map Exapmple',
        subtext: '',
        x: 'center',
        textStyle:{color:'#33CCFF'}
    },
//    tooltip: {
//        trigger: 'item'
//    },
    legend: {
        show: false,
        orient: 'horizontal',//图例的排列方向
        x: 'left',
        data: ['']
    },
    tooltip: {
        show: true,
        formatter: function (params) {
            if (params.value.length > 1) {
                return '&nbsp;&nbsp;' + params.name + '&nbsp;&nbsp;&nbsp;' + params.value[2] + '万人&nbsp;&nbsp;';
            } else {
                return '&nbsp;&nbsp;' + params.name + '&nbsp;&nbsp;&nbsp;' + params.value + '万人&nbsp;&nbsp;';
            }
        },

    },
    visualMap: {
        show: true,
        x: 'left',
        y: 'center',
        splitList: [
            { start: 8000, end: 12000 },
            { start: 5000, end: 8000 },
            { start: 4000, end: 5000 },
            { start: 3500, end: 4000 },
            { start: 2500, end: 3500 },
            { start: 800, end: 2500 },
            { start: 50, end: 800 },
        ],
        text: ['高', '低'],
        textStyle:{color:'#33CCFF'},
        color: ['#93CDE1', '#6EC2EE', '#2961AD']
    },
    toolbox: {
        show: false,
        orient: 'vertical',
        x: 'right',
        y: 'center',
        feature: {//各工具配置项。
            mark: { show: true },
            dataView: { show: true, readOnly: false },//数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新。
            restore: { show: true },//配置项还原。
            saveAsImage: { show: true }//保存为图片。
        }
    },
    roamController: {//控制地图的上下左右放大缩小 图上没有显示
        show: true,
        x: 'right',
        mapTypeControl: {
            'china': true
        }
    },
    series: [
        {
            name: '人口数量',
            type: 'map',
            mapType: 'china',
            roam: false,//是否开启鼠标缩放和平移漫游
            itemStyle: {//地图区域的多边形 图形样式
                normal: {//是图形在默认状态下的样式
                    label: {
                        show: true,//是否显示标签
                        textStyle: {
                            color: "rgb(249, 249, 249)"
                        }
                    }
                },
                emphasis: {//是图形在高亮状态下的样式,比如在鼠标悬浮或者图例联动高亮时
                    label: { show: true }
                }
            },
            top: "3%",//组件距离容器的距离
            data: [],
        }
    ]
});


myChartmap.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartmap.hideLoading();
myChartmap.setOption(
(option={
series:[{name:'人口数量',
        data:result.mapdata}
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);

setInterval(fetchData, 5000);

