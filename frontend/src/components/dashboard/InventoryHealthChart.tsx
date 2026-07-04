import {
    ResponsiveContainer,
    BarChart,
    Bar,
    CartesianGrid,
    XAxis,
    YAxis,
    Tooltip,
} from "recharts";

import ChartCard from "../common/ChartCard";

interface Props {
    data: any[];
}

export default function InventoryHealthChart({
    data,
}: Props) {

    return (

        <ChartCard title="Inventory Status">

            <ResponsiveContainer
                width="100%"
                height={330}
            >

                <BarChart
                    data={data}
                    margin={{
                        top: 20,
                        right: 20,
                        left: 0,
                        bottom: 0,
                    }}
                >

                    <CartesianGrid
                        vertical={false}
                        stroke="#E5E7EB"
                    />

                    <XAxis
                        dataKey="name"
                        axisLine={false}
                        tickLine={false}
                    />

                    <YAxis
                        axisLine={false}
                        tickLine={false}
                    />

                    <Tooltip />

                    <Bar
                        dataKey="count"
                        radius={[8, 8, 0, 0]}
                        fill="#2563EB"
                    />

                </BarChart>

            </ResponsiveContainer>

        </ChartCard>

    );

}