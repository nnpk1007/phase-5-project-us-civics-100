import { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";

function Learning({ isLoggedIn, handleLogout }) {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetch("/civics100-learning")
      .then((res) => res.json())
      .then((data) => setQuestions(data));
  }, []);
  console.log(questions);

  return (
    <>
      <nav className="navbar navbar-expand-lg fixed-top navbar-dark" style={{ backgroundColor: "#e3f2fd"}}>
        <h2 className="ms-3" style={{ color: "#441C3E" }}>
          100 Civics Questions and Answers (2008 version)
        </h2>
        <div className="navbar-nav ms-auto">
          <NavLink className="nav-link ms-auto" style={{ color: "#1B1824" }} to="/test">
            QuizTest
          </NavLink>
          {isLoggedIn ? (
            <>
              <NavLink
                className="nav-link ms-auto"
                style={{ color: "#1B1824" }}
                to="/quiz-history"
              >
                Quiz History
              </NavLink>
              <button
                className="nav-link ms-auto"
                style={{ color: "#1B1824" }}
                onClick={() => {
                  handleLogout();
                }}
              >
                Logout
              </button>
            </>
          ) : (
            <NavLink
              className="nav-link"
              style={{ color: "#1B1824" }}
              to="/login"
            >
              Login
            </NavLink>
          )}
        </div>
      </nav>
      <div className="container mt-5" style={{paddingTop: "150px"}}>
        <p className="fst-italic fw-lighter" style={{color: "#70067D"}}>
          Although USCIS is aware that there may be additional correct answers
          to the 100 civics questions, applicants are encouraged to respond to
          the civics questions using the answers provided below.
        </p>
        <p className="fst-italic fw-lighter" style={{color: "#70067D"}}>
          * If you are 65 years old or older and have been a legal permanent
          resident of the United States for 20 or more years, you may study just
          the questions that have been marked with an asterisk
        </p>

        {questions.map((question, index) => (
          <div key={question.id} >
            <p style={{color: "#48033D"}}>
              <strong>
                Question {index + 1}: {question.question_text}
              </strong>
            </p >

            {question.answers.map((answer) => (
              <p key={answer} style={{color: "#48033D"}}>. {answer}</p>
            ))}
          </div>
        ))}
      </div>
    </>
  );
}

export default Learning;
