import json
from datetime import datetime
from urllib.parse import urlparse

import boto3


def lambda_handler(event: dict, context) -> dict:
    transcribe = boto3.client("transcribe", region_name="us-east-1")

    request = json.loads(event["body"])
    job_uri = request.get("interaction_url")
    if not job_uri:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Parameter `interaction_url` is required!"}),
        }

    url = urlparse(job_uri, allow_fragments=False)
    bucket_name = url.netloc
    job_name = f"{url.path[1:]}_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"

    response = transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": job_uri},
        MediaFormat="mp3",
        LanguageCode="en-US",
        OutputBucketName=bucket_name,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Transcription job started",
                "TranscriptionJobName": response["TranscriptionJob"]["TranscriptionJobName"],
            }
        ),
    }
