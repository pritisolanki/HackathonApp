import React, { useState } from "react";
import { useHistory } from "react-router-dom";

const UserInput = () => {
  const history = useHistory();

  const [start, setstart] = useState(false);
  const [form, setForm] = useState({
    age: "",
    gender: "",
    outdoor: false,
    voluntering: "",
    interest: [],
  });
  const [gender, setGender] = useState(null);
  const [age, setAge] = useState(null);
  const [outdoor, setOutdoor] = useState(false);
  const [voluntering, setVoluntering] = useState(null);

  const handleStart = () => {
    setstart(true);
  };
  // const handleGender = (event) => {
  //   setGender(event.value);
  // };
  // const handleAge = (event) => {
  //   setAge(event.value);
  // };
  // const handleLevel = (event) => {
  //   setOutdoor(event.value);
  //   setVoluntering(event.value);
  // };
  // const handleBackGender = () => {
  //   if (start === true) setstart(false);
  //   // if (gender !== null) setGender(null);
  // };
  // const handleBackAge = () => {
  //   //   if (start === true) setstart(false);
  //   if (gender !== null) setGender(null);
  // };
  // const handleBackLevel = () => {
  //   //   if (start === true) setstart(false);
  //   if (age !== null) setAge(null);
  // };
  return (
    <div>
      {/* {!start && ( */}
      <div>
        <h4>Welcome to iConnect</h4>
        <p>Small steps to big change</p>
        <p>Join us for a cause personalised for you</p>
        <button onClick={() => history.push("/signup")}>GET STARTED</button>
        <p>
          I have an <u onClick={() => history.push("/signin")}>Account</u>
        </p>
      </div>
      {/* )} */}
      {/* {start && gender === null && (
        <div>
          <button onClick={handleBackGender}>Back</button>
          <h4>Let us know more about yourself?</h4>
          <input type="radio" id="male" name="gender" value="male" />
          <label for="male">He/Him</label>
          <br />
          <input type="radio" id="female" name="gender" value="female" />
          <label for="female">She/Her</label>
          <br />
          <input type="radio" id="other" name="gender" value="other" />
          <label for="other">They/Them</label>
          <br />
          <input type="radio" id="other" name="gender" value="nothing" />
          <label for="other">I prefer not to say</label>

          <button onClick={handleGender}>Continue</button>
        </div>
      )}
      {gender !== null && age === null && (
        <div>
          <button onClick={handleBackAge}>Back</button>
          <h4>
            Age is just a number but helps us to provide you a personalized
            experience
          </h4>
          <input type="radio" id="male" name="gender" value="21-24" />
          <label>21-24</label>
          <br />
          <input type="radio" id="female" name="gender" value="25-44" />
          <label>25-44</label>
          <br />
          <input type="radio" id="other" name="gender" value="45-64" />
          <label>45-64</label>
          <br />
          <input type="radio" id="other" name="gender" value="65+" />
          <label>65+</label>

          <button onClick={handleAge}>Continue</button>
        </div>
      )}
      {age !== null && (
        <div>
          <button onClick={handleBackLevel}>Back</button>
          <h4>Almost Done...</h4>
          <p>Are you an?</p>
          <input type="radio" id="male" name="gender" value="true" />
          <label>Outdoorsy</label>
          <br />
          <input type="radio" id="female" name="gender" value="false" />
          <label>Indoorsy</label>
          <p>Level of voluntering?</p>
          <input type="radio" id="male" name="gender" value="Begineer" />
          <label>Begineer</label>
          <br />
          <input type="radio" id="female" name="gender" value="Experienced" />
          <label>Experienced</label>
          <button onClick={handleLevel}>Continue</button>
        </div>
      )} */}
    </div>
  );
};
export default UserInput;
