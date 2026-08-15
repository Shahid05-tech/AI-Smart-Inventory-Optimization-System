import { useEffect, useState } from "react";

import {
    Alert,
    Box,
    Button,
    Card,
    CardContent,
    Grid,
    LinearProgress,
    MenuItem,
    Select,
    Typography,
    FormControl,
    InputLabel,
    Chip,
} from "@mui/material";

import DashboardLayout from "../layouts/DashboardLayout";

import { getRecommendation } from "../services/inventoryService";

import {
    getStores,
    getProducts,
    type Store,
    type Product,
} from "../services/lookupService";

export default function Recommendation() {

    const [stores, setStores] = useState<Store[]>([]);
    const [products, setProducts] = useState<Product[]>([]);

    const [storeId, setStoreId] = useState(1);
    const [productId, setProductId] = useState(1);

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState<any>(null);

    useEffect(() => {

        async function load() {

            const s = await getStores();
            const p = await getProducts();

            setStores(s);
            setProducts(p);

            if (s.length)
                setStoreId(s[0].store_id);

            if (p.length)
                setProductId(p[0].product_id);

        }

        load();

    }, []);

    async function predict() {

        setLoading(true);

        try {

            const response =
                await getRecommendation({

                    store_id: storeId,

                    product_id: productId,

                });

            setResult(response);

        }

        catch {

            alert("Prediction Failed");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <DashboardLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                Inventory Recommendation
            </Typography>

            <Grid
                container
                spacing={3}
            >

                <Grid size={{ xs: 12, md: 4 }}>

                    <Card>

                        <CardContent>

                            <Typography
                                variant="h6"
                                gutterBottom
                            >
                                Recommendation Input
                            </Typography>

                            <Box sx={{ mt: 2 }}>

                                <FormControl fullWidth>

                                    <InputLabel>
                                        Store
                                    </InputLabel>

                                    <Select

                                        label="Store"

                                        value={storeId}

                                        onChange={(e) =>
                                            setStoreId(
                                                Number(e.target.value)
                                            )
                                        }
                                    >

                                        {
                                            stores.map(store => (

                                                <MenuItem
                                                    key={store.store_id}
                                                    value={store.store_id}
                                                >
                                                    {store.store_name}
                                                </MenuItem>

                                            ))
                                        }

                                    </Select>

                                </FormControl>

                            </Box>

                            <Box sx={{ mt: 3 }}>

                                <FormControl fullWidth>

                                    <InputLabel>
                                        Product
                                    </InputLabel>

                                    <Select

                                        label="Product"

                                        value={productId}

                                        onChange={(e) =>
                                            setProductId(
                                                Number(e.target.value)
                                            )
                                        }
                                    >

                                        {
                                            products.map(product => (

                                                <MenuItem
                                                    key={product.product_id}
                                                    value={product.product_id}
                                                >
                                                    {product.product_name}
                                                </MenuItem>

                                            ))
                                        }

                                    </Select>

                                </FormControl>

                            </Box>

                            <Box sx={{ mt: 4 }}>

                                <Button
                                    fullWidth
                                    variant="contained"
                                    onClick={predict}
                                >
                                    Generate Recommendation
                                </Button>

                            </Box>

                        </CardContent>

                    </Card>

                </Grid>

                <Grid size={{ xs: 12, md: 8 }}>

                    <Card>

                        <CardContent>

                            <Typography
                                variant="h6"
                                gutterBottom
                            >
                                Prediction Result
                            </Typography>

                            {
                                loading &&
                                <LinearProgress />
                            }

                            {

                                result &&

                                <>

                                    <Box sx={{ mt: 3 }}>

                                        <Typography variant="h5">

                                            Predicted Demand

                                        </Typography>

                                        <Typography
                                            variant="h3"
                                        >
                                            {result.predicted_demand}
                                        </Typography>

                                    </Box>

                                    <Box sx={{ mt: 3 }}>

                                        <Typography>

                                            Safety Stock

                                        </Typography>

                                        <Typography variant="h5">

                                            {result.safety_stock}

                                        </Typography>

                                    </Box>

                                    <Box sx={{ mt: 3 }}>

                                        <Typography>

                                            Recommended Stock

                                        </Typography>

                                        <Typography variant="h5">

                                            {result.recommended_stock}

                                        </Typography>

                                    </Box>

                                    <Box sx={{ mt: 3 }}>

                                        <Typography>

                                            Inventory Health

                                        </Typography>

                                        <LinearProgress
                                            variant="determinate"
                                            value={result.inventory_health}
                                            sx={{
                                                height:12,
                                                borderRadius:5,
                                                mt:1
                                            }}
                                        />

                                        <Typography
                                            sx={{ mt: 1 }}
                                        >
                                            {result.inventory_health}%
                                        </Typography>

                                    </Box>

                                    <Box sx={{ mt: 4 }}>

                                        {
                                            result.reorder_required ?

                                                <Alert severity="warning">

                                                    Reorder Required

                                                </Alert>

                                                :

                                                <Alert severity="success">

                                                    Inventory Level is Healthy

                                                </Alert>

                                        }

                                    </Box>

                                    <Box sx={{ mt: 3 }}>

                                        <Chip

                                            color={
                                                result.reorder_required
                                                    ? "error"
                                                    : "success"
                                            }

                                            label={
                                                result.reorder_required
                                                    ? "LOW STOCK"
                                                    : "HEALTHY"
                                            }

                                        />

                                    </Box>

                                </>

                            }

                        </CardContent>

                    </Card>

                </Grid>

            </Grid>

        </DashboardLayout>

    );

}