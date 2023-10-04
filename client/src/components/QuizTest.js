import { useState, useEffect } from "react";

function QuizTest() {
  const [quiz, setQuiz] = useState([]);
  
  useEffect(() => {
    fetch("/civics-test")
      .then((res) => res.json())
      .then((data) => {
        //console.log(data)
        setQuiz(data);
      });
  }, []);

  console.log(quiz)

  return (
    // resource to learn how to build a quiz test by Bootstrap
    // https://medium.com/@reul.ghorm/get-familiar-with-bootstrap-components-build-a-simple-knowledge-quiz-d5908beeb5ba
    <>
      <div className="container-fluid">
        <div className="jumborton">
          <h2 className="text-center mt-5">US Civics Test</h2>
          {quiz.map((question, index) => (
            <div className="card border-info">
              <div key={question.id}>
                <div className="card-header bg-info text-white">
                  Question {index + 1}: {question.question_text}
                </div>
                {question.answers.map((answer, index) => (
                  <div className="form-check">
                    <input
                      className="form-check-input"
                      type="checkbox"
                      value=""
                      id={index + 1}
                    />
                    <label
                      className="form-check-label"
                      htmlFor="flexCheckIndeterminate"
                    >
                      {answer}
                    </label>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
      <h3>Result</h3>

      <div class="card">
        <div class="card-body">
          <p id="result">No result.</p>

          <div class="progress mb-2">
            <div
              class="progress-bar"
              role="progressbar"
              aria-valuenow="0"
              aria-valuemin="0"
              aria-valuemax="100"
            ></div>
          </div>

          <button type="button" class="btn btn-success">
            Update
          </button>
        </div>
      </div>
    </>
  );
}

export default QuizTest;
