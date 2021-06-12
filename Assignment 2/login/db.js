exports.login = function (request, response) {
  message = '';
  let data = request.body;
  console.log('here');
  console.log(data.loginId);
  console.log(data.password);
  let sqlCommand = "select * from register_user(userName, password) where userName = '" + data.loginId + "' and password = '" + data.password + "')";
  let query = db.query(sqlCommand, function (error, result) {
    if(result){
    message = "Succesfull! User login successful.";
    return response.status(200).json({result: message})
    }
    else{
      message = "UnSuccesfull! User login can not be performed.";
      return response.status(300).json({result: message})
    }
  });  
};
