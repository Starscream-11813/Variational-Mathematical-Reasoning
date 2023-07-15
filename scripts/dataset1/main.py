#!/bin/python

import sys
import json
import argparse

from pprint import pprint

def main(args):
    jsondata = parse_json(args.inputfile)
    # pprint(jsondata[0])
    # print(jsondata[0]['sQuestion'])
    for i in jsondata:
        print(i['sQuestion'] + '\n')

def parse_json(jsonfile : str):
    jsondata = None
    if jsonfile == "-":
        jsondata = json.loads(sys.stdin.read())
    else:
        with open(jsonfile, "r") as f:
            jsondata = json.load(f)
    return jsondata

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    args = parser.parse_args()
    main(args)
