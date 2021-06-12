import React, {Component} from "react";
import {
  withRouter
} from "react-router-dom";
import axios from 'axios'
import Button from 'react-bootstrap/Button'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'

export class logout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    };
  }

  componentDidMount() {
    fetch('https://container2-login-ubd4wnd23n1knn.run.app')
      .then(res => res.json())
      .then(result => {
        this.setState({
          isLoaded: true,
          items: result
        });
      });
  }
  logOut = (event) => {
      axios.post('https://container3-logout-ubd423113n1knn.run.app', this.state).then((response) => {
          window.location.href = 'https://container2-login-ubd4wnd23n1knn.run.app/'
      })
  }
  render() {
        const apiData = this.state.onlineUsers
        return (
            <div>
                <Container>
                    <Row>
                        <Col xs={12}>
                            <Row>
                                <Col>
                                    Welcome User {this.state.email}
                                </Col>
                                <Col>
                                    <Button variant="primary" type="submit" onClick={this.logOut}>
                                        LogOut
                                    </Button>
                                </Col>
                            </Row>
                        </Col>
    
                        
                        <Col xs={12}>
                            < Table striped hover >
                                <thead className="table-header">
                                    <tr>
                                        <th>#</th>
                                        <th>User Name</th>
                                        <th>Activation Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {apiData.map((row, index) => {
                                        return (
                                            <tr>
                                                <td>{index + 1}</td>
                                                <td>{row.name}</td>
                                                <td className={row.state}>{row.state}</td>
                                            </tr>
                                        )
                                    })}
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                </Container>


            </div>
        )
    }

}

export default logout; // this is eliminated  
