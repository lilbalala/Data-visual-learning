var chartDom = document.getElementById('cy');
var myChartwdcd = echarts.init(chartDom);

myChartwdcd.setOption ({
  title:{
    text:'WordCloud Example',
    textStyle:{color:'#33CCFF'}
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
   },
  series: [
    {
      type: 'wordCloud',
      sizeRange: [6, 48],
      textStyle: {
                color: function () {
                     return 'rgb(' +
                            [
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160),
                            ].join(',') +')'
                    }
            },
      emphasis: {
        shadowBlur: 10,
        shadowColor: '#333'
        },
      data: []
      }
  ]
});

myChartwdcd.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
myChartwdcd.hideLoading();
myChartwdcd.setOption(
({
series:[{
        data:result.wdcd
         }
        ]
      })
    )
   }
  });
};

$.get('/data').done(fetchData);

setInterval(fetchData, 5000);