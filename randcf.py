import argparse
import os
import json
import requests
from numpy import random
import time

r = requests.get('https://codeforces.com/api/problemset.problems')
content = r.json()

if content['status'] != 'OK':
    raise Exception('Requesting problemset failed.')

# Parsing default variables

default_min = 800
default_max = 1400
default_num = 5
default_username = ''

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if not os.path.exists(os.path.join(__location__, "randcf_settings.txt")):
    f = open(os.path.join(__location__, "./randcf_settings.txt"), "w")
    f.write("min={}\nmax={}\nnum={}\nusr={}".format(default_min, default_max, default_num, default_username)) 
    f.close()

f = open(os.path.join(__location__, "randcf_settings.txt"), "r+")
default_min = int(f.readline()[4:])
default_max = int(f.readline()[4:])
default_num = int(f.readline()[4:])
default_username = f.readline()[4:].strip()

if len(default_username) < 1:
    default_username = input('What is your Codeforces username? ')
    print("Welcome, {}!".format(default_username))
user_info = requests.get('https://codeforces.com/api/user.info?handles={}'.format(default_username))
if (user_info.json()['status'] != 'OK'):
        raise Exception('Requesting user failed.')
f.seek(0)
f.write("min={}\nmax={}\nnum={}\nusr={}".format(default_min, default_max, default_num, default_username))
f.close()

# Parsing finished problems

user_status = requests.get('https://codeforces.com/api/user.status?handle={}'.format(default_username))
submissions = user_status.json()

if submissions['status'] != 'OK':
    raise Exception('Requesting user submissions failed.')
AC_problems = []
for i in user_status.json()['result']:
    if i['verdict'] != 'OK':
        continue
    AC_problems.append(str(i['problem']['contestId']) + i['problem']['index'])

# Parsing arguments

parser = argparse.ArgumentParser(prog='randrc', description="Return random problem(s) from Codeforces.com",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-m', '--min', type=int, default=default_min, help='Set minimum rating of problem (s)')
parser.add_argument('-M', '--max', type=int, default=default_max, help='Set maximum rating of problem (s)')
parser.add_argument('-n', type=int, default=default_num, help='Number of problem(s) to show')
parser.add_argument('-t', '--tags', type=str, nargs='*', help="Set tags and remove problems without any of the provided tags")
parser.add_argument('--strict', action='store_true', help="Remove problems without any of the provided tags")
args = parser.parse_args()

# Parsing problems

problems = []

for i in content['result']['problems']:
    if 'rating' not in i:
        continue
    if not i['rating'] in range(args.min, args.max + 1):
        continue
    x = str(i['contestId']) + i['index']
    if x in AC_problems:
        continue
    if args.tags is not None:
        if 'tags' not in i:
            continue
        if args.strict:
            flag = False
            for j in args.tags:
                if not j in i['tags']:
                    flag = True
                    break
            if flag:
                continue
        else:
            flag = True
            for j in args.tags:
                if j in i['tags']:
                    flag = False
                    break
            if flag:
                continue
    problems.append(i)

if len(problems) < 1:
    print("No problems found under given parameters!")

# Choosing random problems

random.seed(int(time.time()))
random.shuffle(problems)
for i in range(min(args.n, len(problems))):
    print('{}. {}'.format(i + 1, problems[i]['name'].ljust(50)), end = '')
    print('rating:', str(problems[i]['rating']).ljust(10), end='')
    print('tags: ', end = '')
    flag = False
    for j in problems[i]['tags']:
        if flag:
            print(', ', end = '')
        print(j, end = '')
        flag = True
    print()
    print()
    print('\tlink: https://codeforces.com/problemset/problem/{}/{}'.format(problems[i]['contestId'], problems[i]['index']))
    print()


