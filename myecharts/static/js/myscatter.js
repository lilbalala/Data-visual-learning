var chartDom = document.getElementById('st');
var myChartst = echarts.init(chartDom);
var option;

myChartst.setOption ( {
  title: {
    text: 'Life Expectancy and GDP by Country',
    left: '5%',
    top: '3%',
    textStyle:{color:'#33CCFF'}
  },
  legend: {
    right: '10%',
    top: '3%',
    textStyle:{color:'#33CCFF'}
  },
  grid: {
    left: '8%',
    top: '10%'
  },
  xAxis: {
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    },
    axisLabel:{color:'#33CCFF'}
  },
  yAxis: {
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    },
    scale: true,
    axisLabel:{color:'#33CCFF'}
  }
});

myChartst.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartst.hideLoading();
myChartst.setOption(
(option={
        series: [
    {
      name: result.stdata[0],
      data: result.stdata[2][0],
      type: 'scatter',
      symbolSize: function (data) {
        return Math.sqrt(data[2]) / 5e1;
      },
      emphasis: {
        focus: 'series',
        label: {
          show: true,
          formatter: function (param) {
            return param.data[3];
          },
          color:'#33CCFF',
          position: 'top'
        }
      },
      itemStyle: {
        shadowBlur: 10,
        shadowColor: 'rgba(120, 36, 50, 0.5)',
        shadowOffsetY: 5,
        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
          {
            offset: 0,
            color: 'rgb(251, 118, 123)'
          },
          {
            offset: 1,
            color: 'rgb(204, 46, 72)'
          }
        ])
      }
    },
    {
      name: result.stdata[1],
      data: result.stdata[2][1],
      type: 'scatter',
      symbolSize: function (data) {
        return Math.sqrt(data[2]) / 5e1;
      },
      emphasis: {
        focus: 'series',
        label: {
          show: true,
          formatter: function (param) {
            return param.data[3];
          },
          color:'#33CCFF',
          position: 'top'
        }
      },
      itemStyle: {
        shadowBlur: 100,
        shadowColor: 'rgba(25, 100 , 150, 1)',
        shadowOffsetY: 5,
        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
          {
            offset: 0,
            color: 'rgb(129, 227, 238)'
          },
          {
            offset: 1,
            color: 'rgb(25, 183, 207)'
          }
        ])
      }
    }
  ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);

setInterval(fetchData, 5000);