WORKSPACE=/media/data/coco_data_cleaning
DATA=/media/data/datasets

docker run -it \
    -w $WORKSPACE \
	-v $WORKSPACE:$WORKSPACE \
	-v $DATA:$DATA \
	python:3.10 \
	bash
