import React from "react"
import { Link } from "react-router-dom"


function LandingPage() {
    return (
        <div className="text-center mt-5">
            <h1>US Civics 100 Exam Prep</h1>
            <p className="lead">
                Prepare for your civics exam and test your knowledge
            </p>
            <Link to="/learning">
                <button className="btn btn-primary">Get Started</button>
            </Link>
        </div>
    )
}

export default LandingPage
