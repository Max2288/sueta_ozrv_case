import React, { useEffect } from 'react';
import * as echarts from 'echarts/core';
import {
    TitleComponent,
    TitleComponentOption,
    TooltipComponent,
    TooltipComponentOption,
    VisualMapComponent,
    VisualMapComponentOption
} from 'echarts/components';
import { PieChart, PieSeriesOption } from 'echarts/charts';
import { LabelLayout } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([
    TitleComponent,
    TooltipComponent,
    VisualMapComponent,
    PieChart,
    CanvasRenderer,
    LabelLayout
]);

export type PieChartOptions = {
    backgroundColor?: string;
    title?: TitleComponentOption;
    tooltip?: TooltipComponentOption;
    visualMap?: VisualMapComponentOption;
    series?: PieSeriesOption[];
};

export type PieChartData = {
    value: number;
    name: string;
};

interface PieChartProps {
    option: PieChartOptions;
    width?: string;
    height?: string;
}

const PieChartComponent: React.FC<PieChartProps> = ({
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

export default PieChartComponent;
