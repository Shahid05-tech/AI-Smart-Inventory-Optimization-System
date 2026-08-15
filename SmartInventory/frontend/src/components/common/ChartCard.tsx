import {
    Card,
    CardContent,
    Typography,
} from "@mui/material";

interface Props {

    title: string;

    children: React.ReactNode;

}

export default function ChartCard({

    title,

    children,

}: Props) {

    return (

        <Card
            elevation={0}
            sx={{
                borderRadius: 4,
                border: "1px solid #E5E7EB",
                height: "100%",
            }}
        >

            <CardContent
                sx={{
                    p: 3,
                }}
            >

                <Typography
                    variant="h6"
                    fontWeight={700}
                    mb={3}
                >
                    {title}
                </Typography>

                {children}

            </CardContent>

        </Card>

    );

}