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
${yolov5}
```
You can run this command to split the training data into training set and validation set:
```
python3 split.py
```
# Training
To train the model, run this command:
```
python3 ./yolov5/train.py --batch 64 --epoch 50 --data svhn.yaml --cfg yolov5m.yaml --weight yolov5m.pt
```
# Evaluation
If you want to detect the street numbers in testing images, run this command:
```
python3 ./yolov5/detect.py --weights {weight_path} --source ../data/test --save-txt --save-conf
```
You can download pretrained weight here:
```
https://drive.google.com/drive/folders/1Vg95zri9a8YvCqszL93trzC4SPEn9qG6
```
After detecting all testing images, you can use this command to get answer.json:
```
python3 submit.py
```
The inference.ipynb can be found below:
```
https://colab.research.google.com/drive/13nOlfNeLaJNwZC3ZUPBkzS-3oBcZmdpq
```
# Results
mAP 0.5, 0.95 => 0.407894 <br>
Inference time per image => 0.103869
# Reference
Yolov5
```
https://github.com/ultralytics/yolov5
```

