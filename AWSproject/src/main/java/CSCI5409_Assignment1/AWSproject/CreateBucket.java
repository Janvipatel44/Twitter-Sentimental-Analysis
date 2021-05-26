package CSCI5409_Assignment1.AWSproject;

import java.io.IOException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AmazonS3Exception;

public class CreateBucket {

	public static void main(String[] args) throws IOException 
	{
        //connection with AWS s3 using region East 1 and the configurations provided in local folder
	    final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();

	    //variable declaration for bucket name
	    String bucketName = "csci5410-task2-bucket2";
	    
	    if (s3.doesBucketExistV2(bucketName))	//checking if bucket already exist
	    {
	        System.out.format("Bucket %s already exists.\n", bucketName);
	    } 
	    else 
	    {
	        try 
	        {
	            s3.createBucket(bucketName);		//creating new bucket using createBucket function
	        	System.out.println("Successfully bucket creation!");
	        }
	        catch (AmazonS3Exception e) 	//exception handling
	        {
	        	System.out.println("Error while creating bucket!");
	            System.err.println(e.getErrorMessage());
	        }
	    }
	 }
}