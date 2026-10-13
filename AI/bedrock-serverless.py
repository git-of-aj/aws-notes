import boto3

# Uses your configured AWS credentials and default Region.
client = boto3.client("bedrock-runtime")

model_id = "amazon.nova-micro-v1:0" # search > click > get modelID

response = client.converse(
    modelId=model_id,
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "Explain AWS Bedrock in one sentence."}
            ],
        }
    ],
    inferenceConfig={
        "maxTokens": 200,
        "temperature": 0.3,
    },
)

answer = response["output"]["message"]["content"][0]["text"]
print(answer)
