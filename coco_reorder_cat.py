import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

## CHANGE CATEGORY HERE
REORDERED_CAT = ['Cat', 'Dog', 'Bird', 'Chicken', 'Snake', 'Elephant', 'Dinosaur', 'Crocodile']

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

new_categories = []
id_change = {}

for category in coco_data["categories"]:
    cat_name = category["name"]
    cat_id = category["id"]

    new_id = REORDERED_CAT.index(cat_name) + 1
    category["id"] = new_id
    new_categories.append(category)
    id_change[cat_id] = new_id

sorted_cat = sorted(new_categories, key = lambda i: i['id'])
coco_data["categories"] = sorted_cat

annots = coco_data["annotations"]
new_annots = []

for annot in annots:
    cat_id = annot["category_id"]
    annot["category_id"] = id_change[cat_id]
    new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
