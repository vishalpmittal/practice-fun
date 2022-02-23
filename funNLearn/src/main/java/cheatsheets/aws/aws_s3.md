
aws s3api get-object-acl --bucket my-bucket --key index.html

aws s3api put-object --bucket destination_awsexamplebucket --key dir-1/my_images.tar.bz2 --body my_images.tar.bz2 --acl bucket-owner-full-control


boto3.resource('s3').ObjectAcl('S3BUCKETNAME', account_id + "_" + date_fmt + ".json").put(ACL='bucket-owner-full-control')



aws s3 cp ./hello_world s3://bt2-test-ctindall/put_by_staging --profile cuda-essstaging --acl bucket-owner-full-control


aws s3 cp vmittal-test.json s3://sentinel-forensics-billing-data-staging1/vmittal-test.json --profile AWSGlueServiceRole-DefaultRole --acl bucket-owner-full-control


[profile vmittalglueprofile]
role_arn = arn:aws:iam::737024935095:role/service-role/AWSGlueServiceRole-DefaultRole
source_profile = vmittal

aws s3 cp vmittal-test.json s3://sentinel-forensics-billing-data-staging1/vmittal-test.json --profile vmittalglueprofile --acl bucket-owner-full-control