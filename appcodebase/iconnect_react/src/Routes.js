import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";

import App from "./App";
import Signin from "./user/signin";
import Signup from "./user/signup";
import UserInput from "./user/UserInput";

const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={UserInput}></Route>
        <Route path="/signin" exact component={Signin}></Route>
        <Route path="/signup" exact component={Signup}></Route>
        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;
