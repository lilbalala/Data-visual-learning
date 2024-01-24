var chartDom = document.getElementById('ra');
var myChartra = echarts.init(chartDom);
var option;

myChartra.setOption({
  title: {
    text: 'Basic Radar Chart',
    textStyle:{color:'#33CCFF'}
  },
  legend: {
    data: ['Allocated Budget', 'Actual Spending'],
    orient:'vertical',
    right:'0%',
    textStyle:{color:'#33CCFF'},
  },
  radar: {
//     shape: 'circle',
    indicator: [
      { name: 'Sales', max: 100 },
      { name: 'Administration', max: 100 },
      { name: 'Information Technology', max: 100 },
      { name: 'Customer Support', max: 100 },
      { name: 'Development', max: 100 },
      { name: 'Marketing', max: 100 }
    ],
    axisName: {
        formatter: '【{value}】',
        color: '#33CCFF'
      },
  },
  series: [
    {
      name: 'Budget vs spending',
      type: 'radar',
      data: [
        {
          value: [4200, 3000, 20000, 35000, 50000, 18000],
          name: 'Allocated Budget'
        },
        {
          value: [5000, 14000, 28000, 26000, 42000, 21000],
          name: 'Actual Spending'
        }
      ]
    }
  ]
});

myChartra.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartra.hideLoading();
myChartra.setOption(
(option={
        series:[{
            data:[
                {value:result.rddata[0],
                 name:'Allocated Budget'},
                {value:result.rddata[1],
                 name:'Actual Spending'}
            ]
        }]
       })
    )
   }
  });
};

$.get('/data').done(fetchData);

setInterval(fetchData, 5000);