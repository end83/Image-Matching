import numpy as np
import csv

class search_bro:
    def __init__(self,path):
        self.path=path
    
    def distance(self,hist1,hist2,eps=1e-8):
        dis=0.5*np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(hist1,hist2)])        #use itertools.izip for large training data
        return dis

    def search(self,qfeature,lim=3):
        result={}
        with open(self.path) as f:
            reader=csv.reader(f)
            for row in reader:
                features=[float(x) for x in row[1:]]
                d=self.distance(features,qfeature)
                result[row[0]]=d
            f.close()
        result=sorted([(v,k) for (k,v) in result.items()])
        return result[:lim]