import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

min_img_id = min(coco_data["images"], key=lambda x:x["id"])["id"]
img_id_offset = min_img_id - 1

new_images = []
id_change = {}

for image_data in coco_data["images"]:
    img_id = image_data["id"]
    new_id = img_id - img_id_offset
    image_data["id"] = new_id
    new_images.append(image_data)
    id_change[img_id] = new_id

coco_data["images"] = new_images

annots = coco_data["annotations"]
new_annots = []

for annot in annots:
    img_id = annot["image_id"]
    annot["image_id"] = id_change[img_id]
    new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
