import json

with open('synack.json') as f:
    data = json.load(f)

for record in data['records']:
    with open("clean.json", "w") as outfile:
        outfile.write(record['domain'])
    # print(record['domain'])
# I think i need to change this to a while loop
# right now I am only outputting the last entry of the file that is being read in.
