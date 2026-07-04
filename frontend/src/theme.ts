import { createTheme } from "@mui/material/styles";

const theme = createTheme({

  palette: {

    mode: "light",

    primary: {
      main: "#2563EB",
    },

    secondary: {
      main: "#0F172A",
    },

    success: {
      main: "#16A34A",
    },

    warning: {
      main: "#F59E0B",
    },

    error: {
      main: "#DC2626",
    },

    background: {
      default: "#F8FAFC",
      paper: "#FFFFFF",
    },

  },

  shape: {

    borderRadius: 16,

  },

  typography: {

    fontFamily: "Inter, Roboto, sans-serif",

    h3: {

      fontWeight: 700,

    },

    h4: {

      fontWeight: 700,

    },

    h5: {

      fontWeight: 700,

    },

    h6: {

      fontWeight: 600,

    },

    button: {

      textTransform: "none",

      fontWeight: 600,

    },

  },

  components: {

    MuiCard: {

      styleOverrides: {

        root: {

          borderRadius: 18,

          border: "1px solid #E2E8F0",

          transition: "all .25s ease",

          "&:hover": {

            transform: "translateY(-4px)",

            boxShadow: "0 12px 24px rgba(15,23,42,.08)",

          },

        },

      },

    },

    MuiPaper: {

      styleOverrides: {

        root: {

          borderRadius: 18,

        },

      },

    },

    MuiButton: {

      styleOverrides: {

        root: {

          borderRadius: 12,

          textTransform: "none",

          fontWeight: 600,

          height: 44,

        },

      },

    },

    MuiTextField: {

      defaultProps: {

        size: "small",

        fullWidth: true,

      },

    },

  },

});

export default theme;