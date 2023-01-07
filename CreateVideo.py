import os
import cv2

path = "Images/"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        print(file_name)
        Images.append(file_name)

count = len(Images)
print(count)

frameSize = cv2.imread(Images[0])
height, width, channels = frameSize.shape
size = (width,height)
print(size)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('project.avi',fourcc,1,size)

for i in range(0,count-1):
    img = cv2.imread(Images[i])
    out.write(img)

#out.release()
print("Done")
