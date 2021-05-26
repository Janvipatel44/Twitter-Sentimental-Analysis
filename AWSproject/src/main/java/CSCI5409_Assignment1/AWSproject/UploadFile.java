package CSCI5409_Assignment1.AWSproject;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import java.io.File;
import java.io.IOException;

public class UploadFile 
{
	 public static void main(String[] args) throws IOException 
	 {
	    //variable declaration for bucket name, file path and file name
        String bucketName = "csci5410-task2-bucket2";
        String filePath = "D:\\Study D\\Dalhousie\\Sem 3\\Serverless\\Assignments\\Assignment 1\\Lookup5410.txt";
        String keyName = "Lookup5410";
        
        System.out.format("Uploading %s.txt to S3 bucket %s...\n", keyName, bucketName);
        
        //connection with AWS s3 using region East 1 and the configurations provided in local folder
        final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();
        
        try 
        {
        	//using put object uploading file present at a particular location in the specific bucket
            s3.putObject(bucketName, keyName, new File(filePath));
        } 
        catch (AmazonServiceException e)		//Exception handling
        {
    	    System.out.println("Error while uploading the file!");
            System.err.println(e.getErrorMessage());
            System.exit(1);
        }
	    System.out.println("Successfully uploaded!");
	 }
}
