import json

with open('synack.json') as f:
    data = json.load(f)

for record in data['records']:
    with open("clean.json", "w") as outfile:
        outfile.write(record['domain'])
    # print(record['domain'])
