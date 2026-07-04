import { Box, Grid, Typography } from "@mui/material";
import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import KPICard from "../components/dashboard/KPICard";
import SalesChart from "../components/dashboard/SalesChart";
import CategoryChart from "../components/dashboard/CategoryChart";
import InventoryHealthChart from "../components/dashboard/InventoryHealthChart";
import TopProductsTable from "../components/dashboard/TopProductsTable";

import Inventory2Icon from "@mui/icons-material/Inventory2";
import StoreIcon from "@mui/icons-material/Store";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import MonitorHeartIcon from "@mui/icons-material/MonitorHeart";
import PaidRoundedIcon from "@mui/icons-material/PaidRounded";
import WarningAmberRoundedIcon from "@mui/icons-material/WarningAmberRounded";

import {
    getDashboardSummary,
    type DashboardSummary,
} from "../services/dashboardService";

import {
    getSalesTrend,
    type SalesTrend,
} from "../services/chartService";

import {
    getCategoryDistribution,
    getInventoryHealth,
    type CategoryDistribution,
    type InventoryHealth,
} from "../services/dashboardAnalyticsService";

import {
    getTopProducts,
    type TopProduct,
} from "../services/topProductService";

export default function Dashboard() {

    const [summary, setSummary] = useState<DashboardSummary>();

    const [salesTrend, setSalesTrend] = useState<SalesTrend[]>([]);

    const [categoryData, setCategoryData] =
        useState<CategoryDistribution[]>([]);

    const [inventoryHealth, setInventoryHealth] =
        useState<InventoryHealth[]>([]);

    const [topProducts, setTopProducts] =
        useState<TopProduct[]>([]);

    useEffect(() => {

        async function loadDashboard() {

            try {

                const [

                    summaryData,

                    salesData,

                    categoryChart,

                    healthChart,

                    products,

                ] = await Promise.all([

                    getDashboardSummary(),

                    getSalesTrend(),

                    getCategoryDistribution(),

                    getInventoryHealth(),

                    getTopProducts(),

                ]);

                setSummary(summaryData);

                setSalesTrend(salesData);

                setCategoryData(categoryChart);

                setInventoryHealth(healthChart);

                setTopProducts(products);

            }

            catch (error) {

                console.error(error);

            }

        }

        loadDashboard();

    }, []);

    return (

        <DashboardLayout>

            <Box mb={4}>

                <Typography
                    variant="h4"
                    fontWeight={700}
                >
                    Smart Inventory Dashboard
                </Typography>

                <Typography color="text.secondary">
                    AI Powered Inventory Optimization System
                </Typography>

            </Box>

            <Grid
                container
                spacing={3}
            >

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Products"
                        value={summary?.products ?? 0}
                        icon={<Inventory2Icon />}
                        color="#2563EB"
                        subtitle="Products"
                    />

                </Grid>

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Stores"
                        value={summary?.stores ?? 0}
                        icon={<StoreIcon />}
                        color="#16A34A"
                        subtitle="Stores"
                    />

                </Grid>

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Suppliers"
                        value={summary?.suppliers ?? 0}
                        icon={<LocalShippingIcon />}
                        color="#F59E0B"
                        subtitle="Suppliers"
                    />

                </Grid>

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Health"
                        value={`${summary?.inventory_health ?? 0}%`}
                        icon={<MonitorHeartIcon />}
                        color="#10B981"
                        subtitle="Inventory"
                    />

                </Grid>

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Revenue"
                        value={`$${Number(summary?.total_sales ?? 0).toLocaleString()}`}
                        icon={<PaidRoundedIcon />}
                        color="#0891B2"
                        subtitle="Total Sales"
                    />

                </Grid>

                <Grid size={{ xs:12, sm:6, lg:2 }}>

                    <KPICard
                        title="Low Stock"
                        value={summary?.low_stock ?? 0}
                        icon={<WarningAmberRoundedIcon />}
                        color="#DC2626"
                        subtitle="Need Attention"
                    />

                </Grid>

                <Grid size={{ xs:12 }}>

                    <SalesChart
                        data={salesTrend}
                    />

                </Grid>

                <Grid size={{ xs:12, lg:6 }}>

                    <CategoryChart
                        data={categoryData}
                    />

                </Grid>

                <Grid size={{ xs:12, lg:6 }}>

                    <InventoryHealthChart
                        data={inventoryHealth}
                    />

                </Grid>

                <Grid size={{ xs:12 }}>

                    <TopProductsTable
                        data={topProducts}
                    />

                </Grid>

            </Grid>

        </DashboardLayout>

    );

}