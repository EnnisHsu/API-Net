import os
import time
time_start = time.time()
print('start_read_dateset')
path_images = './CUB_200_2011/images.txt'
path_split =  './CUB_200_2011/train_test_split.txt'
path_class="./CUB_200_2011/image_class_labels.txt"
path="./CUB_200_2011/images/"
print('fin_read_dateset_and_new_txt')
f_test=open("./CUB_200_2011/val.txt","w")
f_train=open("./CUB_200_2011/train.txt","w")
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
    if int(label) == 1:
        f_train.write(path+file_name+" "+Class+"\n")
    else:
        f_test.write(path+file_name+" "+Class+"\n")
time_end = time.time()
print('CUB200 train set and val set split successfully, time%s!!' % (time_end - time_start))
f_test.close()
f_train.close()
