import csv
import openai
import openai.error
import backoff
import argparse
import time
from tqdm import tqdm
import sys

key_s = "<API-KEY>"
key_z = "<API-KEY>"
key_sir = "<API-KEY>"

prompt1 = "Solve the given Math Word Problem:\n"

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.APIConnectionError))
def gen_solutions(problem: str):
    prompt = f"{problem}\n{prompt1}" + " Only output the resulting number in a single line, no other sentences will be output."
    completion = openai.ChatCompletion.create( #ChatCompletion, Completion
        # model="text-davinci-002",
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a Math Word Problem solver that outputs the final answer of Math Word Problems in the format: \"Answer: [ANS]\", where [ANS] is the answer."},
                {"role": "user", "content": prompt}
        ]
    )
    # response = completion['choices'][0].text
    response = completion['choices'][0]['message']['content']
    return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('idsfile', help='file containing list of ids to rephrase for')
    parser.add_argument('outfile', help='file to output rephrased variations to')
    parser.add_argument('key', help='which api key to use ("s" for mine, "z" for zarif\'s)')
    parser.add_argument('start', help='which line to start after')
    parser.add_argument('end', help='which line to end at')

    args = parser.parse_args()

    # idsfile = open(args.idsfile, "r")
    outfile = open(args.outfile, "a")
    # outfile = sys.stdout

    if args.key == 's':
        openai.api_key = key_s
    elif args.key == 'z':
        openai.api_key = key_z
    elif args.key == 'sir':
        openai.api_key = key_sir

    startid = int(args.start)
    endid = int(args.end)

    f = open('paramawps.csv')
    data = csv.reader(f)
    header = next(data)

    row_ctr = 1

    for row in data:
        row_ctr += 1
        if (row_ctr < startid):
            next(data)
            continue
        if (row_ctr > endid):
            break
        row_id = int(row[0])
        st_time = time.time()

        print(f"--- {row_ctr} {row_id}")
        outfile.write(f"--- {row_ctr} {row_id}\n")
        v = gen_solutions(row[1])
        outfile.write(v)
        outfile.write('\n')
        outfile.flush()
        ed_time = time.time()

        # if (ed_time - st_time < 20):
        #     time.sleep(20 - (ed_time - st_time))
