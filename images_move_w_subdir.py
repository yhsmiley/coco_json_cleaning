import argparse
import shutil
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument('--src_folder', type=str, help='source folder path containing all images', required=True)
ap.add_argument('--dest_folder', type=str, help='destination folder path to move all images', required=True)
args = ap.parse_args()

for img_path in Path(args.src_folder).rglob("*.jpg"):
	if not len(list(Path(args.dest_folder).rglob(img_path.name))):
		## CHANGE THIS IF NEEDED
		dest_filepath = Path(args.dest_folder) / img_path.parent.name / img_path.name

		Path(dest_filepath.parent).mkdir(parents=True, exist_ok=True)
		shutil.copyfile(img_path, dest_filepath)
