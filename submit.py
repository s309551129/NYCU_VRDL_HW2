import os
import cv2
import json

label_path = './yolov5/runs/detect/exp/labels/'
label_list = os.listdir(label_path)
label_list.sort(key=lambda x: int(x[:-4]))
result_to_json = []

for label in label_list:
    if not os.path.isfile(label_path+label):
        continue
    else:
        det_box_info = {}
        label_file = open(label_path+label, 'r')
        contents = label_file.readlines()
        img_name = label.replace("txt", "png")
        im = cv2.imread('./data/test/'+img_name)
        h, w, _ = im.shape

        for content in contents:
            content = content.replace('\n', '')
            c = content.split(' ')
            w_center = w*float(c[1])
            h_center = h*float(c[2])
            width = w*float(c[3])
            height = h*float(c[4])
            left = w_center - width/2
            top = h_center - height/2
            det_box_info = {
                "image_id": int(img_name[:-4]),
                "score": float(c[5]),
                "category_id": int(c[0]),
                "bbox": tuple((left, top, width, height))
            }
            result_to_json.append(det_box_info)
        label_file.close()

json_object = json.dumps(result_to_json, indent=4)

print(len(result_to_json))
with open('answer.json', 'w') as outfile:
    outfile.write(json_object)
