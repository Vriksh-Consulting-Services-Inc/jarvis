Vriksh Jarvis


gcloud functions deploy vriksh-jarvis-v1 --runtime python310 --trigger-http --allow-unauthenticated --entry-point chat_with_gpt


export OPENAI_API_TOKEN=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
functions-framework --target=chat_with_gpt --port=8080

curl -m 70 -X POST https://us-central1-prag-2019.cloudfunctions.net/vriksh-jarvis-v1 \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{"message":"Tell me a 10 worded horror story"}'