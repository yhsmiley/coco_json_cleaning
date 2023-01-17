import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

coco_filtered = []

lrp_thresh = [0.887, 0.755, 0.647, 0.838, 0.893]

for pred in coco_data:
    ## CHANGE FILTER FUNCTION HERE
    if pred['score'] >= lrp_thresh[pred['category_id']-1]:
        coco_filtered.append(pred)

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_filtered, json_file)
