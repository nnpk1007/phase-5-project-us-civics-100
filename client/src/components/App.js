import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Home";
import Learning from "./Learning";
import Login from "./Login";
import Signup from "./Signup";
import QuizTest from "./QuizTest";

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [user, setUser] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogout = () => {
    fetch("/logout", {
      method: "DELETE",
    }).then((r) => {
      if (r.status === 204) {
        setIsLoggedIn(false);
        setUser(null)
      } else {
        console.error("Logout error:", r.statusText)
      }
    });
  };

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/learning"
          element={
            <Learning isLoggedIn={isLoggedIn} handleLogout={handleLogout} />
          }
        />
        <Route
          path="/login"
          element={<Login onLogin={(user) => setUser(user)} setIsLoggedIn={setIsLoggedIn}/>}
        />
        <Route path="/signup" element={<Signup setIsLoggedIn={setIsLoggedIn}/>} />
        <Route path="/test" element={<QuizTest />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
