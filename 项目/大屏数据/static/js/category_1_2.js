var chartDom = document.getElementById('category_1_2');
var myChartmpie = echarts.init(chartDom);

myChartmpie.setOption({
    title: [{
        text: '每个一级类目下销量最好的二级类目',
        subtext: '',
        x: 'center',
        textStyle:{color:'#33CCFF'}
    },
    {
        text: '28',
        textStyle:{color:'#33CCFF'},
        left:'13%',
        top:'22%'
    },
    {
        text: '38',
        textStyle:{color:'#33CCFF'},
        left:'48%',
        top:'22%'
    },
    {
        text: '50008168',
        textStyle:{color:'#33CCFF'},
        left:'78%',
        top:'22%'
    },
    {
        text: '50014815',
        textStyle:{color:'#33CCFF'},
        left:'9%',
        top:'73%'
    },
    {
        text: '50022520',
        textStyle:{color:'#33CCFF'},
        left:'43.5%',
        top:'73%'
    },
    {
        text: '122650008',
        textStyle:{color:'#33CCFF'},
        left:'77.5%',
        top:'73%'
    },
    ],
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
            name: '28',
            type: 'pie',
            radius: [60, 90],
            center: ['15%', '25%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
        {
            name: '38',
            type: 'pie',
            radius: [60, 90],
            center: ['50%', '25%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
        {
            name: '50008168',
            type: 'pie',
            radius: [60, 90],
            center: ['85%', '25%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
        {
            name: '50014815',
            type: 'pie',
            radius: [60, 90],
            center: ['15%', '75%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
        {
            name: '50022520',
            type: 'pie',
            radius: [60, 90],
            center: ['50%', '75%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
        {
            name: '122650008',
            type: 'pie',
            radius: [60, 90],
            center: ['85%', '75%'],
            roseType: 'area',
            label:'center',
            itemStyle: {
                 borderRadius: 5
            },
            data: [],
        },
    ]
});


myChartmpie.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartmpie.hideLoading();
myChartmpie.setOption(
(option={
series:[
        {
            name:'28',
            data:result.category_1_2[0]
        },
        {
            name:'38',
            data:result.category_1_2[1]
        },
        {
            name:'50008168',
            data:result.category_1_2[2]
        },
        {
            name:'50014815',
            data:result.category_1_2[3]
        },
        {
            name:'50022520',
            data:result.category_1_2[4]
        },
        {
            name:'122650008',
            data:result.category_1_2[5]
        },
        ]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);

//setInterval(fetchData, 5000);


