var chartDom = document.getElementById('pst');
var myChartpst = echarts.init(chartDom);

myChartpst.showLoading();
function fetchData(){
    $.ajax({
            url:'/data',
            result:{},
            type:'get',
            dataType:'json',
            success:function(result){
                myChartpst.hideLoading();
                const CATEGORY_DIM_COUNT = result.pdata.dlen-1;
                const GAP=2;
                const BASE_LEFT=5;
                const BASE_TOP = 8;
                const GRID_WIDTH = (100 - BASE_LEFT - GAP) / CATEGORY_DIM_COUNT - GAP;
                const GRID_HEIGHT = (100 - BASE_TOP - GAP-2) / CATEGORY_DIM_COUNT - GAP;
                const CATEGORY_DIM = result.pdata.dlen-1;
                const SYMBOL_SIZE = 4;
                function retrieveScatterData(data, dimX, dimY) {
                          let result = [];
                          for (let i = 0; i < data.length; i++) {
                            let item = [data[i][dimX], data[i][dimY]];
                            item[CATEGORY_DIM] = data[i][CATEGORY_DIM];
                            result.push(item);
                          }
                          return result;
                        }
                function generateGrids(){
                      let index = 0;
                      const grid = [];
                      const xAxis = [];
                      const yAxis = [];
                      const series = [];
                      for(let i=0;i<result.pdata.dlen;i++){
                        for(let j=i;j<result.pdata.dlen-1;j++){
                          grid.push({
                            left:BASE_LEFT + i * (GRID_WIDTH + GAP) + '%',
                            top:BASE_TOP + j * (GRID_HEIGHT+GAP) + '%',
                            width:GRID_WIDTH+'%',
                            height:GRID_HEIGHT+'%',
                           }),
                          xAxis.push({
                            splitNumber:3,
                            position: 'bottom',
                            axisLine:{show:j==CATEGORY_DIM_COUNT - 1,onZero:false},
                            axisTick:{show:j==CATEGORY_DIM_COUNT - 1,inside:true},
                            axisLabel:{show:j==CATEGORY_DIM_COUNT - 1,color:'#33CCFF'},
                            type: 'value',
                            gridIndex: index,
                            scale: true,
                            name:j==CATEGORY_DIM_COUNT - 1?result.pdata.col[i]:"",
                            nameLocation:'center',
                            nameGap:20,
                            nameTextStyle:{color:'#33CCFF'}
                          }),
                          yAxis.push({
                            splitNumber:3,
                            position: 'left',
                            axisLine:{show:i==0,onZero:false},
                            axisTick:{show:i==0,inside:true},
                            axisLabel:{show:i==0,color:'#33CCFF'},
                            type: 'value',
                            gridIndex: index,
                            scale: true,
                            name:i==0?result.pdata.col[j]:"",
                            nameLocation:'center',
                            nameGap:20,
                            nameTextStyle:{color:'#33CCFF'}
                          }),
                          series.push({
                            type: 'scatter',
                            xAxisIndex: index,
                            yAxisIndex: index,
                            data:retrieveScatterData(result.pdata.pdata, i, j)
                          });
                          index++;
                        }
                      }
                    return {grid,xAxis,yAxis,series};
                    }
                const gridOption = generateGrids();
                myChartpst.setOption({
                  animation: false,
                  visualMap: {
                        type: 'piecewise',
                        categories: result.pdata.cat,
                        dimension: CATEGORY_DIM,
                        orient: 'horizontal',
                        top: 0,
                        left: 'center',
                        textStyle:{color:'#33CCFF'},
                        inRange: {
                          color: ['#51689b', '#ce5c5c', '#fbc357']
                        },
                        outOfRange: {
                          color: '#ddd'
                        },
                        seriesIndex: gridOption.series.map(function (_, idx) {
                                      return idx;
                                    })
                      },
                  tooltip: {
                            trigger: 'item'
                          },
                  title:{text:'散点图矩阵',textStyle:{color:'#33CCFF'}},
                  grid:gridOption.grid,
                  xAxis: gridOption.xAxis,
                  yAxis: gridOption.yAxis,
                  series:gridOption.series
                })
            }
    })
};
$.get('/data').done(fetchData)
setInterval(fetchData, 5000);