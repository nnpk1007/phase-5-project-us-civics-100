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
      <nav className="navbar navbar-expand fixed-top navbar-light bg-light">
        <div className="navbar-nav ms-auto">
          <NavLink className="nav-link" style={{ color: "purple" }} to="/test">
            QuizTest
          </NavLink>
          {isLoggedIn ? (
            <>
              <NavLink
                className="nav-link"
                style={{ color: "purple" }}
                to="/quiz-history"
              >
                Quiz History
              </NavLink>
              <button
                className="nav-link"
                style={{ color: "purple" }}
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
              style={{ color: "purple" }}
              to="/login"
            >
              Login
            </NavLink>
          )}
        </div>
      </nav>
      <div className="container mt-5">
        <h2 className="text-center mt-5">
          Civics Questions and Answers (2008 version)
        </h2>
        <p>
          Although USCIS is aware that there may be additional correct answers
          to the 100 civics questions, applicants are encouraged to respond to
          the civics questions using the answers provided below.
        </p>
        <p>
          * If you are 65 years old or older and have been a legal permanent
          resident of the United States for 20 or more years, you may study just
          the questions that have been marked with an asterisk
        </p>

        {questions.map((question, index) => (
          <div key={question.id}>
            <p>
              <strong>
                Question {index + 1}: {question.question_text}
              </strong>
            </p>

            {question.answers.map((answer) => (
              <p key={answer}>. {answer}</p>
            ))}
          </div>
        ))}
      </div>
    </>
  );
}

export default Learning;
