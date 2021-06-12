exports.register = function (request, response) {
  message = '';
  let data = request.body;
  let sqlCommand = "Insert into register_user(userName, emailId, topic, password) values ('" + data.username + "','" +
                    data.email + "','" + data.password + "','" + data.topic + "')";
  let query = db.query(sqlCommand, function (error, result) {
      sqlCommand = "Insert into activate_user (loginId, activateUser) values ('" + result.username + "', 'offline');"
      db.query(sqlCommand);
      message = "Succesfull! Your account has been created.";
      return response.status(444).json({result: message})
  });  
};