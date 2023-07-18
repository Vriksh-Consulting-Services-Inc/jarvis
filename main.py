import os, openai, requests


def chat_with_gpt(request):
    
    #request_json = request #request.get_json()
    request_json = request.get_json()
    message = request_json['message'] if 'message' in request_json else 'Tell me a unique, random fact in less than 50 words.'
    chat_context = request_json['chat_context'] if 'chat_context' in request_json else 'You are a helpful assistant named Jarvis'
    api_key = request_json['token'] if 'token' in request_json else None
    MODEL = request_json['token'] if 'model' in request_json else 'gpt-3.5-turbo'

    response = 'You must pass an Open API key under token parameter.'

    if api_key:
        openai.api_key = api_key
        
        messages=[
            {"role": "system", "content": chat_context},
            {"role": "user", "content": message}
        ]
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            max_tokens=100,
            temperature=0.7,
            top_p=1.0,
        )
        response = response['choices'][0]['message']['content']
    
    return response
    


# def handleWebhook(request):
#     req = request.get_json()
#     print(req)

#     responseText = ""
#     intent = req["queryResult"]["intent"]["displayName"]

#     if intent == "Default Welcome Intent":
#         #responseText = "Hello from a GCF Webhook"
#         responseText = chat_with_gpt(request)
#     elif intent == "get-agent-name":
#         responseText = "My name is Flowhook"
#     else:
#         responseText = f"There are no fulfillment responses defined for Intent {intent}"
    
#     message = {'message': req['queryResult']['queryText']}
#     responseText = chat_with_gpt(message)
#     print({'message': message, 'response': responseText})

#     # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
#     res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

#     return res

