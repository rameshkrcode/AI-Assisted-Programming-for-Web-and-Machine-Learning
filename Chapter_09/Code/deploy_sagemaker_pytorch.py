import boto3
s3 = boto3.client('s3')
from sagemaker.pytorch import PyTorchModel
pytorch_model = PyTorchModel(
    model_data="s3://your-bucket/model/model.tar.gz",
    entry_point= "inference.py",
    role="arn:aws:iam::123456789012:role/SageMakerExecutionRole",
    framework_version= "1.12",
    py_version="py38"
)
predictor = pytorch_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large"
)
response = predictor.predict({"input": [1.2, 3.4, 5.6]})
print(response)
