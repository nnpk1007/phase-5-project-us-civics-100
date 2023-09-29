import { useState, useEffect } from "react"


function Learning() {
    const [questions, setQuestions] = useState([])

    useEffect(() => {
        fetch("/civics100-learning")
            .then(res => res.json())
            .then(data => setQuestions(data))
    }, [])

    return (
        <div className="container mt-5">
            <h1 className="text-center mt-5">Learning Mode</h1>
            <p>* If you are 65 years old or older and have been a legal permanent resident of the United States for 20 or more years, you 
                may study just the questions that have been marked with an asterisk</p>

            {questions.map((question, index) => (
                <div key={question.id}>
                    <p><strong>Question {index+1}: {question.question_text}</strong></p>

                    {question.answers.map(answer => (
                        <p key={answer}>. {answer}</p>
                    ))}
                </div>
            ))}
        </div>
    )

}

export default Learning