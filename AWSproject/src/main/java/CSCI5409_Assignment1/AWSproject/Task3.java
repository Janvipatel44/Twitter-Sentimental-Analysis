package CSCI5409_Assignment1.AWSproject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.S3Object;

public class Task3 
{
	//configuration details for JDBC connection
    private static String driverName = "com.mysql.cj.jdbc.Driver";   
    private static String database = "jdbc:mysql://task3database.cfprz1ccsmta.ap-south-1.rds.amazonaws.com:3306/aws_testing?user=janvi&password=janvi123";
    private static String username = "janvi";
    private static String password = "janvi123*";
    private static Connection connection;
   
    //establish connection with database
    protected static Connection getConnection(String database,String username,String password)
    {
        try 
        {
            Class.forName(driverName);
            try
            {
                 connection = DriverManager.getConnection(database, username, password);		//connecting to database
            } 
            catch (SQLException ex) 
            {
                  System.out.println("Failed to create the database connection."); 
            }
        } 
        catch (ClassNotFoundException ex) 
        {
            System.out.println("Driver not found."); 
        }
        return connection;
    }	
	
    //performs insert, encryption, decryption and select operation 
    public static void main(String[] args) throws IOException 
	{
		connection = getConnection(database,username,password);
		if (connection != null) 
		{
	        java.sql.Statement stmt;
	        try
			{
				 stmt = connection.createStatement();
			     System.out.println("\nConnection established successfully !!");

			     //bucket and key name to read from lookup file
		         String bucketName = "csci5410-task2-bucket2";
		         String	key = "Lookup5410";
		         
		         //user name and password to insert into database
		         String UserID = "janvi";
		         String user_password = "jan";
		         
		         System.out.print("\nPassword before encryption:" +user_password);

		         //hash maps to store encryption and decryption letters
		         HashMap<String, String> LookupEncryption = new HashMap<String, String>();
		         HashMap<String, String> LookupDecryption = new HashMap<String, String>();
		         
				 /********* Password Encryption **********/
		         
		         //reading from file located at AWS S3
		         @SuppressWarnings("deprecation")
				 AmazonS3 s3Client = new AmazonS3Client(new ProfileCredentialsProvider());        
		         S3Object object = s3Client.getObject(new GetObjectRequest(bucketName, key));
		         InputStream objectData = object.getObjectContent();
		         BufferedReader reader = new BufferedReader(new InputStreamReader (objectData));  
		         
		         //splitting the file content and storing the data into lookup encryption hashmap and look up decryption hash map
		         String readLine = reader.readLine();
		         while(readLine!=null) 
		         {	 
		        	 String[] ary = readLine.split("	");
		        	 LookupEncryption.put(ary[0], ary[1]);
		        	 LookupDecryption.put(ary[1], ary[0]);
		        	 readLine = reader.readLine();
		         }
		         
		         String encryptedPassword = "";

		         //generating encrypted password
		         for(int i = 0; i<user_password.length(); i++)
		         {
		        	 encryptedPassword += LookupEncryption.get(String.valueOf(user_password.charAt(i)));
		         }
		         System.out.print("\nEncripted Password:" +encryptedPassword);
		         
				 /********* Inserting user details into database **********/
		         String sqlquery = " INSERT INTO userDetails(UserID,Password) VALUES ('"+UserID+"', '"+encryptedPassword+"');"; 
				 if(stmt.executeUpdate(sqlquery) == 1)
				 {
			         System.out.print("\nSuccessful insertion into database");
				 }
				
				 /********* displaying password for a particular userID**********/
				 String sqlselect = "SELECT Password from userDetails where userDetails.UserID = '"+UserID+"';"; 
				 String decryptedPassword = "";
				 String passwordDatabase = "";

				 //getting password from result set
				 ResultSet rs = stmt.executeQuery(sqlselect);
		         while(rs.next())
		         {
		        	 passwordDatabase =  rs.getString("Password");
		         }
		         
		         //decryption of password
		         for(int i = 0; i<passwordDatabase.length(); i++)
		         {
		        	 decryptedPassword += LookupDecryption.get(String.valueOf(passwordDatabase.charAt(i))+String.valueOf(passwordDatabase.charAt(i+1)));
		        	 i++;
		         }
		         System.out.print("\nSelecting userdetails with userID :" +UserID);
		         System.out.print("\n\tUserID:" +UserID);
		         System.out.print("\n\tDecripted Password:" +decryptedPassword);
		         objectData.close();
			} 
        	catch (SQLException e) 
	        {
				e.printStackTrace();
			}
		}
	}
}