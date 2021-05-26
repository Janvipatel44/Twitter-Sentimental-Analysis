package CSCI5409_Assignment1.AWSproject;

import java.io.IOException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.PublicAccessBlockConfiguration;
import com.amazonaws.services.s3.model.SetPublicAccessBlockRequest;

public class BlockFileAccess {

	public static void main(String[] args) throws IOException 
	{
	    
		//variable declaration for bucket name
	    String bucketName = "csci5410-task2-bucket2";
	   
        //connection with AWS s3 using region East 1 and the configurations provided in local folder
		final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();
	    
		//blocking public access
    	s3.setPublicAccessBlock(new SetPublicAccessBlockRequest().withBucketName(bucketName)
    															.withPublicAccessBlockConfiguration(new PublicAccessBlockConfiguration()
										    					.withBlockPublicAcls(true)
										    					.withIgnorePublicAcls(true)
										    					.withBlockPublicPolicy(true)
										    					.withRestrictPublicBuckets(true)));
    	
    	System.out.print("Successfully blocked permission");
	 }
}
