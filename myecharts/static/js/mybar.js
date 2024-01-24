var chartDom = document.getElementById('zhu');
var myChartbar = echarts.init(chartDom);

myChartbar.showLoading();
function fetchData(){
    $.ajax({
        url:'/data',
        result:{},
        type:'GET',
        dataType:'json',
        success:function(result){
            myChartbar.hideLoading();
            myChartbar.setOption({
                title: {
                    text:'Bar Example',
                    textStyle:{color:'#33CCFF'}
                },
                toolbox:{
                    show:true,
                    iconStyle:{color:'#33CCFF'},
                    feature:{
                    dataView:{
                               show:true,
                               title:'数据视图',
                               readOnly:false,
                                },
                    saveAsImage:{
                                show:true,
                                type:'png',
                                title:'保存为图片'
                                },
                    magicType:{
                               show:true,
                               type:['line','bar'],
                               title:{'line':'切换为折线图',
                                      'bar':'切换为柱形图'}
                               }
                    }
                },
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
                      data: result.zhudata,
                      type: 'bar',
                      itemStyle:{color:"#CC0000"},
                      showBackground: true,
                      backgroundStyle: {
                        color: 'rgba(180, 180, 180, 0.6)'
                      }
                    }
                ]
            })
        }
    });
};

$.get('/data').done(fetchData);

//setInterval(fetchData, 5000);

myChartbar.on('click',function(params){
    if(params.seriesName=='测试系列' && params.dataIndex==1){
        myChartbar.setOption({
            xAxis: {
                type: 'category',
                axisLabel:{color:"#33CCFF"},
                data: ['one', 'two', 'three',]
            },
            series:[{
                name:'new',
                type:'bar',
                data:[1,2,3]
            }]
        })
    }else{
        $.ajax({
        url:'/data',
        result:{},
        type:'GET',
        dataType:'json',
        success:function(result){
            myChartbar.hideLoading();
            myChartbar.setOption({
                title: {
                    text:'Bar Example',
                    textStyle:{color:'#33CCFF'}
                },
                toolbox:{
                    show:true,
                    iconStyle:{color:'#33CCFF'},
                    feature:{
                    dataView:{
                               show:true,
                               title:'数据视图',
                               readOnly:false,
                                },
                    saveAsImage:{
                                show:true,
                                type:'png',
                                title:'保存为图片'
                                },
                    magicType:{
                               show:true,
                               type:['line','bar'],
                               title:{'line':'切换为折线图',
                                      'bar':'切换为柱形图'}
                               }
                    }
                },
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
                      data: result.zhudata,
                      type: 'bar',
                      itemStyle:{color:"#CC0000"},
                      showBackground: true,
                      backgroundStyle: {
                        color: 'rgba(180, 180, 180, 0.6)'
                      }
                    }
                ]
            })
        }
    });
    }
})