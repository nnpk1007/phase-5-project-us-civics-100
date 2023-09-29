import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Home"
import Learning from "./Learning"
import Login from "./Login"
import Signup from "./Signup"
import QuizTest from "./QuizTest"

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/learning" element={<Learning />}/>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/test" element={<QuizTest />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
