var chartDom = document.getElementById('t_y_m_mount');
var myChartline = echarts.init(chartDom);
var option;

myChartline.setOption({
    title: {
        text: '年月销量趋势图',
        subtext: '',
        x: 'center',
        textStyle:{color:'#33CCFF'}
    },
//    tooltip: {
//        trigger: 'item',
//        formatter: '{a} <br/>{b} : {c} ({d}%)'
//    },
    legend: {
        show: false,
        orient: 'horizontal',//图例的排列方向
//        x: 'left',
    },
    tooltip: {
        show: true,
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
//      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  xAxis: {
    type: 'category',
    data: [],
    axisLabel:{color:'#33CCFF'}
  },
  yAxis: {
    type: 'value',
    axisLabel:{color:'#33CCFF'}
  },
    series:{
       name:'ym',
       type:'line',
       smooth:true,
       data:[],
       label:{show:true,textStyle:{color:'#33CCFF'}}
  }
 });

myChartline.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartline.hideLoading();
myChartline.setOption(
(option={
xAxis:{data:result.t_y_m_mount[0]},
series:[
        {name:'ym',data:result.t_y_m_mount[1]}
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);