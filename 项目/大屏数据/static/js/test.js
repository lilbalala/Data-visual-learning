var chartDom = document.getElementById('bar');
var myChartbar = echarts.init(chartDom);

myChartbar.setOption ({
  title:{
    text:'一级类目下二级类目数量',
    x:'center',
    textStyle:{color:'#33CCFF',}
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
    axisLabel:{color:"#33CCFF",rotate:45},
    data: []
  },
  yAxis: {
    type: 'value',
    axisLabel:{color:"#33CCFF"},
  },
  series: [
    {
      name:'一级类目下二级类目数量',
      data: [],
      type: 'bar',
      label:{show:true,position:'top'},
      itemStyle:{color:"#CC0000"},
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.6)'
      }
    }
  ]
});

myChartbar.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartbar.hideLoading();
myChartbar.setOption(
(option={xAxis:{data:result.category[0]},
series:[{name:'一级类目下二级类目数量',
        data:result.category[1]}
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);
