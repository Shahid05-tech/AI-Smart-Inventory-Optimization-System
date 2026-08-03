import {
    Avatar,
    Box,
    Typography,
} from "@mui/material";

export default function UserProfile() {

    return (

        <Box
            sx={{
                display: "flex",
                alignItems: "center",
                gap: 2,
                mt: "auto",
                p: 2,
            }}
        >

            <Avatar
                sx={{
                    bgcolor: "primary.main",
                }}
            >
                A
            </Avatar>

            <Box>

                <Typography
                    sx={{ fontWeight: 600 }}
                >
                    Administrator
                </Typography>

                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    Inventory Manager
                </Typography>

            </Box>

        </Box>

    );

}