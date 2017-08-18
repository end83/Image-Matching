import cv2
import numpy as np

class ColorDecriptor:
    def __init__(self, bins):
        self.bins=bins

    def describe(self, image): 
        image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        features=[]
        (h,w)=image.shape[:2]
        (cx,cy)=(int(w*0.5),int(h*0.5))
        segments=[(0,cx,0,cy),(cx,w,0,cy),(0,cx,cy,h),(cx,w,cy,h)]
        (X,Y)=(int(0.75*w)/2,int(0.75*h)/2)
        ellipsemask=np.zeros(image.shape[:2],dtype="uint8")
        cv2.ellipse(ellipsemask,(cx,cy),(X,Y),0,0,360,255,-1)
        for(startx,endx,starty,endy)in segments:
            cornermask=np.zeros(image.shape[:2],dtype=np.uint8)
            cv2.rectangle(cornermask,(startx,starty),(endx,endy),255,-1)
            cornermask=cv2.subtract(cornermask,ellipsemask)
            hist=self.histogram(image,cornermask)
            features.extend(hist)

        hist=self.histogram(image,ellipsemask)
        features.extend(hist)
        return features

    def histogram(self,image,mask):
        hist=cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
        hist=cv2.normalize(hist,hist)
        hist=hist.flatten()
        return hist

