package CSCI5409_Assignment1.AWSproject;

import java.io.IOException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.CopyObjectRequest;
import com.amazonaws.services.s3.model.DeleteObjectRequest;

public class MoveFile 
{
	 public static void main(String[] args) throws IOException 
	 {
		    //variable declaration for bucket name, file path and file name
	        String sourcebucketName = "csci5410-task2-bucket1";
	        String destinationbucketName = "csci5410-task2-bucket2";
	        String sourceKey = "janvi";
	        String destinationKey = "janvi-bucket2";

	        try 
	        {
	            //connection with AWS s3 using region East 1 and the configurations provided in local folder
	            AmazonS3 s3Client = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();

	            // Copy one object from one bucket to another bucket and delete it from source bucket
	            CopyObjectRequest copyObjRequest = new CopyObjectRequest(sourcebucketName, sourceKey, destinationbucketName, destinationKey);
	            s3Client.copyObject(copyObjRequest);
	            s3Client.deleteObject(new DeleteObjectRequest(sourcebucketName, sourceKey));
	        }
	        catch(AmazonServiceException e) {
	            // The call was transmitted successfully, but Amazon S3 couldn't process 
	            // it, so it returned an error response.
	            e.printStackTrace();
	        }
	        catch(SdkClientException e) {
	            // Amazon S3 couldn't be contacted for a response, or the client  
	            // couldn't parse the response from Amazon S3.
	            e.printStackTrace();
	        }
	    }
}
