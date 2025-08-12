model.save("ecommerce_model")
import boto3
s3 = boto3.client('s3')
s3.upload_file("ecommerce_model/saved_model.pb", "mybucket", "models/ecommerce_model/saved_model.pb")
