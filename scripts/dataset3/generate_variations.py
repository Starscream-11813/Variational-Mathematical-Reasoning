
import csv
import openai
import openai.error
import backoff
import argparse
import time
from tqdm import tqdm

key_s = "<API-KEY>"
key_z = "<API-KEY>"

prompt1 = "Generate 5 rephrased variations of this problem by changing the sentence structure and occasionally changing the object names. "

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.APIConnectionError))
def gen_variations(problem: str):
    prompt = f"{problem}\n{prompt1}"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a Math Word Problem rephraser that generates variations of Math Word Problems."},
                {"role": "user", "content": prompt}
        ]
    )
    response = completion['choices'][0]['message']['content']
    return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('idsfile', help='file containing list of ids to rephrase for')
    parser.add_argument('outfile', help='file to output rephrased variations to')
    parser.add_argument('key', help='which api key to use ("s" for mine, "z" for zarif\'s)')
    parser.add_argument('start', help='which id to start *after*')
    parser.add_argument('end', help='which id to end *at*')

    args = parser.parse_args()

    idsfile = open(args.idsfile, "r")
    outfile = open(args.outfile, "a")

    if args.key == 's':
        openai.api_key = key_s
    elif args.key == 'z':
        openai.api_key = key_z
    
    ids = set()
    for line in idsfile:
        ids.add(int(line))
    
    startid = int(args.start)
    endid = int(args.end)

    f = open('paramawps-id-corrected.csv')
    data = csv.reader(f)
    header = next(data)

    for row in tqdm(data):
        row_id = int(row[0])
        st_time = time.time()
        if row_id in ids and row_id > startid and row_id <= endid:
            # print(row_id)
            outfile.write(f"--- {row_id}\n")
            outfile.write(str(row_id) + '\n')
            v = gen_variations(row[1])
            outfile.write(v)
            outfile.write('\n')
            outfile.flush()
            ed_time = time.time()
            if (ed_time - st_time < 3):
                time.sleep(9 - (ed_time - st_time))

