import sys
import random
import argparse

parser = argparse.ArgumentParser(description='API Spec Generator')
parser.add_argument('--language', default="python", help='Language to generate for: python or golang')
parser.add_argument('--num', default=10, help='Number of specs to generate')
args = parser.parse_args()

if args.language not in ["python", "golang"]:
    print('Language must be set to "python" or "golang"')
    sys.exit(1)

words_fd = open("/usr/share/dict/words", "r")
all_words = words_fd.readlines()
all_words = [word.strip() for word in all_words]

# req/s, SLO, SLI calculation window
req_per_s = [1, 5, 10]
slos = [0.9] + 2*[0.99] +  4*[0.999] + 4*[0.9999]
windows=[30]
verbs=["GET", "POST"]

num_api_specs = args.num

for i in range(num_api_specs):
    name = random.choice(all_words)
    email_name = random.choice(all_words)
    email_domain = random.choice(all_words)
    api_resource = random.choice(all_words)
    verb = random.choice(verbs)
    req_s = random.choice(req_per_s)
    slo = random.choice(slos)
    window = random.choice(windows)
    if args.language == "python":
        print('ApiSpec({}, ' + '"{}", "{}@{}.com", "{}", "/api/v1/{}", {}, {:.5f}, {})'.format(name, email_name, email_domain, verb, api_resource, req_s, slo, window))
    elif args.language == "golang":
        print('{} {}@{}.com {} /api/v1/{} {} {:.5f} {}'.format(name, email_name, email_domain, verb, api_resource, req_s, slo, window))

