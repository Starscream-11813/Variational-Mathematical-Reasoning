
import openai

openai.api_key = "<API-KEY>"

problem1 = "A pet shelter had 9 puppies when another 12 were brought in . " \
           "If 3 puppies a day are adopted , how long would it take for all of them to be adopted ?"

problem = problem1

prompt1 = f"\"{problem}\" \nGenerate 5 rephrased variations of this problem by" \
        "changing the sentence structure and occasionally changing the object names. "
prompt2 = prompt1 + "Also add other related information to the problem that is not " \
        "related to solving the problem. "

promptend = ""

prompt = prompt1 + promptend

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a Math Word Problem rephraser that generates variations of Math Word Problems."},
        {"role": "user", "content": prompt}
    ]
)

response = completion['choices'][0]['message']['content']
usage = completion['usage']

print(response)

# print(usage)
