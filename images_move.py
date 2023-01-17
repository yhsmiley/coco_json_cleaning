import argparse
import shutil
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--src_folder', type=str, help='source folder path containing all images', required=True)
ap.add_argument('--dest_folder', type=str, help='destination folder path to move all images', required=True)
args = ap.parse_args()


Path(args.dest_folder).mkdir(parents=True, exist_ok=True)

for img_path in Path(args.src_folder).rglob("*.jpg"):
	shutil.copyfile(img_path, Path(args.dest_folder)/img_path.name)
