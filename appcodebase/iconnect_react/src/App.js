import './App.css';
import'bootstrap/dist/css/bootstrap.css';
import {Link, withRouter} from "react-router-dom";
// import'bootstrap/dist/css/bootstrap-theme.css';


function App() {
  return (
    <div>
      <Link to="/signup">
        <button type="button" class="btn btn-primary" style={{ marginRight: 5 }}>
          SignUp
        </button>
        </Link>
      <Link to="/signin">
        <button type="button" class="btn btn-primary">SignIn</button>
      </Link>

    </div>
  );
}

export default App;
// export default withRouter(App);
