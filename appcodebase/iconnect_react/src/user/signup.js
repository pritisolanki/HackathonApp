import React from "react";

const Signup=()=>{
    return (
        <div className="container m-5 border p-5">
            <form>

                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="name" class="form-control" id="name" aria-describedby="name" placeholder="Enter Name"/>
                </div>

                <div class="form-group">
                    <label for="email">Email address</label>
                    <input type="email" class="form-control" id="email" aria-describedby="email" placeholder="Enter email"/>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Password"/>
                </div>

                <button type="button" className="btn btn-primary mr-1">Submit</button>
                <button type="button" className="btn btn-default">Cancel</button>

            </form>
        </div>
      
    )
}

export default Signup;