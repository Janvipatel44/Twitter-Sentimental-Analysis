import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Register from './Register';

//route for 2 pages 
export default function App() {
  return (
    <div style = {{ marginLeft : 30 }}>
      <Router>
        <div>
          <Switch>
            <Route path="/register">
                <Register />
            </Route>
            </Switch>
        </div>
      </Router>
    </div>
  );
}