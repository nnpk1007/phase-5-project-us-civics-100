import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Home from "./Home";
import Learning from "./Learning";
import Login from "./Login";
import Signup from "./Signup";
import QuizTest from "./QuizTest";

import "bootstrap/dist/css/bootstrap.min.css";
import QuizHistory from "./QuizHistory";

function App() {
  const [user, setUser] = useState(null);
  const [userId, setUserId] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = () => {
    fetch("/authorized").then((r) => {
      if (r.ok) {
        console.log("Fetch User", r);
        r.json().then((userData) => {
          setUserId(userData.id);
          setUser(userData);
          setIsLoggedIn(true);
        });
      } else {
        r.json().then((errorData) => {
          setErrors([errorData.errors]);
          console.log(errors)
        });
      }
    });
  };
  
  const onLogin=(user) => setUser(user)

 
  const handleLogout = () => {
    fetch("/logout", {
      method: "DELETE",
    }).then((r) => {
      if (r.status === 204) {
        setIsLoggedIn(false);
        setUser(null);
        setUserId(null)
      } else {
        console.error("Logout error:", r.statusText);
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
          element={
            <Login
              onLogin={onLogin}
              setIsLoggedIn={setIsLoggedIn}
              setErrors={setErrors}
              setUserId={setUserId}
            />
          }
        />
        <Route
          path="/signup"
          element={<Signup setIsLoggedIn={setIsLoggedIn} />}
        />
        {isLoggedIn ? (
          <Route path="/test" element={<QuizTest user={user}/>} />
        ) : (
          <Route path="/login" element={<Navigate to="/login" />} />
        )}
        <Route path="/quiz-history" element={<QuizHistory userId={userId}/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
