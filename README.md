# MiniSedric

This project creates AWS infrastructure to provide a transcription service.

## Prerequisites

Before deploying to AWS, ensure you have the following:

- Terraform installed
- AWS credentials set up

## Infrastructure Deployment

This project uses Terraform to deploy the full infrastructure.

### Set AWS Credentials

Before deploying to AWS, provide your AWS credentials like this:

```sh
export AWS_ACCESS_KEY_ID='your_aws_key_id'
export AWS_SECRET_ACCESS_KEY='your_aws_secret_access_key'
```

### Deploy Services

To deploy all services to AWS, run these commands:

```sh
terraform init
terraform apply
```

### Destroy Services

To remove these services, you can use this command:

```sh
terraform destroy
```

## Execute Transcription

To execute the transcription function, send an API request to:

```
https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/transcribe
```

### Request Payload

Use the following payload where interaction_url is a link to an mp3 file uploaded to S3 storage:

```json
{
    "interaction_url": "s3://..."
}
```

### Example Payload

Here is an example payload:

```json
{
    "interaction_url": "s3://minisedric-transcribe-bucket/my_way.mp3"
}
```