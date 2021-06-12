exports.findActiveUser = function (request, response) {
    let data = request.body
    message = '';
    let sqlCommand = "Select * from acti INNER JOIN userDetails ON userState.userId = userDetails.userId;"
    let query = db.query(sqlCommand, function(error, result) {
        return response.status(200).json({result: result})
    })
}

exports.logout = function (request, response) {
    request.session.cookie.token = '';
    return response.status(200).json()
}