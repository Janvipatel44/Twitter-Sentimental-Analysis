import boto3


def s3_client():
    """
        Function: get s3 client
         Purpose: get s3 client
        :returns: s3
    """
    session = boto3.session.Session()
    client = session.client('s3')
    """ :type : pyboto3.s3 """
    return client


def s3_upload_small_files(inp_file_name, s3_bucket_name, inp_file_key):
    client = s3_client()
    s3_bucket_create_response = client.upload_file(inp_file_name, s3_bucket_name, inp_file_key)
    print(f" ** Successfully file upload done - {s3_bucket_create_response} ")


for i in range(1, 299):
    file = i
    if i < 10 :
        file = "0" + str(i);
    inp_file_name = "D:/Study D/Dalhousie/Sem 3/Serverless/Assignments/Assignment 4/Dataset/Train/0" + str(file) + ".txt";
    inp_file_key = str(file) + ".txt"
    s3_bucket_name = "sourcedatab00863421"
    s3_upload_small_files(inp_file_name, s3_bucket_name, inp_file_key)


for i in range(300, 401):
    inp_file_name = "D:/Study D/Dalhousie/Sem 3/Serverless/Assignments/Assignment 4/Dataset/Test/" + str(file) + ".txt";
    inp_file_key = str(file) + ".txt"
    s3_bucket_name = "sourcedatab00863421"
    s3_upload_small_files(inp_file_name, s3_bucket_name, inp_file_key)
