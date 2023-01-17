import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--json_path', help='annotations json path', required=True)
args = ap.parse_args()

with open(str(args.json_path)) as json_file:
    coco_data = json.load(json_file)

all_img_id = set()

for annot in coco_data["annotations"]:
    img_id = annot["image_id"]
    all_img_id.add(img_id)

print(f'num images: {len(coco_data["images"])}')
print(f'num images with annotations: {len(all_img_id)}')
print(f'num annotations: {len(coco_data["annotations"])}')
