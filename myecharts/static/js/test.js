var chartDom = document.getElementById('zhu');
var myChart = echarts.init(chartDom);

myChart.setOption ({
  xAxis: {
    type: 'category',
    axisLabel:{color:"#33CCFF"},
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value',
    axisLabel:{color:"#33CCFF"},
  },
  series: [
    {
      name:'测试系列',
      data: [],
      type: 'bar',
      itemStyle:{color:"#CC0000"},
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.6)'
      }
    }
  ]
});
var update_mychart=function(data){
myChart.hideLoading();
myChart.setOption({series:[{name:'测试系列',data:data.zhudata}]});
};
myChart.showLoading();
$.get('/data').done(update_mychart);
var timeTicket=setInterval(function(){
$.get('/data').done(update_mychart);
},5000);

//option && myChart.setOption(option);
//window.addEventListener("resize",function(){myChart.resize()});