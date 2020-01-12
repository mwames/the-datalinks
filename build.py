import os
import json

entries = os.listdir(path='techs')
techs = []

for entry in entries:
  with open('techs/'+ entry) as tech:
    data = json.load(tech)
    data['filename'] = os.path.splitext(entry)[0]
    techs.append(data)

with open('all_techs.json', 'w') as outfile:
  json.dump(techs, outfile)

print('================== ALL DONE ==================')