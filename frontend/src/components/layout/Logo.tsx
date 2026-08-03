import { Box, Typography } from "@mui/material";
import Inventory2RoundedIcon from "@mui/icons-material/Inventory2Rounded";

export default function Logo() {
    return (
        <Box
            sx={{
                display: "flex",
                alignItems: "center",
                gap: 1.5,
                py: 2,
            }}
        >
            <Inventory2RoundedIcon
                sx={{
                    fontSize: 34,
                    color: "primary.main",
                }}
            />

            <Box>
                <Typography
                    sx={{ fontWeight: 700, fontSize: 18 }}
                >
                    Smart Inventory
                </Typography>

                <Typography
                    variant="caption"
                    color="text.secondary"
                >
                    Optimization System
                </Typography>
            </Box>
        </Box>
    );
}