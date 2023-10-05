import { useState, useEffect } from "react";

function QuizHistory({ userId }) {
  const [quizAttempts, setQuizAttempts] = useState([]);
  console.log("User id first load:",userId);

  useEffect(() => {
    const fetchQuizAttempts = () => {
      if (userId) {
        fetch(`/quiz-attempts/${userId}`)
          .then((r) => r.json())
          .then((data) => setQuizAttempts(data))
      }
    };
    
    fetchQuizAttempts();
  }, [userId]);
    
  return (
    <>
      <div className="container mt-4">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card">
              <div className="card-header text-center bg-info text-white">
                <h4>Quiz History</h4>
              </div>
              <div className="card-body">
                <table className="table table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Score</th>
                      <th scope="col">Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {quizAttempts.map((attempt) => (
                      <tr key={attempt.id}>
                        <td>{attempt.score}</td>
                        <td>
                          {new Date(attempt.quiz_date).toLocaleString()} {/* https://www.w3schools.com/jsref/jsref_tolocalestring.asp */}
                        </td>{" "}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
export default QuizHistory;
