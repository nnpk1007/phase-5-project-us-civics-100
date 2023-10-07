import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function QuizTest({ user, userId }) {
  const [quiz, setQuiz] = useState([]);
  const [currentQuestionsIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswerIndex, setSelectedAnswerIndex] = useState(null);
  const [score, setScore] = useState(0);

  useEffect(() => {
    console.log("User state in QuizTest:", user);
    const fetchCivicsTest = () => {
      if (user) {
        console.log("User inside if statement:", user);
        fetch("/civics-test")
          .then((res) => res.json())
          .then((data) => {
            //console.log(data)
            setQuiz(data);
          });
      }
    };
    fetchCivicsTest();
  }, [user]);

  const handleAnswerSelect = (answerIndex) => {
    setSelectedAnswerIndex(answerIndex);
  };

  console.log("Quiz.lenght:", quiz.length);
  console.log("Current Question Index:", currentQuestionsIndex);

  const handleNextQuestion = () => {
    const currentQuestion = quiz[currentQuestionsIndex];
    // Check if the selected answer is null
    if (selectedAnswerIndex === null) {
      alert("You must select an answer.");
      return;
    }
    // Check if the selected answer is correct and update the score.
    if (currentQuestion.answer_options[selectedAnswerIndex].correct) {
      // Use the functional form of setScore to update it based on the previous value
      console.log("Before update score:", score);
      setScore((prevScore) => prevScore + 1);
      console.log("After update score:", score);
    }
    // check to make sure the currenQuestionIndex does not go over the limit
    if (currentQuestionsIndex < quiz.length) {
      setCurrentQuestionIndex(currentQuestionsIndex + 1);
    }

    if (currentQuestionsIndex === quiz.length - 1) {
      console.log("User ID:", userId);
      console.log("Score:", score);
      console.log("Length:", quiz.length);
      console.log("Current question index in the If:", currentQuestionsIndex);
      // due to the asynchronous of state updates in React, the score state using setScore
      // might not have been updated immediately.
      // using score + 1 in submitQuizAttempt to ensure that the correct score is submitted (it showed incorrect score when deploy)
      // back to using score only, not + 1

      return submitQuizAttempt(userId, score, quiz.length);
    }
  };

  function submitQuizAttempt(userId, score, quizAttempted) {
    fetch("/submit-quiz-attempt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: userId,
        score: score,
        questions_attempted: quizAttempted,
      }),
    }).then((r) => {
      if (r.ok) {
        console.log("Quiz attempt has been submitted");
      } else {
        console.log("Quiz attenpt submission failed");
      }
    });
  }

  return (
    <>
      <div className="container-fluid">
        <div className="jumborton">
          <h2 className="text-center text-primary mt-5">US Civics Test</h2>
          {currentQuestionsIndex < quiz.length ? (
            <>
              <div className="card border-info">
                <div className="card-header bg-info text-white">
                  Question {currentQuestionsIndex + 1}:{" "}
                  {quiz[currentQuestionsIndex].question_text}
                </div>
                {quiz[currentQuestionsIndex].answer_options.map(
                  (answer, answerIndex) => (
                    <div className="form-check" key={answerIndex}>
                      <input
                        className="form-check-input"
                        type="radio"
                        name={`q${currentQuestionsIndex}`}
                        id={`q${currentQuestionsIndex}_a${answerIndex}`}
                        onChange={() => handleAnswerSelect(answerIndex)}
                      />
                      <label
                        className="form-check-label"
                        htmlFor={`q${currentQuestionsIndex}_a${answerIndex}`}
                      >
                        {answer.answer_text}
                      </label>
                    </div>
                  )
                )}
                <button
                  type="button"
                  className="btn btn-success mt-3"
                  onClick={handleNextQuestion}
                >
                  Next
                </button>
              </div>
              <div>
                <p className="mt-3 text-center">
                  <Link to="/learning">
                    Skip the test and go to learning page
                  </Link>
                </p>
              </div>
            </>
          ) : (
            <div className="text-center">
              <h3 className="text-info">Quiz Completed</h3>
              <p className="score fs-4 fw-bold text-secondary">
                Score: {score}
              </p>
              {score > 5 ? (
                <div className="text-center">
                  <h2 className="text-success">
                    Congratulations! You passed the Civics test
                  </h2>
                </div>
              ) : (
                <div className="text-center">
                  <h2 className="text-danger">Try again next time</h2>
                </div>
              )}
              <p className="mt-3 text-center">
                <Link to="/quiz-history">Your Quiz Attempted History</Link>
              </p>
              <p className="mt-3 text-center">
                <Link to="/learning">Go back to learning page</Link>
              </p>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default QuizTest;
