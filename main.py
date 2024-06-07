import os
import json
import sys
import boto3

print('import libraries successfully')


prompt = '''

    you are a smart assistant so please let me know what is the machine learning in a smartest way ?

'''

bedrock = boto3.client(service_name='bedrock-runtime')

payload = {
    
    
}

body = json.dumps(payload)
model_id = "meta.llama2-70b-chat-v1"

response = bedrock.invoke_model(
    body=body,
    model_id = model_id,
    accept='application/json',
    content_type = 'application/json'
)

response_body = json.loads(response.get("body").read())
respones_text = response_body['generation']
print(respones_text)