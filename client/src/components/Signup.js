import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";

function Signup({ setIsLoggedIn, fetchUser }) {
  const [errors, setErrors] = useState([]);

  const navigate = useNavigate();

  const formSchema = yup.object().shape({
    username: yup
      .string()
      .required("Must enter username")
      .max(15, "Username must be at most 15 characters"),
    email: yup.string().email("Invalid email").required("Must enter email"),
    password: yup
      .string()
      .required("Must enter password")
      .min(6, "Password is too short - should be 6 characters minimum.")
      .max(125),
    passwordConfirmation: yup
      .string()
      .oneOf([yup.ref("password"), null], "Passwords must match")
      .required("Must enter password confirmation"),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      passwordConfirmation: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(values, null, 2),
      }).then((r) => {
        if (r.ok) {
          r.json().then(() => {
            setIsLoggedIn(true);
            console.log(values)
            fetchUser(values);
            navigate("/learning");
          });
          } else {
            r.json().then((errorData) => {
              // console.log(errorData);
              setErrors([errorData.errors]);
              console.log("Errors:", errorData.errors);
            });
        }
      });
    },
  });

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2 className="text-center">Signup</h2>
            </div>
            <div className="card-body">
              <form onSubmit={formik.handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="username" className="form-label">
                    Username
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="username"
                    name="username"
                    onChange={formik.handleChange}
                    value={formik.values.username}
                  />
                  {formik.touched.username && formik.errors.username && (
                    <div className="alert alert-danger">
                      {formik.errors.username}
                    </div>
                  )}
                </div>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">
                    Email
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="email"
                    name="email"
                    onChange={formik.handleChange}
                    value={formik.values.email}
                  />
                  {formik.touched.email && formik.errors.email && (
                    <div className="alert alert-danger">
                      {formik.errors.email}
                    </div>
                  )}
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">
                    Password
                  </label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    name="password"
                    onChange={formik.handleChange}
                    value={formik.values.password}
                  />
                  {formik.touched.password && formik.errors.password && (
                    <div className="alert alert-danger">
                      {formik.errors.password}
                    </div>
                  )}
                </div>
                <div className="mb-3">
                  <label htmlFor="passwordConfirmation" className="form-label">
                    Password Confirmation
                  </label>
                  <input
                    type="password"
                    className="form-control"
                    id="passwordConfirmation"
                    name="passwordConfirmation"
                    value={formik.values.passwordConfirmation}
                    onChange={formik.handleChange}
                  />
                  {formik.touched.passwordConfirmation &&
                    formik.errors.passwordConfirmation && (
                      <div className="alert alert-danger">
                        {formik.errors.passwordConfirmation}
                      </div>
                    )}
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

              <p className="mt-3 text-center">
            <Link to="/learning">Go back to learning page</Link>
          </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Signup;
