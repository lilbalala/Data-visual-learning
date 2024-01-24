echarts.registerTransform(ecStat.transform.histogram);
var chartDom = document.getElementById('hist');
var myCharthist = echarts.init(chartDom);

myCharthist.showLoading();
function fetchData(){
  $.ajax({
            url:'/data',
            result:{},
            type:'get',
            dataType:'json',
            success:function(result){
                myCharthist.hideLoading();
                myCharthist.setOption({
                  title:{
                    text:'Hist Example',
                    textStyle:{color:'#33CCFF'}
                    },
                  dataset:[{
                            source:result.histdata
                          },
                            {
                              transform:{type:'ecStat:histogram'}
                            }
                          ],
                  xAxis: {
                        type:'value',
                        scale:false,
                        axisLabel:{
                            color:'#33CCFF'
                            }
                        },
                  yAxis: {
                        type:'value',
                        axisLine:{show:true},
                        axisLabel:{
                            color:'#33CCFF'
                            }
                    },
                  series: [{
                    type: 'bar',
                    barWidth: '99%',
                    datasetIndex:1,
                    label:{
                            show:true,
                            position:'top',
                            color:'#33CCFF'
                        }
                  }]
                })
            }
  })
};
$.get('/data').done(fetchData)
setInterval(fetchData, 5000);
