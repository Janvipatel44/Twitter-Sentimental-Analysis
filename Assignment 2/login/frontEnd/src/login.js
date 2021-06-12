import React, {Component} from "react";
import './Register.css';
import {
  withRouter
} from "react-router-dom";

import axios from 'axios';

//https://stackoverflow.com/questions/41296668/reactjs-form-input-validation 

//https://stackoverflow.com/questions/46595961/validate-string-length-and-make-sure-it-contains-certain-characters-in-react-red/46599759

//https://stackoverflow.com/questions/42858542/react-this-props-is-undefined

//https://stackoverflow.com/questions/12090077/javascript-regular-expression-password-validation-having-special-characters
export class Register extends Component
{
    //constructor for props
    constructor(props)
    {
        super(props);
        this.state = {}                                                                                                 
        this.submitForm = this.submitForm.bind(this);
    }

    //once the change occured on click event check whether fields are empty or not and validating the fields
    handleChange(e)
    {
      const target = e.target;
      const value = target.type === 'checkbox' ? target.checked : target.value;
      const name = target.name;
      this.setState({
        [name]: value
      });
      if (e.target.name === 'submit') {
        if (!this.state.loginId) {
          this.setState({loginIdError: true})
        }
       
        if (!this.state.password) {
          this.setState({passwordError: true})
        }
      
      }
      if(e.target.name==='loginId'){
        if(e.target.value==='' || e.target.value===null ){
          this.setState({
            loginIdError:true
          })
        } else {
          this.setState({
            loginIdError:false,     
            loginId:e.target.value
          })
        }
      }
    
      if(e.target.name==='password'){
        if(e.target.value==='' || e.target.value===null){
          this.setState({
            passwordError:true
          })
        } else {
          this.setState({
            passwordError:false,
            password:e.target.value
          })          
        }
      }
    }

    //submitting form once checking there is no error in any flag
    submitForm(e)
    {
      this.handleChange(e);
      e.preventDefault();
    
      if(this.state.loginIdError === true) {
        alert('User name field is empty!!!!');
      }
        
      if(this.state.passwordError === true) {
        alert('Password field is empty!!!!');
      }
 
      if(this.state.loginIdError===false && this.state.passwordError===false  )
      {
        
        this.setState({
            isDisabled:false
        })
        console.log('Submitted successfully!!!');
        alert('Login Unsuccessful, Please check the credentials');
  
        axios.post('http://localhost:5000/login', this.state).then((response) => {
              if (response.status == 444) {
                alert('Login Successful');
                this.props.history.push({
                  pathname: 'https://container3-logout-ubd423113n1knn.run.app',
                  state: this.state
                });
              }
              else if (response.status == 300) {
                alert('Login Unsuccessful, Please check the credentials');
              }
          })    
      }        
      
      else{
        console.log('Unsuccessful submission!!!');
      } 
    }

    //rendering the front page
    render()
    {
    return(
      <div className="container">
        <div className="card card-login mx-auto mt-5">
          <div class="container"> </div>
            <div className="card-body">
                <form id="signup-form">
                  <h1><center>Login Page</center></h1>
                  <div className="form-group">
                    <div className="form-label-group">
                      <label htmlFor="loginId">User Name*: </label>
                      <input type="loginId" id="loginId" name="loginId" className="form-control" placeholder="Login Id" onChange={(e)=>{this.handleChange(e)}} />
                      {this.state.usernameError ? <span style={{color: "red"}}>Username is required </span> : ''} 
                    </div>
                  </div>              
                  <div className="form-group">
                    <div className="form-label-group">
                      <label htmlFor="password"> Password*: </label>
                      <input type="password" id="password" name="password" className="form-control" placeholder="Password"  onChange={(e)=>{this.handleChange(e)}} />
                      {this.state.passwordError ? <span style={{color: "red"}}>Password is required</span> : ''}
                    </div>
                  </div>                  
                  <button className="btn btn-primary btn-block" onClick={this.submitForm} name="submit">Submit</button>
                </form>
            </div>
          </div>
        </div>
      );
    }
}

export default withRouter(Register);