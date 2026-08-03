import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import {
    Box,
    Card,
    CardContent,
    Grid,
    Paper,
    Typography,
} from "@mui/material";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    PieChart,
    Pie,
    Cell,
    BarChart,
    Bar,
    CartesianGrid,
} from "recharts";

import {
    getMonthlyRevenue,
    getCategoryRevenue,
    getTopProducts,
    getTopStores,
    getDiscountSummary,
} from "../services/analyticsService";

const COLORS = [
    "#1976d2",
    "#2e7d32",
    "#ed6c02",
    "#9c27b0",
    "#d32f2f",
    "#0288d1",
];

export default function Analytics() {

    const [monthlyRevenue, setMonthlyRevenue] = useState<any[]>([]);
    const [categoryRevenue, setCategoryRevenue] = useState<any[]>([]);
    const [topProducts, setTopProducts] = useState<any[]>([]);
    const [topStores, setTopStores] = useState<any[]>([]);
    const [discount, setDiscount] = useState(0);

    useEffect(() => {

        async function load() {

            const [
                revenue,
                category,
                products,
                stores,
                discountSummary
            ] = await Promise.all([
                getMonthlyRevenue(),
                getCategoryRevenue(),
                getTopProducts(),
                getTopStores(),
                getDiscountSummary(),
            ]);

            setMonthlyRevenue(revenue);
            setCategoryRevenue(category);
            setTopProducts(products);
            setTopStores(stores);
            setDiscount(discountSummary.average_discount);

        }

        load();

    }, []);

    return (

        <DashboardLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                Analytics Dashboard
            </Typography>

            <Grid container spacing={3}>

                <Grid size={{ xs: 12 }}>

                    <Paper sx={{ p: 2, height: 400 }}>

                        <Typography variant="h6">
                            Monthly Revenue
                        </Typography>

                        <ResponsiveContainer>

                            <LineChart data={monthlyRevenue}>

                                <CartesianGrid strokeDasharray="3 3"/>

                                <XAxis dataKey="month"/>

                                <YAxis/>

                                <Tooltip/>

                                <Line
                                    type="monotone"
                                    dataKey="revenue"
                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </Paper>

                </Grid>

                <Grid size={{ xs: 12, md: 6 }}>

                    <Paper sx={{ p:2, height:350 }}>

                        <Typography variant="h6">
                            Revenue by Category
                        </Typography>

                        <ResponsiveContainer>

                            <PieChart>

                                <Pie
                                    data={categoryRevenue}
                                    dataKey="revenue"
                                    nameKey="category"
                                    outerRadius={100}
                                >

                                    {
                                        categoryRevenue.map((_, index)=>(

                                            <Cell
                                                key={index}
                                                fill={COLORS[index % COLORS.length]}
                                            />

                                        ))
                                    }

                                </Pie>

                                <Tooltip/>

                            </PieChart>

                        </ResponsiveContainer>

                    </Paper>

                </Grid>

                <Grid size={{ xs:12, md:6 }}>

                    <Paper sx={{ p:2, height:350 }}>

                        <Typography variant="h6">
                            Top Selling Products
                        </Typography>

                        <ResponsiveContainer>

                            <BarChart data={topProducts}>

                                <XAxis dataKey="product"/>

                                <YAxis/>

                                <Tooltip/>

                                <Bar dataKey="quantity"/>

                            </BarChart>

                        </ResponsiveContainer>

                    </Paper>

                </Grid>

                <Grid size={{ xs:12, md:6 }}>

                    <Paper sx={{ p:2, height:350 }}>

                        <Typography variant="h6">
                            Top Stores
                        </Typography>

                        <ResponsiveContainer>

                            <BarChart data={topStores}>

                                <XAxis dataKey="store"/>

                                <YAxis/>

                                <Tooltip/>

                                <Bar dataKey="revenue"/>

                            </BarChart>

                        </ResponsiveContainer>

                    </Paper>

                </Grid>

                <Grid size={{ xs:12, md:6 }}>

                    <Card sx={{ height:350 }}>

                        <CardContent>

                            <Typography
                                variant="h6"
                                gutterBottom
                            >
                                Average Discount
                            </Typography>

                            <Box
                                sx={{
                                    display: "flex",
                                    justifyContent: "center",
                                    alignItems: "center",
                                    height: "250px",
                                }}
                            >

                                <Typography variant="h2">

                                    {discount}%

                                </Typography>

                            </Box>

                        </CardContent>

                    </Card>

                </Grid>

            </Grid>

        </DashboardLayout>

    );

}