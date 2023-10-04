import { useState, useEffect } from "react";

function QuizTest() {
  const [quiz, setQuiz] = useState([]);
  const [currentQuestionsIndex, setCurrentQuestionIndex] = useState(0);

  useEffect(() => {
    fetch("/civics-test")
      .then((res) => res.json())
      .then((data) => {
        //console.log(data)
        setQuiz(data);
      });
  }, []);

  console.log(quiz);
  
  const handleNextQuestion = () => {
    // check to make sure the currenQuestionIndex does not go over the limit
    if (currentQuestionsIndex < quiz.length -1) {
      setCurrentQuestionIndex(currentQuestionsIndex + 1)
    }
  }

  return (
    <>
      <div className="container-fluid">
        <div className="jumborton">
          <h2 className="text-center mt-5">US Civics Test</h2>
        {currentQuestionsIndex < quiz.length &&  ( 
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
        )}
        </div>
        </div>
    </>
  );
}

export default QuizTest;
