import cv2
import os
import numpy as np
import math
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def create_MEI(path):
    MEI= np.array([])
    images=load_images_from_folder(path)
    
    for image in images:
        if MEI.size == 0:
            MEI=image
        MEI=MEI+image    
    ret,MEI = cv2.threshold(MEI, 20, 255, cv2.THRESH_BINARY)
    cv2.imwrite(path+"/deneme.bmp",MEI)


if __name__=="__main__":
    create_MEI("/Users/abdurrahman/desktop/goruntu/rapordeneme")
    
    
