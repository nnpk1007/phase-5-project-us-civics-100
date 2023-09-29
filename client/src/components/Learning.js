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

            {questions.map(question => (
                <div key={question.id}>
                    <p><strong>{question.id} {question.question_text}</strong></p>

                    {question.answers.map(answer => (
                        <p key={answer}>{answer}</p>
                    ))}
                </div>
            ))}
        </div>
    )

}

export default Learning