import cv2
import numpy as np
from search_kr import search_bro
from colordecriptor import ColorDecriptor

inp=raw_input("Enter the full address of the image :-\n")
img=cv2.imread(inp,1)

if img is None:
    print 'image not opening, please try again later'
else:
    cv2.namedWindow("input_image",cv2.WINDOW_NORMAL)
    cv2.namedWindow("final_images",cv2.WINDOW_NORMAL)
    cd=ColorDecriptor((8,12,3))
    features=cd.describe(img)
    srch=search_bro('Z:\output.csv') #Address of the CSV file that is use should be given here
    result=srch.search(features)
    cv2.imshow('input_image',img)
    for (val,id) in result:
        ans=cv2.imread('Z:\dataset'+"\\" + id,1) #folder of dataset should be given here
        cv2.imshow('final_images',ans)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    