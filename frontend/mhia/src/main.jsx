import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/layout/Header.jsx";
import Footer from "./components/layout/Footer.jsx";
import Landing from "./pages/Landing.jsx";
import LogInPage from "./pages/LogIn.jsx";
import SelectPatient from "./pages/SelectPatient.jsx";
import SessionPage from "./pages/Session.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<LogInPage />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/patients" element={<SelectPatient />} />
        <Route path="/session/:patientId" element={<SessionPage />}/>
        <Route path="*" element={<div>Page not found</div>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  </StrictMode>
);