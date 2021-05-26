package CSCI5409_Assignment1.AWSproject;

import java.io.IOException;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AccessControlList;
import com.amazonaws.services.s3.model.CanonicalGrantee;
import com.amazonaws.services.s3.model.Grant;
import com.amazonaws.services.s3.model.Permission;

public class ACLFullFileControl 
{
	public static void main(String[] args) throws IOException 
	{	    
		//variable declaration for bucket name
	    String bucketName = "csci5410-task2-bucket2";
	   
        //connection with AWS s3 using region East 1 and the configurations provided in local folder
		final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();
		    
		final AccessControlList aclcontrol = s3.getBucketAcl(bucketName);	

		//grant all permissions
		aclcontrol.grantAllPermissions(new Grant(new CanonicalGrantee(aclcontrol.getOwner().getId()), Permission.FullControl));
        Grant grant1 = new Grant(new CanonicalGrantee(s3.getS3AccountOwner().getId()), Permission.FullControl);

        AccessControlList Bucket = s3.getBucketAcl(bucketName);
        Bucket.grantAllPermissions(grant1);
        s3.setBucketAcl(bucketName, Bucket);  
	}
}