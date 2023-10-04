import { useState, useEffect } from "react";

function QuizTest() {
  const [quiz, setQuiz] = useState([]);
  const [currentQuestionsIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswerIndex, setSelectedAnswerIndex] = useState(null);
  const [score, setScore] = useState(0);

  useEffect(() => {
    fetch("/civics-test")
      .then((res) => res.json())
      .then((data) => {
        //console.log(data)
        setQuiz(data);
      });
  }, []);

  console.log("Length:", quiz.length);
  console.log("Current question index:", currentQuestionsIndex)

  const handleAnswerSelect = (answerIndex) => {
    setSelectedAnswerIndex(answerIndex);
  };

  const handleNextQuestion = () => {
    // Check if the selected answer is correct and update the score.
    const currentQuestion = quiz[currentQuestionsIndex];
    if (
      selectedAnswerIndex !== null &&
      currentQuestion.answer_options[selectedAnswerIndex].correct
    ) {
      setScore(score + 1);
    }
    // check to make sure the currenQuestionIndex does not go over the limit
    if (currentQuestionsIndex < quiz.length) {
      setCurrentQuestionIndex(currentQuestionsIndex + 1);
    }
  };
  console.log("Score:", score);

  return (
    <>
      <div className="container-fluid">
        <div className="jumborton">
          <h2 className="text-center text-primary mt-5">US Civics Test</h2>
          {currentQuestionsIndex < quiz.length ? (
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
          ) : (
            <div className="text-center">
              <h3 className="text-info">Quiz Completed</h3>
              <p className="score fs-4 fw-bold text-secondary">Score: {score}</p>
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
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default QuizTest;
