var chartDom = document.getElementById('category_2_mount');
var myChartwc = echarts.init(chartDom);
var option;

var maskResource = new Image();
maskResource.src ='/static/img/tm.png';

myChartwc.setOption({
    title:{
        text:'商品二级类目的销量情况',
        x:'center',
        textStyle:{color:'#33CCFF',}
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
  series:[
    {
//            maskImage: maskResource,
            //词的类型
            type:'wordCloud',
            //设置字符大小范围
            sizeRange:[6, 78],
            rotationRange:[-45, 90],
            textStyle: {
                color: function() {
                    // Random color
                    return 'rgb(' + [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160)
                    ].join(',') + ')'
                }
            },
            //不要忘记调用数据
            data:[]
  }
  ]
});

myChartwc.showLoading();
function fetchData(){
$.ajax({
url:'/data',
result:{},
type:'GET',
dataType:'json',
success:function(result){
console.log(result.category_2_mount),
myChartwc.hideLoading();

myChartwc.setOption(
{
series:[
        {
        data:result.category_2_mount
      }
      ]
     }
    )
   }
  });
};

$.get('/data').done(fetchData);

//setInterval(fetchData, 5000);
