# NYCU_VRDL_HW2
This repository is about HW2 in Visual Recognition using Deep Learning class, NYCU. The main target is to recognize the street numbers and localize them.
# Environment
Run this command to fit the requirement:
```
pip3 install -r ./yolov5/requirements.txt
```
# Prepare Dataset
You can download the dataset from codalab in-class competition:
```
https://competitions.codalab.org/competitions/35888#participate-get_starting_kit
```
After downloading, the data directory is structured as:
```
${data}
  +- train
  |  +- 1.png
  |  +- 2.png
  |  +- ...
  +- test
  |  +- 117.png
  |  +- 162.png
  |  +- ...
```
# Training
To train the model, run this command:
```
python3 ./yolov5/train.py 
```
# Evaluation
If you want to evaluate a single model, run this command:
```
python3 ./yolov5/detect.py 
```
You can download pretrained weight here:
```
https://drive.google.com/drive/folders/1Vg95zri9a8YvCqszL93trzC4SPEn9qG6
```
After downing all pretrained weight, please put them into ```./weight``` folder.
# Results
mAP 0.5, 0.95: 0.407894 <br>
Inference time per image: 0.103869 
# Reference
Yolov5
```
https://github.com/ultralytics/yolov5
```

