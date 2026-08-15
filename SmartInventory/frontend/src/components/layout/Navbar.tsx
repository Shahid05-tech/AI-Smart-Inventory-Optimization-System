import {
    AppBar,
    Toolbar,
    Typography,
    Box,
    IconButton,
    Badge,
    TextField,
    InputAdornment,
} from "@mui/material";

import NotificationsNoneRoundedIcon from "@mui/icons-material/NotificationsNoneRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";

const drawerWidth = 270;

export default function Navbar() {

    return (

        <AppBar
            position="fixed"
            elevation={0}
            sx={{
                width: `calc(100% - ${drawerWidth}px)`,
                ml: `${drawerWidth}px`,
                bgcolor: "#FFFFFF",
                color: "#111827",
                borderBottom: "1px solid #E5E7EB",
                boxShadow: "none",
                zIndex: 1201,
            }}
        >

            <Toolbar
                sx={{
                    minHeight: 72,
                    height: 72,
                    px: 4,
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                }}
            >

                <Box>

                    <Typography
                        variant="h5"
                        fontWeight={700}
                    >
                        Smart Inventory Dashboard
                    </Typography>

                    <Typography
                        variant="body2"
                        color="text.secondary"
                    >
                        AI Powered Inventory Optimization
                    </Typography>

                </Box>

                <Box
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        gap: 2,
                    }}
                >

                    <TextField
                        size="small"
                        placeholder="Search..."
                        sx={{
                            width: 240,
                            "& .MuiOutlinedInput-root": {
                                borderRadius: 3,
                                bgcolor: "#F8FAFC",
                            },
                        }}
                        InputProps={{
                            startAdornment: (
                                <InputAdornment position="start">
                                    <SearchRoundedIcon />
                                </InputAdornment>
                            ),
                        }}
                    />

                    <IconButton>

                        <Badge
                            badgeContent={3}
                            color="error"
                        >

                            <NotificationsNoneRoundedIcon />

                        </Badge>

                    </IconButton>

                    <IconButton>

                        <SettingsRoundedIcon />

                    </IconButton>

                </Box>

            </Toolbar>

        </AppBar>

    );

}