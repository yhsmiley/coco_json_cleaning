import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

min_ann_id = min(coco_data["annotations"], key=lambda x:x["id"])["id"]
ann_id_offset = min_ann_id - 1

annots = coco_data["annotations"]
new_annots = []

for annot in annots:
    ann_id = annot["id"]
    new_id = ann_id - ann_id_offset
    annot["id"] = new_id
    new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
