import openai

# Set the API key
openai.api_key = "<API-KEY>"

# Set the model to use
model_engine = "text-davinci-003" # gpt 3.5 turbo try kore dekhis eikhane, if it works then great

# Set the prompt for the model

problem1 = "If there are 41 short plants and 44 tall plants in the park, and " \
          "park workers are planting 57 short plants today, how many short " \
          "plants will the park have when the workers are finished?"

problem2 = "A pet shelter had 9 puppies when another 12 were brought in . " \
          "If 3 puppies a day are adopted , how long would it take for all of them to be adopted ?"

problem = problem2

prompt1 = f"Paraphrase the math word problem \"{problem}\" in 5 different ways by changing the sentence structure and occasionally changing the object names."
prompt2 = f"Paraphrase the math word problem \"{problem}\" in 5 different ways. Incorporate a sentence containing irrelevant numerical information disguised as relevant to the problem statement."
prompt3 = f"Solve the math word problem \"{problem}\". Then rephrase the problem by reversing the question to ask for a value already given in the original question."
prompt3_2 = f""

prompt2a = "Add some extra information to the problem statement."

prompt = []
prompt.append(prompt1)
# prompt.append(prompt1+prompt2a)
# prompt.append(prompt3_2)

for p in prompt:
  print('--------')
  # Generate a response from the model
  completion = openai.Completion.create(engine=model_engine, prompt=p, max_tokens=1024, n=1, stop=None, temperature=0.7)
  response = completion.choices[0].text

  # Print the response
  print(response)