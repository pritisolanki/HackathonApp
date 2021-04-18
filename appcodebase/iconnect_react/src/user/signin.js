import React, { useState } from "react";
import Backendless from "../backendless/Credentials";
import { useHistory } from "react-router-dom";

const Signin = () => {
  const history = useHistory();

  //   const templateParams = {
  //     from_name: "Asit",
  //     to_name: "Suresh",
  //     feedback: "My Feedback",
  //   };

  //   const sendMessage = () => {
  //     // emailjs
  //     // .send("gmail", "portfoliositecontact", templateParams, "panda9asit@gmail.com")
  //     // .then(
  //     //     function(response) {
  //     //     toast.success("Your message has successfully sent!", {
  //     //         position: toast.POSITION.BOTTOM_CENTER
  //     //     });
  //     //     console.log("SUCCESS!", response.status, response.text);
  //     //     },
  //     //     function(err) {
  //     //     toast.error("Your message was not able to be sent");
  //     //     }
  //     // );
  //     };
  const [userData, setUserData] = useState({ email: "", password: "" });
  const handleInput = (event) => {
    console.log(event.target.name, event.target.value);
    setUserData((prev) => ({
      ...prev,
      [event.target.name]: event.target.value,
    }));
  };

  const handleLogin = (event) => {
    // var user = new Backendless.User();
    // user.email = "backendlessdeveloper@backedless.com";
    // user.password = "password";
    //     event.preventDefault();
    console.log(userData);
    Backendless.UserService.login(userData.email, userData.password, true)
      .then(function (loggedInUser) {
        console.log(loggedInUser);
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
          onClick={handleLogin}
        >
          Submit
        </button>
        <button
          type="button"
          className="btn btn-default"
          onClick={() => history.push("/signup")}
        >
          Create an Account
        </button>
      </form>
    </div>
  );
};

export default Signin;
