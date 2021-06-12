const express = require('express')
const db = require('./db')
const http = require('http')
const path = require('path');
const session = require('express-session');
const app = express();
const mysql = require('mysql');
const cors = require('cors');
let bodyParser = require("body-parser");
let connection = mysql.createConnection({
      host     : '34.134.145.55',
      user     : 'root',
      password : 'Janvi@123',
      database : 'csci5410'
});

connection.connect();
global.db = connection;

app.set('port', process.env.PORT || 5000);
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'))
app.use(cors())

app.post('/logout', db.findActiveUser);

app.listen(5000)
console.log("Server started...")