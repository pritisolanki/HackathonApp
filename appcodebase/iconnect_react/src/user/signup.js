import React, { useState } from "react";
import Backendless from "../backendless/Credentials";
import { useHistory } from "react-router-dom";
const Signup = () => {
  const history = useHistory();
  const [userData, setUserData] = useState({
    email: "",
    password: "",
    name: "",
  });
  const handleInput = (event) => {
    console.log(event.target.name, event.target.value);
    setUserData((prev) => ({
      ...prev,
      [event.target.name]: event.target.value,
    }));
  };

  const handleSignup = (event) => {
    // var user = new Backendless.User();
    // user.email = "backendlessdeveloper@backedless.com";
    // user.password = "password";
    //     event.preventDefault();
    console.log(userData);
    Backendless.UserService.register(userData)
      .then(function (registeredUser) {
        console.log(registeredUser);
        alert("success");
      })
      .catch(function (error) {
        console.log(error);
      });
    // Backendless.Data.of("demo")
    //   .find()
    //   .then(function (result) {
    //     if (
    //       result.find(
    //         (item) =>
    //           item.email === userData.email &&
    //           item.password === userData.password
    //       )
    //     )
    //       alert("success");
    //     console.log(result);
    //   })
    //   .catch(function (error) {});
  };
  return (
    <div className="container m-5 border p-5">
      <form>
        <div class="form-group">
          <label>Name</label>
          <input
            type="name"
            class="form-control"
            id="name"
            aria-describedby="name"
            placeholder="Enter Name"
            name="name"
            onChange={handleInput}
          />
        </div>

        <div class="form-group">
          <label>Email address</label>
          <input
            type="email"
            class="form-control"
            id="email"
            aria-describedby="email"
            placeholder="Enter email"
            name="email"
            onChange={handleInput}
          />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input
            type="password"
            class="form-control"
            id="password"
            placeholder="Password"
            name="password"
            onChange={handleInput}
          />
        </div>

        <button
          type="button"
          className="btn btn-primary mr-1"
          onClick={handleSignup}
        >
          Submit
        </button>
        <button
          type="button"
          className="btn btn-default"
          onClick={() => history.push("/signin")}
        >
          I have an <u>Account</u>
        </button>
      </form>
    </div>
  );
};

export default Signup;
