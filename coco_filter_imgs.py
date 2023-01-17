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
images_removed = 0
id_change = {}

for image in coco_data["images"]:
    img_name = image["file_name"]
    img_id = image["id"]

    ## CHANGE FILTER FUNCTION HERE
    prefixes = ["set10"]
    if not img_name.startswith(tuple(prefixes)):
        images_removed += 1
        id_change[img_id] = 0
        # print(img_name)

    else:
        new_id = img_id - images_removed
        image["id"] = new_id
        new_images.append(image)
        id_change[img_id] = new_id

coco_data["images"] = new_images

annots = coco_data["annotations"]
new_annots = []
annotations_removed = 0

for annot in annots:
    img_id = annot["image_id"]
    annot_id = annot["id"]

    if id_change[img_id] == 0:
        annotations_removed += 1
    else:
        new_annot_id = annot_id - annotations_removed
        annot["id"] = new_annot_id
        annot["image_id"] = id_change[img_id]
        new_annots.append(annot)

coco_data["annotations"] = new_annots

with open(str(args.output_json), 'w') as json_file:
    json.dump(coco_data, json_file)
