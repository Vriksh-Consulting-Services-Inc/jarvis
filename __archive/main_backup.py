# %%
import openai, os, requests

openai.api_key = os.getenv('OPENAI_API_KEY')
bard_api_key = os.getenv('BARD_API_KEY')

MODEL = "gpt-3.5-turbo"
PROMPT = "Tell me a unique AI related joke"

def chat_with_gpt_v2(prompt):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
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

def chat_with_bard(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={bard_api_key}"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": {"text": prompt}}
    response = requests.post(url, headers=headers, data=data)
    return response.json()


def chat(ai,prompt):
    response = 'error'
    if ai=='gpt':
        response = chat_with_gpt(prompt)
    elif ai=='bard':
        response = chat_with_bard(prompt)
    return response

response_gpt = ''
response_gpt = chat('gpt',PROMPT)
response_bard = ''
response_bard = chat('bard',PROMPT)

print(response_gpt)
print(response_bard)

# %%
