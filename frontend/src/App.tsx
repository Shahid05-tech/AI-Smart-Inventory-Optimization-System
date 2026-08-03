import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Recommendation from "./pages/Recommendation";
import Inventory from "./pages/Inventory";
import Analytics from "./pages/Analytics";

function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/recommendation"
                    element={<Recommendation />}
                />

                <Route
                    path="/inventory"
                    element={<Inventory />}
                />

                <Route
                    path="/analytics"
                    element={<Analytics />}
                />

            </Routes>

        </BrowserRouter>

    );

}

export default App;