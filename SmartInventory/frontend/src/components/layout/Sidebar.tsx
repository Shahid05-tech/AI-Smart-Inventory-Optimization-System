import {
  Drawer,
  Box,
  Typography,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
  Avatar,
} from "@mui/material";

import DashboardRoundedIcon from "@mui/icons-material/DashboardRounded";
import Inventory2RoundedIcon from "@mui/icons-material/Inventory2Rounded";
import SmartToyRoundedIcon from "@mui/icons-material/SmartToyRounded";
import AutoGraphRoundedIcon from "@mui/icons-material/AutoGraphRounded";

import { NavLink } from "react-router-dom";

const drawerWidth = 270;

const menuItems = [
  {
    text: "Dashboard",
    icon: <DashboardRoundedIcon />,
    path: "/",
  },
  {
    text: "Recommendation",
    icon: <SmartToyRoundedIcon />,
    path: "/recommendation",
  },
  {
    text: "Inventory",
    icon: <Inventory2RoundedIcon />,
    path: "/inventory",
  },
  {
    text: "Analytics",
    icon: <AutoGraphRoundedIcon />,
    path: "/analytics",
  },
];

export default function Sidebar() {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,

        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
          borderRight: "1px solid #E5E7EB",
          backgroundColor: "#FFFFFF",
          display: "flex",
          flexDirection: "column",
        },
      }}
    >
      {/* Logo */}
      <Box
        sx={{
          px: 3,
          py: 3,
        }}
      >
        <Typography
          variant="h5"
          fontWeight={800}
          color="primary"
        >
          Smart Inventory
        </Typography>

        <Typography
          variant="body2"
          color="text.secondary"
        >
          AI Optimization System
        </Typography>
      </Box>

      <Divider />

      {/* Navigation */}
      <List
        sx={{
          px: 2,
          py: 2,
          flexGrow: 1,
        }}
      >
        {menuItems.map((item) => (
          <NavLink
            key={item.text}
            to={item.path}
            style={{ textDecoration: "none" }}
          >
            {({ isActive }) => (
              <ListItemButton
                sx={{
                  mb: 1,
                  borderRadius: 3,
                  minHeight: 48,
                  bgcolor: isActive ? "#EEF4FF" : "transparent",

                  "&:hover": {
                    bgcolor: "#F8FAFC",
                  },
                }}
              >
                <ListItemIcon
                  sx={{
                    minWidth: 40,
                    color: isActive ? "#2563EB" : "#64748B",
                  }}
                >
                  {item.icon}
                </ListItemIcon>

                <ListItemText
                  primary={item.text}
                  primaryTypographyProps={{
                    fontWeight: isActive ? 700 : 500,
                    color: isActive ? "#2563EB" : "#334155",
                  }}
                />
              </ListItemButton>
            )}
          </NavLink>
        ))}
      </List>

      <Divider />

      {/* Footer */}
      <Box
        sx={{
          p: 2.5,
          display: "flex",
          alignItems: "center",
          gap: 2,
        }}
      >
        <Avatar
          sx={{
            width: 44,
            height: 44,
            bgcolor: "#2563EB",
            fontWeight: 700,
          }}
        >
          A
        </Avatar>

        <Box>
          <Typography
            fontWeight={700}
            fontSize={15}
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
    </Drawer>
  );
}