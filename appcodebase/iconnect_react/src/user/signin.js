import React from "react";

const Signin=()=>{
    const templateParams = {
        from_name: "Asit",
        to_name: "Suresh",
        feedback: "My Feedback"
      };

    //  const sendMessage=()=> {
    //     emailjs
    //     .send("gmail", "portfoliositecontact", templateParams, "panda9asit@gmail.com")
    //     .then(
    //         function(response) {
    //         toast.success("Your message has successfully sent!", {
    //             position: toast.POSITION.BOTTOM_CENTER
    //         });
    //         console.log("SUCCESS!", response.status, response.text);
    //         },
    //         function(err) {
    //         toast.error("Your message was not able to be sent");
    //         }
    //     );
    // };


    return (
    <div className="container m-5 border p-5">
        <form>
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" aria-describedby="email" placeholder="Enter email"/>
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" placeholder="Password"/>
            </div>

             <button type="button" className="btn btn-primary mr-1" onClick={sendMessage}>Submit</button>
             <button type="button" className="btn btn-default">Cancel</button>            
        </form>
    </div>
    )
}

export default Signin;