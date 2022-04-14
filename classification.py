import os
import time
time_start = time.time()
print('start_read_dateset')
path_images = './cell/images.txt'
path_split =  './cell/train_test_split.txt'
path_class="./cell/image_class_labels.txt"
path="./cell/images/"
print('fin_read_dateset_and_new_txt')
f_test=open("./cell/val.txt","w")
f_train=open("./cell/train.txt","w")
images = []
with open(path_images,'r') as f:
    for line in f:
        images.append(list(line.strip('\n').split()))
split = []
with open(path_split, 'r') as f_:
    for line in f_:
        split.append(list(line.strip('\n').split()))
clss=[]
with open(path_class, 'r') as f_c:
    for cls in f_c:
        clss.append(list(cls.strip('\n').split()))
num = len(images)
print(num)
for k in range(num):
    file_name = images[k][-1]
    label = split[k][-1]
    Class=clss[k][-1]
    if (int(label) == 1):
        f_train.write(path+file_name+" "+Class+"\n")
    else:
        if (int(label) == 0):
            f_test.write(path+file_name+" "+Class+"\n")
time_end = time.time()
print('cell train set and val set split successfully, time%s!!' % (time_end - time_start))
f_test.close()
f_train.close()
