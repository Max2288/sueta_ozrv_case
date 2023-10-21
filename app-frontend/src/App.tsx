import NavBarSearch from "actions/components/Navbar/NavbarSerach";
import BasicLineChartComponent, { BasicLineChartOptions } from 'actions/components/Charts/BasicLineChart/BasicLineChart';
import WaterfallChartComponent, { WaterfallChartOptions } from 'actions/components/Charts/WaterfallChart/WaterfallChart';
import PieChartComponent, { PieChartOptions, PieChartData } from 'actions/components/Charts/PieChart/PieChart';
import { useState, useEffect } from "react";
import { Routes, Route } from 'react-router-dom';
import { fetchJsonData } from "actions/utils/post";
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import 'actions/styles/App.css'


function App() {
  const [bsLineChartOpt, setBasicChartOptions] = useState<BasicLineChartOptions>({});
  const [wfChartOpt, setWaterfallChartOptions] = useState<WaterfallChartOptions>({});
  const [pChartOpt, setPieChartOptions] = useState<PieChartOptions>({});
  useEffect(() => {
    const apiBasicUrl = "http://127.0.0.1:8011/api/v1/monitoring/basic-line";
    const apiWaterfallUrl = "http://127.0.0.1:8011/api/v1/monitoring/waterfall";
    const apiPieUrl = "http://127.0.0.1:8011/api/v1/monitoring/pie";
    const headers = {
      "Content-Type": "application/json",
      "Accept": "application/json"
    }
    const fetchBasicData = async () => {
      try {
        const jsonData = await fetchJsonData(apiBasicUrl, "GET", headers);
        const basicLineChartOptions: BasicLineChartOptions = {
          grid: {
            left: '10%',
            right: '10%',
            bottom: '5%',
            containLabel: true,
          },
          xAxis: {
            type: 'category',
            data: jsonData.xAxis,
          },
          yAxis: {
            type: 'value',
          },
          series: jsonData.series
        };
        setBasicChartOptions(basicLineChartOptions);
      } catch (error) {
        console.error("Ошибка:", error);
      }
    };
    const fetchWaterfallData = async () => {
      try {
        const jsonData = await fetchJsonData(apiWaterfallUrl, "GET", headers);
        const waterfallChartOptions: WaterfallChartOptions = {
          title: {
            text: 'Waterfall Chart',
            subtext: 'Living Expenses in Shenzhen',
            padding: 20,
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            },
            formatter: function (params: any) {
              var tar = params[0];
              return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
            }
          },
          grid: {
            left: '10%',
            right: '10%',
            bottom: '6%',
            containLabel: true,
          },
          xAxis: {
            type: 'category',
            splitLine: { show: false },
            data: jsonData.xAxis
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name: 'Life Cost',
              type: 'bar',
              stack: 'Total',
              label: {
                show: true,
                position: 'inside'
              },
              data: jsonData.series
            }
          ]
        }
        setWaterfallChartOptions(waterfallChartOptions);
      } catch (error) {
        console.error("Ошибка:", error);
      }
    };

    const fetchPieData = async () => {
      try {
        const jsonData = await fetchJsonData(apiPieUrl, "GET", headers);
        const data: [PieChartData]  = jsonData.data
        const pieChartOptions: PieChartOptions = {
          backgroundColor: '#2c343c',
          title: {
            text: 'Customized Pie',
            left: 'center',
            top: 20,
            textStyle: {
              color: '#ccc'
            }
          },
          tooltip: {
            trigger: 'item'
          },
          visualMap: {
            show: false,
            min: 80,
            max: 600,
            inRange: {
              colorLightness: [0, 1]
            }
          },
          series: [
            {
              name: 'Access From',
              type: 'pie',
              radius: '55%',
              center: ['50%', '50%'],
              data: data.sort(function (a, b) {
                return a.value - b.value;
              }),
              roseType: 'radius',
              label: {
                color: 'rgba(255, 255, 255, 0.3)'
              },
              labelLine: {
                lineStyle: {
                  color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
              },
              itemStyle: {
                color: '#c23531',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              },
              animationType: 'scale',
              animationEasing: 'elasticOut',
              animationDelay: () => Math.random() * 200
            }
          ]
        };
        setPieChartOptions(pieChartOptions);
      } catch (error) {
        console.error("Ошибка:", error);
      }
    };

    fetchBasicData();
    fetchWaterfallData();
    fetchPieData();
  }, []);


  
  return (
    <>
      <NavBarSearch />
      <Routes>
        <Route
          path="/charts"
          element={
            <>
              <BasicLineChartComponent option={bsLineChartOpt} width="100%" height="250px" />
              <WaterfallChartComponent option={wfChartOpt} width="100%" height="400px" />
              <PieChartComponent option={pChartOpt} width="100%" height="400px" />
            </>
          }
        />
      </Routes>
    </>
  );
};




export default App;