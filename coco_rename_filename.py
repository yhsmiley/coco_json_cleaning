import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    annots = json.load(json_file)

images = annots["images"]

for image in images:
    file_name = image["file_name"]

    ## CHANGE FILE RENAME LOGIC HERE
    city = file_name.split('_')[0]
    new_name = f'{city}/{file_name}'

    image["file_name"] = new_name

annots["images"] = images

with open(str(args.output_json), 'w') as json_file:
	json.dump(annots, json_file)
