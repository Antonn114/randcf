import argparse
import os
import json
import requests
import time
import random

# Parsing default variables

# default settings the first time the user starts the script. Changing this dict doesn't change randcf_settings.json

settings = {
    "min": 800,
    "max": 1400,
    "n": 5,
    "user": ""
}

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if not os.path.exists(os.path.join(__location__, "randcf_settings.json")):
    f = open(os.path.join(__location__, "./randcf_settings.json"), "w")
    f.write(json.dumps(settings, indent=4))
    f.close()

f = open(os.path.join(__location__, "randcf_settings.json"), 'r+')
settings = json.load(f)

if len(settings['user']) < 1:
    settings['user'] = input('What is your Codeforces username? ')
    print("Welcome, {}!".format(settings['user']))

    user_info = requests.get('https://codeforces.com/api/user.info?handles={}'.format(settings['user']))
    if (user_info.json()['status'] != 'OK'):
        raise Exception('Requesting user failed.')

    f.seek(0)
    f.write(json.dumps(settings, indent=4))

f.close()

# Fetching finished problems

user_status = requests.get('https://codeforces.com/api/user.status?handle={}'.format(settings['user']))
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
parser.add_argument('-m', '--min', type=int, default=settings['min'], help='Set minimum rating of problem (s)')
parser.add_argument('-M', '--max', type=int, default=settings['max'], help='Set maximum rating of problem (s)')
parser.add_argument('-n', type=int, default=settings['n'], help='Number of problem(s) to show')
parser.add_argument('-t', '--tags', type=str, nargs='*', help="Set tags and remove problems without any of the provided tags")
parser.add_argument('--strict', action='store_true', help="Remove problems without any of the provided tags")
args = parser.parse_args()

# Parsing problems

r = requests.get('https://codeforces.com/api/problemset.problems')
content = r.json()

if content['status'] != 'OK':
    raise Exception('Requesting problemset failed.')

contest_r = requests.get('https://codeforces.com/api/contest.list?gym=false')
contest_r_json = contest_r.json();

if contest_r_json['status'] != 'OK':
    raise Exception('Requesting contests failed.')

april_fools_contests = []

for i in contest_r_json['result']:
    if "April Fools" in i['name']:
        april_fools_contests.append(i['id'])

problems = []

for i in content['result']['problems']:
    if 'rating' not in i:
        continue
    if 'tags' not in i:
        continue
    if '*special' in i['tags']:
        continue
    if i['contestId'] in april_fools_contests:
        continue
    if not i['rating'] in range(args.min, args.max + 1):
        continue
    if str(i['contestId']) + i['index'] in AC_problems:
        continue
    
    if args.tags is not None:
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