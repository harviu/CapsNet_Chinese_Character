from struct import unpack
import numpy as np 
from PIL import Image
from codecs import decode
import json
import os

test_dir="C:\\Users\\li.8460\\Desktop\\HW_data\\test\\"
train_dir = "C:\\Users\\li.8460\\Desktop\\HW_data\\train\\"


def process(dir):
    count = 0
    with open('chinese_labels','r') as labels:
        label_dict=json.load(labels)
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith((".gnt")):
                with open(root+name,mode = 'rb') as gnt:
                    length = gnt.read(4)
                    while length:
                        length = int.from_bytes(length,"little")
                        content = gnt.read(length-4)
                        up = unpack('ccHH'+'B'*(length-4-6),content)
                        width = up[2]
                        height = up[3]
                        bitmap = up[4:]
                        code = up[0]+up[1]
                        cha = decode(code,'gb2312')
                        if cha == "汕" or cha =="抄" or cha =="仙" or \
                                cha =="沙" or cha =="浊" or cha =="灿" or \
                                cha =="炒" or cha =="烛":
                            img_array = np.array(bitmap, dtype=np.uint8)
                            img_array = np.reshape(img_array,(height,width))
                            img = Image.fromarray(img_array)
                            img = img.resize((56,56))
                            try:
                                img.save(dir+cha+"/{}.png".format(count))
                            except:
                                os.mkdir(dir+cha)
                                img.save(dir+cha+"/{}.png".format(count))
                        count+=1
                        print("{:.2%}\r".format(count/1121749),end = "")
                        length = gnt.read(4)

process(test_dir)
process(train_dir)
