import React, { useEffect } from 'react';
import * as echarts from 'echarts/core';
import { GridComponent, GridComponentOption } from 'echarts/components';
import { LineChart, LineSeriesOption } from 'echarts/charts';
import { UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([
  GridComponent,
  LineChart,
  CanvasRenderer,
  UniversalTransition
]);

export type BasicLineChartOptions = {
  grid?: GridComponentOption;
  xAxis?: { [key: string]: any };
  yAxis?: { [key: string]: any };
  series?: LineSeriesOption[];
};

interface BasicLineChartProps {
  option: BasicLineChartOptions;
  width?: string;
  height?: string;
}

const BasicLineChartComponent: React.FC<BasicLineChartProps> = ({
  option,
  width = '100%',
  height = '400px',
}) => {
  const chartRef = React.createRef<HTMLDivElement>();

  useEffect(() => {
    if (chartRef.current) {
      const myChart = echarts.init(chartRef.current, 'dark');
      myChart.setOption(option);

      window.addEventListener('resize', () => {
        myChart.resize();
      });

      return () => {
        myChart.dispose();
      };
    }
  }, [chartRef, option]);

  return <div ref={chartRef} style={{ width, height }} />;
};

export default BasicLineChartComponent;
