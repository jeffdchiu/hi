from openai import OpenAI
#client = OpenAI()
client = OpenAI(
 api_key='OPENAI_API_KEY',
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": " I am 59  years old. My gender is male. My height is 178.81 cm tall and my weight is 96.36 kg. I have Allergy to tree pollen. My Body Mass Index is 25. Provide me 1 meal plan"}
  ]
)

print(completion.choices[0].message)
