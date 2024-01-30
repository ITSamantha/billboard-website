import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Routes, Route, Link, Router } from "react-router-dom";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import React, { useState } from "react";
import HomePage from "./pages/HomePage";

export default function App() {
  return (
    <>
      <div style={{ direction: "rtl" }}>
        <Header />
        <HomePage/>
        <Footer/>
      </div>
    </>
  );
}
