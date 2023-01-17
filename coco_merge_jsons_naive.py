import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_paths', help='annotations json paths', nargs='+', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

coco_datas = []
for idx, json_path in enumerate(args.json_paths):
    with open(json_path) as json_file:
        if idx == 0:
            new_coco_data = json.load(json_file)
        else:
            coco_datas.append(json.load(json_file))

for coco_data in coco_datas:
    new_coco_data["images"].extend(coco_data["images"])
    new_coco_data["annotations"].extend(coco_data["annotations"])

with open(str(args.output_json), 'w') as json_file:
    json.dump(new_coco_data, json_file)
