var chartDom = document.getElementById('gender_c1');
var myChartstbar = echarts.init(chartDom);

myChartstbar.setOption ({
  title:{
    text:'不同性别对购买商品一级目录的数据差异',
    x:'center',
    textStyle:{color:'#33CCFF',}
  },
//  legend:{},
  tooltip:{},
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
    axisLabel:{color:"#33CCFF"},
    data: ['男','女']
  },
  yAxis: {
    type: 'value',
    axisLabel:{color:"#33CCFF"},
  },
  series: [
    {
      name:'28',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
    {
      name:'38',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
//      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
    {
      name:'50008168',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
//      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
    {
      name:'50014815',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
//      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
    {
      name:'50022520',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
//      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
    {
      name:'122650008',
      data: [],
      type: 'bar',
      stack:true,
      label:{show:false},
//      itemStyle:{color:"#CC0000"},
//      showBackground: true,
//      backgroundStyle: {
//        color: 'rgba(180, 180, 180, 0.6)'
//      }
    },
  ]
});


myChartstbar.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartstbar.hideLoading();
myChartstbar.setOption(
(option={
series:[{name:'28',
        data:result.gender_c1[0]},
        {name:'38',
        data:result.gender_c1[1]},
        {name:'50008168',
        data:result.gender_c1[2]},
        {name:'50014815',
        data:result.gender_c1[3]},
        {name:'50022520',
        data:result.gender_c1[4]},
        {name:'122650008',
        data:result.gender_c1[5]},
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);
