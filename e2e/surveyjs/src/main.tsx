import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import DateTimeLocal from "./pages/DateTimeLocal.tsx";
import Color from "./pages/Color.tsx";
import Month from "./pages/Month.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/datetime-local",
    element: <DateTimeLocal />,
  },
  {
    path: "/color",
    element: <Color />,
  },
  {
    path: "/month",
    element: <Month />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
