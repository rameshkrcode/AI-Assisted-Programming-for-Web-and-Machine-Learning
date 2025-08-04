
import openai

openai.api_key = "your-api-key-here"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful data analyst."},
        {"role": "user", "content": "Summarize the dataset insights in plain English."}
    ],
    max_tokens=50
)

print(response.choices[0].message["content"].strip())
