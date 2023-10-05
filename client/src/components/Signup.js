import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Signup({ setIsLoggedIn, fetchUser }) {
  const [username, setUsername] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [passwordConfirmation, setPasswordConfirmation] = useState("")

  const [errors, setErrors] = useState([]);

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    const newUser = {
        username,
        email,
        password,
        passwordConfirmation,
    }
    e.preventDefault();
    fetch("/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newUser),
    }).then((r) => {
        console.log(newUser);
      if (r.ok) {
        r.json().then(() => {
          setUsername("");
          setEmail("")
          setPassword("")
          setPasswordConfirmation("")
          setIsLoggedIn(true)
          fetchUser(newUser)
          navigate("/learning");
        })
      } else {
        r.json().then((errorData) => {
          // console.log(errorData);
          setErrors([errorData.errors]);
          console.log("Errors:", errors);
          console.log(errors.length);
        });
      }
    });
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2 className="text-center">Signup</h2>
            </div>
            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="username" className="form-label">
                    Username
                  </label>
                  <input
                    type="text"
                    id="username"
                    className="form-control"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">
                    Email
                  </label>
                  <input
                    type="text"
                    id="email"
                    className="form-control"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">
                    Password
                  </label>
                  <input
                    type="password"
                    id="password"
                    className="form-control"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">
                    Password Confirmation
                  </label>
                  <input
                    type="password"
                    id="password-confirmation"
                    className="form-control"
                    value={passwordConfirmation}
                    onChange={(e) => setPasswordConfirmation(e.target.value)}
                    required
                  />
                </div>
                {errors.length > 0 && (
                  <div className="alert alert-danger">
                    {errors.map((error, index) => (
                      <p key={index}>{error}</p>
                    ))}
                  </div>
                )}
                <div className="text-center">
                  <button type="submit" className="btn btn-primary">
                    Signup
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Signup;
