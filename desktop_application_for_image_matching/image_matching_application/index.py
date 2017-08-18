from colordecriptor import ColorDecriptor
import cv2
import os

def folder_loaded(folder):
    images=[]
    image_ids=[]
    for file in os.listdir(folder):
        image=cv2.imread(os.path.join(folder,file))
        if image is not None:
            images.append(image)
            image_ids.append(file)

    return images,image_ids

required_folder='Z:\dataset' #address of the folder of dataset
list,ids=folder_loaded(required_folder)
cd=ColorDecriptor((8,12,3))
out=open("Z:\output.csv","w")#address of the CSV file which you will use

for img,id in zip(list,ids):        #if the training data set is large use itertools.izip
    features=cd.describe(img)
    features=[str(f) for f in features]
    out.write("%s,%s\n" %(id,",".join(features)))

out.close()

    

