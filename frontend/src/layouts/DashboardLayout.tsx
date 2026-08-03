import { Box } from "@mui/material";
import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

interface Props {
    children: React.ReactNode;
}

export default function DashboardLayout({ children }: Props) {

    return (

        <Box
            sx={{
                display: "flex",
                minHeight: "100vh",
                bgcolor: "#F8FAFC",
            }}
        >

            <Sidebar />

            <Navbar />

            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    ml: "270px",
                    mt: "72px",
                    p: 4,
                    minHeight: "100vh",
                }}
            >

                {children}

            </Box>

        </Box>

    );

}