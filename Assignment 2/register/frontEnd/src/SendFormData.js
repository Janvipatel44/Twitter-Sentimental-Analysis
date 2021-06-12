import React from "react";
import './App.css'
import {
  withRouter
} from "react-router-dom";

//https://stackoverflow.com/questions/41966762/reactjs-how-to-transfer-data-between-pages/41967180

//display details to another page
export class SendFormData extends React.Component { 
    
  constructor(props){
    super(props);
    console.log(props);
  }
  render() {      
      return(
        <div>
          <h1>User Profile</h1>
            <h2>First Name: { this.props.location.state.firstname}</h2>
            <h2>Last Name: {this.props.location.state.lastname}</h2>
            <h2>Email: {this.props.location.state.email}</h2>
            <h2>Password: {this.props.location.state.password}</h2>
        </div>
      )
  }
}

export default withRouter(SendFormData);