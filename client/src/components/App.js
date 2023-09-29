import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Home"
import Learning from "./Learning"

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/learning" element={<Learning />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App;
