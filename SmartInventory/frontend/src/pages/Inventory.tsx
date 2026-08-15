import { useEffect, useMemo, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import {
    Box,
    Button,
    Chip,
    Paper,
    TextField,
    Typography,
} from "@mui/material";

import {
    DataGrid,
    type GridColDef,
} from "@mui/x-data-grid";

import {
    getInventory,
    type InventoryItem,
} from "../services/inventoryTableService";

export default function Inventory() {

    const [rows, setRows] =
        useState<InventoryItem[]>([]);

    const [search, setSearch] =
        useState("");

    useEffect(() => {

        async function load() {

            const data =
                await getInventory();

            setRows(data);

        }

        load();

    }, []);

    const filteredRows = useMemo(() => {

        return rows.filter(row =>

            row.store
                .toLowerCase()
                .includes(search.toLowerCase())

            ||

            row.product
                .toLowerCase()
                .includes(search.toLowerCase())

        );

    }, [rows, search]);

    function exportCSV() {

        const header = [
            "Store",
            "Product",
            "Current Stock",
            "Minimum",
            "Maximum",
            "Health",
            "Status"
        ];

        const csv = [

            header.join(","),

            ...filteredRows.map(r => [

                r.store,

                r.product,

                r.current_stock,

                r.minimum_stock,

                r.maximum_stock,

                r.inventory_health,

                r.status

            ].join(","))

        ].join("\n");

        const blob = new Blob(
            [csv],
            {
                type: "text/csv"
            }
        );

        const url =
            URL.createObjectURL(blob);

        const link =
            document.createElement("a");

        link.href = url;

        link.download = "inventory.csv";

        link.click();

    }

    const columns: GridColDef[] = [

        {
            field: "store",
            headerName: "Store",
            flex: 1
        },

        {
            field: "product",
            headerName: "Product",
            flex: 1
        },

        {
            field: "current_stock",
            headerName: "Current",
            width: 120
        },

        {
            field: "minimum_stock",
            headerName: "Minimum",
            width: 120
        },

        {
            field: "maximum_stock",
            headerName: "Maximum",
            width: 120
        },

        {
            field: "inventory_health",
            headerName: "Health %",
            width: 120
        },

        {
            field: "status",
            headerName: "Status",
            width: 150,

            renderCell: (params) => (

                <Chip

                    label={params.value}

                    color={
                        params.value === "Healthy"

                            ? "success"

                            : "error"
                    }

                />

            )

        }

    ];

    return (

        <DashboardLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                Inventory Management
            </Typography>

            <Paper
                sx={{
                    p: 2
                }}
            >

                <Box
                    sx={{
                        display: "flex",
                        justifyContent: "space-between",
                        mb: 2
                    }}
                >

                    <TextField

                        label="Search"

                        value={search}

                        onChange={(e) =>
                            setSearch(e.target.value)
                        }

                    />

                    <Button
                        variant="contained"
                        onClick={exportCSV}
                    >
                        Export CSV
                    </Button>

                </Box>

                <DataGrid

                    rows={filteredRows}

                    columns={columns}

                    getRowId={(row) =>
                        row.inventory_id
                    }

                    pageSizeOptions={[
                        10,
                        25,
                        50
                    ]}

                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 10,
                                page: 0
                            }
                        }
                    }}

                    autoHeight

                />

            </Paper>

        </DashboardLayout>

    );

}