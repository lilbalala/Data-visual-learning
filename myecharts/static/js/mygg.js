var chartDom = document.getElementById('gge');
var myChartgauge = echarts.init(chartDom);
var option;

myChartgauge.setOption({
  series: [
    {
      type: 'gauge',
      axisLine: {
        lineStyle: {
          width: 30,
          color: [
            [0.3, '#67e0e3'],
            [0.7, '#37a2da'],
            [1, '#fd666d']
          ]
        }
      },
      pointer: {
        itemStyle: {
          color: 'inherit'
        }
      },
      axisTick: {
        distance: -30,
        length: 8,
        lineStyle: {
          color: '#fff',
          width: 2
        }
      },
      splitLine: {
        distance: -30,
        length: 30,
        lineStyle: {
          color: '#fff',
          width: 4
        }
      },
      axisLabel: {
        color: 'inherit',
        distance: 40,
        fontSize: 20
      },
      detail: {
        valueAnimation: true,
        formatter: '{value} km/h',
        color: 'inherit'
      },
      data: [
        {
          value: [70]
        }
      ]
    }
  ]
});


myChartgauge.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartgauge.hideLoading();
myChartgauge.setOption(
{
series:[
        {
        data:[
        {
        value:result.gaugedata
        }
       ]
      }
      ]
     }
    )
   }
  });
};

$.get('/data').done(fetchData);

setInterval(fetchData, 5000);