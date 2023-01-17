import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

## CHANGE CATEGORIES HERE
TO_KEEP = ['Cat', 'Dog', 'Bird', 'Chicken', 'Snake', 'Elephant', 'Dinosaur', 'Crocodile']

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

new_categories = []
num_removed = 0
id_change = {}

for category in coco_data["categories"]:
    cat_name = category["name"]
    cat_id = category["id"]

    if cat_name not in TO_KEEP:
        num_removed += 1
        id_change[cat_id] = 0

    else:
        new_id = cat_id - num_removed
        category["id"] = new_id
        new_categories.append(category)
        id_change[cat_id] = new_id

coco_data["categories"] = new_categories

annots = coco_data["annotations"]
new_annots = []
annotations_removed = 0

for annot in annots:
    cat_id = annot["category_id"]
    annot_id = annot["id"]

    if id_change[cat_id] == 0:
        annotations_removed += 1
    else:
        new_annot_id = annot_id - annotations_removed
        annot["id"] = new_annot_id
        annot["category_id"] = id_change[cat_id]
        new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
