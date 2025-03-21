import os
import openai

client = openai.OpenAI(
  api_key="tgp_v1_0pEQUl6E9MOCJusjE1wo_syohmHqt9NlUzsjXwkMEK0",
  base_url="https://api.together.xyz/v1",
)

response = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-R1",
  messages=[{"role": "user", "content": "Hello, world!"}],
)
print(response)