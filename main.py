import os, openai, requests

openai.api_key = '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'

MODEL = "gpt-3.5-turbo"
PROMPT = "Tell me a dad joke"

def chat_with_gpt(request):
    request_json = request.get_json()
    message = request_json['message']
    
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
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
    
    # Return the reply in the response
    return {'reply': reply}
