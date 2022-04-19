import os
import random


def getFlist(data_path):
    global label
    global num
    global res
    dir_names = os.listdir(data_path)
    dirnum = 0
    for dir_name in dir_names:
        if (data_path=='/home/cell/datasets/cell/images'):
            label = dir_name[:2]
        new_dir = os.path.join(data_path,dir_name)
        if os.path.isfile(new_dir):
            num = num+1
            dirnum = dirnum +1
            image_file.write(str(num)+" "+new_dir[32:]+"\n")
            icl_file.write(str(num)+" "+label+"\n")
            # valnum=int(0.2*len(dir_names))
            # if valnum!=0:
            #     valgap=int(len(dir_names)/valnum)
            # else:
            #     valgap=0
            # if (valgap>2 and dirnum%valgap==int(valgap/2)):
            #     tts_file.write(str(num)+" 0\n")
            # else:
            #     tts_file.write(str(num)+" 1\n")
            if data_path.find('new')!=-1:
                tts_file.write(str(num)+" 2\n")
            else:
                if num % 2==1:
                    res = random.randint(0,1)
                    if res == 0:
                        tts_file.write(str(num)+" 0\n")
                    else:
                        tts_file.write(str(num)+" 1\n")
                else:
                    if res == 0:
                        tts_file.write(str(num)+" 1\n")
                    else:
                        tts_file.write(str(num)+" 0\n")
        if os.path.isdir(new_dir):
            getFlist(new_dir)

if __name__=="__main__":
    tts_file = open('train_test_split.txt', 'w')
    icl_file = open('image_class_labels.txt','w')
    image_file = open('images.txt','w')
    data_path = '/home/cell/datasets/cell/images'
    num=0
    flist = getFlist(data_path) 
    tts_file.close()
    icl_file.close()
    image_file.close()