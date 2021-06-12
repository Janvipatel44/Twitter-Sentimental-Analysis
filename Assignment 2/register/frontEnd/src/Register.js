import React, {Component} from "react";
import './Register.css';
import {
  withRouter
} from "react-router-dom";
import DropdownMenu from "react-bootstrap/esm/DropdownMenu";
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
    
    //validating email format: janvipatel4199@gmail.com
    validateEmail(email){
      const pattern = /[a-zA-Z0-9]+[\.]?([a-zA-Z0-9]+)?[\@][a-z]{3,9}[\.][a-z]{2,5}/g;
      const result = pattern.test(email);
      if(result===true){
        this.setState({
          emailStringError:false,
          email:email
        })
      } else{
        this.setState({
          emailStringError:true
        })
      }
    }

    //validating alphanumeric string for first name and lastname
    validateAlphaNumericString(fieldName, value){
      const pattern = /[a-zA-Z0-9]/g;
      const result = pattern.test(value);
      
        //checking field name as first name or last name
        if(fieldName === 'username') {
          if(result===true){
            this.setState({
              userNameStringError:false,
              value:value
            })
          }
          else {
              this.setState({
                userNameStringError:true
              })
          }
        }         
    }

    //validating password contains alphanumeric and special characters and length equals or more than 8
    validatePassword (value)
    {
      console.log(value);
      const pattern =  /^(?=.*[a-zA-Z0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/g;
      const result = pattern.test(value);

      if(result===true) {
        this.setState({
          passwordStringError:false,
          value:value
        })
      } 
      else{
        this.setState({
          passwordStringError:true
        })
      }  
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
        if (!this.state.userName) {
          this.setState({usernameError: true})
        }
        if (!this.state.email) {
          this.setState({emailError: true})
        }
        if (!this.state.password) {
          this.setState({passwordError: true})
        }
        if (!this.state.confirmpassword) {
          this.setState({confirmpasswordError: true})
        }
      }
      if(e.target.name==='username'){
        if(e.target.value==='' || e.target.value===null ){
          this.setState({
            usernameError:true
          })
        } else {
          this.setState({
            usernameError:false,     
            userName:e.target.value
          })
          this.validateAlphaNumericString(e.target.name, e.target.value );
        }
      }
      if(e.target.name==='email'){
        if(e.target.value==='' || e.target.value===null){
          this.setState({
            emailError:true
          })
        } else {
          this.setState({
            emailError:false,
            email:e.target.value
          })
          this.validateEmail(e.target.value);
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
          this.validatePassword(e.target.value);
          if (e.target.value && this.state.confirmpassword) {
            this.validateConfirmPassword(this.state.password,e.target.value);
          }
        }
        
      }
      
    }

    //submitting form once checking there is no error in any flag
    submitForm(e)
    {
      this.handleChange(e);
      e.preventDefault();
    
      if(this.state.usernameError === true) {
        alert('User name field is empty!!!!');
      }
      if(this.state.userNameStringError === true) {
        alert('User name can only alphanumeric values!!!');
      }
    
      if(this.state.passwordError === true) {
        alert('Password field is empty!!!!');
      }
      if(this.state.passwordStringError === true) {
        alert('Password should contain alphanumeric values, special characters and with more than 8 characters!!!');
      }
    
      if(this.state.emailError === true) {
        alert('Email filed is empty!!!!');
      }
      if(this.state.emailStringError === true) {
        alert('Email format is not valid!!!!');
      }
      if(this.state.usernameError===false &&
         this.state.userNameStringError === false &&
         this.state.emailError===false && this.state.emailStringError === false && 
         this.state.passwordError===false && this.state.passwordStringError===false ){
        
        this.setState({
          isDisabled:false
        })
        console.log('Submitted successfully!!!');
        alert('Duplicate Entry! Already registered user!');

        e.preventDefault();
        
        axios.post('http://localhost:5000/register', this.state).then((response) => {
            if (response.status == 200) {
              console.log('Registration successfully done!');

              this.props.history.push({
                    pathname: 'https://container2-login-ubd4wnd23n1knn.run.app',
                    state: this.state
              });
            }
            else{
              console.log('Registration is not done successfully!');
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
                  <h1><center>Registeration Page</center></h1>
                  <div className="form-group">
                    <div className="form-label-group">
                      <label htmlFor="username">User Name*: </label>
                      <input type="text" id="username" name="username" className="form-control" placeholder="Enter username" onChange={(e)=>{this.handleChange(e)}} />
                      {this.state.usernameError ? <span style={{color: "red"}}>Username is required </span> : ''} 
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="form-label-group">
                      <label htmlFor="email"> Email*: </label>
                      <input type="email" id="email" name="email" className="form-control" placeholder="Enter your email" onChange={(e)=>{this.handleChange(e)}} />
                      {this.state.emailError ? <span style={{color: "red"}}>Email is required</span> : ''}
                    </div>
                  </div>                
                  <div className="form-group">
                    <div className="form-label-group">
                      <label htmlFor="password"> Password*: </label>
                      <input type="password" id="password" name="password" className="form-control" placeholder="Password"  onChange={(e)=>{this.handleChange(e)}} />
                      {this.state.passwordError ? <span style={{color: "red"}}>Password is required</span> : ''}
                    </div>
                  </div>   
                  <div className="form-group">
                    <label htmlFor="selectedValue"> Value*: </label>
                    <select id="dropdown-basic" onChange={this.handleDropdownChange}>
                                        <option value>Choose</option>
                                        <option value="Serverless">Serverless</option>
                                        <option value="GCP">GCP</option>
                    </select> 
                  </div>                
                  <button className="btn btn-primary btn-block" onClick={this.submitForm} name="submit">Submit</button>
                  <h1> </h1>
                  <button className="btn btn-primary btn-block" onClick={this.submitForm} name="login">Login</button>
                </form>
            </div>
          </div>
        </div>
      );
    }
}

export default withRouter(Register);