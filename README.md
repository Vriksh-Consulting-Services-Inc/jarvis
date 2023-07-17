Vriksh Jarvis

gcloud functions deploy vriksh-jarvis-v1 --runtime python310 --trigger-http --allow-unauthenticated --entry-point handleWebhook


export OPENAI_API_TOKEN=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
functions-framework --target=chat_with_gpt --port=8080

curl -m 70 -X POST https://us-central1-prag-2019.cloudfunctions.net/vriksh-jarvis-v1 \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{"message":"Tell me a 10 worded horror story"}'


export OPENAI_API_TOKEN=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
functions-framework --target=chat_with_gpt --port=8080

curl -m 70 -X POST https://us-central1-prag-2019.cloudfunctions.net/vriksh-jarvis-v1 \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{"message":"Tell me a 10 worded horror story"}'


curl -m 70 -X POST https://us-central1-prag-2019.cloudfunctions.net/vriksh-jarvis-v1 \
-H "Content-Type: application/json" \
-d '{}'


curl -H "Content-Type: application/json; charset=utf-8"  -H "Authorization: Bearer ya29.a0AbVbY6Obr59n8Ty-M0m3RYR2YRHyJPag_EUTDHoTNrYzfs1DwoqRdAecn9IrQoUYnPOonrbbV4oxqc3rX4bcCtzFF0NdPfbteLXlDiDL9macGqDnNyP86fgFDysjV8tAXacjyh1S6G3feTAbWtXKa0fFVk7UG-6Oi1W33beRnyuDJBnWCk0QasY7RZVuRQstZ_o9nR5JexDArYCTxkw6NAiJfRqL9clw1Mhn0rYkpVSVh03yqZFXvs0f_4risxIYN3qY0r0fLI23RiNAJVigyvaxTfAALhDbsS1hSoW6ojJYaXmdVyOGKhkpkyEFGkx7QWT0wYM3Iv49OwyRJTrpIjxEmiLQWHVjRrnrQpPVm7vUXemRcnGaRkDznz5A56sk7aNBmMTnO8cxj9cI9PjKL4trcsEgvw_aaCgYKAYQSAQ4SFQFWKvPlvOp1FCJ9zjrXETQB4HcW7Q0423"  -d "{\"queryInput\":{\"text\":{\"text\":\"Hey Jarvis, what color is the sky?\",\"languageCode\":\"en\"}},\"queryParams\":{\"source\":\"DIALOGFLOW_CONSOLE\",\"timeZone\":\"America/Moncton\"}}" "https://dialogflow.googleapis.com/v2beta1/projects/vriksh-jarvis-63484/locations/global/agent/sessions/41e20c9e-f067-5878-7c19-b83543ce253e:detectIntent"