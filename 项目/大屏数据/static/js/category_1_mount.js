var chartDom = document.getElementById('category_1_mount');
var myChartpie = echarts.init(chartDom);
var option;

myChartpie.setOption({
    title: {
        text: '商品一级类目的销量情况',
        subtext: '',
        x: 'center',
        textStyle:{color:'#33CCFF'}
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
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

    series: [
        {
            name: 'one',
            type: 'pie',
            radius: [60, 90],
//            center: ['15%', '25%'],
            roseType: 'area',
            label:{show:true,textStyle:{color:'#33CCFF'}},
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
    ]
});


myChartpie.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartpie.hideLoading();
myChartpie.setOption(
(option={
series:[
        {
            name:'one',
            data:result.category_1_mount
        },
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);
