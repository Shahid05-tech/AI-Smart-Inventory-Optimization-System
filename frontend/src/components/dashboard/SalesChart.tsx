import {
    ResponsiveContainer,
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from "recharts";

import ChartCard from "../common/ChartCard";

interface Props {
    data: any[];
}

export default function SalesChart({ data }: Props) {

    return (

        <ChartCard title="Monthly Sales Trend">

            <ResponsiveContainer
                width="100%"
                height={350}
            >

                <AreaChart
                    data={data}
                    margin={{
                        top: 20,
                        right: 20,
                        left: 0,
                        bottom: 0,
                    }}
                >

                    <defs>

                        <linearGradient
                            id="salesGradient"
                            x1="0"
                            y1="0"
                            x2="0"
                            y2="1"
                        >

                            <stop
                                offset="5%"
                                stopColor="#2563EB"
                                stopOpacity={0.35}
                            />

                            <stop
                                offset="95%"
                                stopColor="#2563EB"
                                stopOpacity={0}
                            />

                        </linearGradient>

                    </defs>

                    <CartesianGrid
                        stroke="#E5E7EB"
                        vertical={false}
                    />

                    <XAxis
                        dataKey="month"
                        tickLine={false}
                        axisLine={false}
                    />

                    <YAxis
                        tickLine={false}
                        axisLine={false}
                    />

                    <Tooltip />

                    <Area
                        type="monotone"
                        dataKey="revenue"
                        stroke="#2563EB"
                        strokeWidth={3}
                        fill="url(#salesGradient)"
                    />

                </AreaChart>

            </ResponsiveContainer>

        </ChartCard>

    );

}