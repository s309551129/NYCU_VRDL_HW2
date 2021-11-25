import numpy as np
import h5py
import cv2
import random


def get_name(idx, data):
    name_ref = data["digitStruct/name"][idx].item()
    return ''.join([chr(v[0]) for v in data[name_ref]])


def get_bbox(idx, data):
    attrs = {}
    item_ref = data["digitStruct/bbox"][idx].item()
    for key in ['label', 'left', 'top', 'width', 'height']:
        attr = data[item_ref][key]
        values = [data[attr[i].item()][0][0].astype(int)
                  for i in range(len(attr))] if len(attr) > 1 else [attr[0][0]]
        attrs[key] = values
    return attrs


def write(root, img_name, img_arr):
    img = cv2.imread("./train/"+img_name)
    img_height, img_width, _ = img.shape
    cv2.imwrite(root+"images/"+img_name, img)
    fout = open(root+"labels/"+img_name.replace('.png', '.txt'), 'w')
    for i in range(len(img_arr['label'])):
        label = int(img_arr['label'][i])
        if label == 10:
            label = 0
        top, left = img_arr['top'][i], img_arr['left'][i]
        height, width = img_arr['height'][i], img_arr['width'][i]
        if left + width > img_width:
            width = img_width - left - 1
        if top + height > img_height:
            height = img_height - top - 1
        x_center, y_center = (left+width/2) / img_width, (top+height/2) / img_height
        bbox_width, bbox_height = height / img_height, width / img_width
        fout.write(str(label)+' '+str(x_center)+' '+str(y_center)+' '+str(bbox_width)+' '+str(bbox_height)+"\n")
    fout.close()


if __name__ == '__main__':
    data = h5py.File("./data/train/digitStruct.mat", 'r')
    data_num = 33402
    sample_num = 3000
    data_idx = [i for i in range(data_num)]
    sample_idx = random.sample(data_idx, sample_num)
    for i in range(data_num):
        img_name = get_name(i, data)
        img_arr = get_bbox(i, data)
        print(img_name)
        if i not in sample_idx:
            write("./training/", img_name, img_arr)
        else:
            write("./validation/", img_name, img_arr)
