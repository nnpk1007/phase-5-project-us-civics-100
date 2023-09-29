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
  const [loggedIn, setLoggedIn] = useState(false)

  useEffect(() => {
    // auto-login
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          setUser(user)
          setLoggedIn(true)
        });
      }
    });
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/learning" element={<Learning isLoggedIn={setLoggedIn}/>} />
        <Route
          path="/login"
          element={<Login onLogin={(user) => setUser(user)} />}
        />
        <Route path="/signup" element={<Signup />} />
        <Route path="/test" element={<QuizTest />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
