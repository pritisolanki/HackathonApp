import {BrowserRouter, Switch, Route} from "react-router-dom";

import App from "./App";
import Signin from "./user/signin";
import Signup from "./user/signup";



const Routes=()=>{
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={App}></Route>
                <Route path="/signin" exact component={Signin}></Route>
                <Route path="/signup" exact component={Signup}></Route>
            </Switch>
        </BrowserRouter>
    )
}


export default Routes;