import csv
import openai
import openai.error
import backoff
import argparse
import time
from tqdm import tqdm
import sys

key = "<API-KEY>"

prompt1 = "Solve the given Math Word Problem:\n"

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.APIConnectionError))
def gen_solutions(problem: str):
    prompt = f"{problem}\n{prompt1}" + " Output in the format \'Answer: <number>'"
    completion = openai.Completion.create( #ChatCompletion, Completion
        model="text-babbage-001",
        temperature=0,
        prompt=prompt
    )
    response = completion['choices'][0].text
    # response = completion['choices'][0]['message']['content']
    return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('idsfile', help='file containing list of ids to rephrase for')
    parser.add_argument('outfile', help='file to output rephrased variations to')
    # parser.add_argument('key', help='which api key to use ("s" for mine, "z" for zarif\'s)')
    parser.add_argument('start', help='which line to start after')
    parser.add_argument('end', help='which line to end at')

    args = parser.parse_args()

    # idsfile = open(args.idsfile, "r")
    outfile = open(args.outfile, "a")
    # outfile = sys.stdout

    openai.api_key = key

    startid = int(args.start)
    endid = int(args.end)

    f = open('paramawps.csv')
    data = csv.reader(f)
    header = next(data)

    row_ctr = 1

    for row in data:
        # print(row_ctr, startid, endid)
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
