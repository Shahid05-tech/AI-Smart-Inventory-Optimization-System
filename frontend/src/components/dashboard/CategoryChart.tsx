import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend,
} from "recharts";

import ChartCard from "../common/ChartCard";

const COLORS = [
    "#2563EB",
    "#16A34A",
    "#F59E0B",
    "#DC2626",
    "#7C3AED",
    "#0891B2",
];

interface Props {
    data: any[];
}

export default function CategoryChart({
    data,
}: Props) {

    return (

        <ChartCard title="Revenue by Category">

            <ResponsiveContainer
                width="100%"
                height={330}
            >

                <PieChart>

                    <Pie
                        data={data}
                        dataKey="value"
                        nameKey="name"
                        cx="50%"
                        cy="50%"
                        outerRadius={110}
                        innerRadius={55}
                        paddingAngle={3}
                    >

                        {data.map((_, index) => (

                            <Cell
                                key={index}
                                fill={
                                    COLORS[
                                        index % COLORS.length
                                    ]
                                }
                            />

                        ))}

                    </Pie>

                    <Tooltip />

                    <Legend
                        verticalAlign="bottom"
                        height={36}
                    />

                </PieChart>

            </ResponsiveContainer>

        </ChartCard>

    );

}