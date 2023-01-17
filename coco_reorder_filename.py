import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
ap.add_argument('--output_json', default='', help='path of output json', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

new_images = []
id_change = {}

for image_data in coco_data["images"]:
    file_name = image_data["file_name"]
    img_id = image_data["id"]

    new_id = int(file_name.split('.')[0])
    image_data["id"] = new_id
    new_images.append(image_data)
    id_change[img_id] = new_id

sorted_images = sorted(new_images, key = lambda i: i['id'])
coco_data["images"] = sorted_images

annots = coco_data["annotations"]
new_annots = []

for annot in annots:
    img_id = annot["image_id"]
    annot["image_id"] = id_change[img_id]
    new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
