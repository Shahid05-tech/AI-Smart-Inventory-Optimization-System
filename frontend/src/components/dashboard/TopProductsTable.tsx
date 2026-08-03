import {
    Paper,
    Typography,
    Table,
    TableHead,
    TableRow,
    TableCell,
    TableBody,
} from "@mui/material";

interface Props {
    data: any[];
}

export default function TopProductsTable({ data }: Props) {
    return (
        <Paper
            elevation={0}
            sx={{
                border: "1px solid #E5E7EB",
                borderRadius: 4,
                p: 3,
            }}
        >
            <Typography
                variant="h6"
                fontWeight={700}
                mb={2}
            >
                Top Selling Products
            </Typography>

            <Table size="small">

                <TableHead>

                    <TableRow>

                        <TableCell>
                            Product
                        </TableCell>

                        <TableCell align="right">
                            Quantity
                        </TableCell>

                    </TableRow>

                </TableHead>

                <TableBody>

                    {data.map((item, index) => (

                        <TableRow key={index}>

                            <TableCell>

                                {item.product}

                            </TableCell>

                            <TableCell align="right">

                                {item.quantity}

                            </TableCell>

                        </TableRow>

                    ))}

                </TableBody>

            </Table>

        </Paper>
    );
}