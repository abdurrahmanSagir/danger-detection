import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
import os


def hu_moments(path):
        MEI=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        moment=cv2.moments(MEI)
        huMoment=cv2.HuMoments(moment).flatten()
        return huMoment

def compare(arr1 , arr,stra,counter):
        result=math.sqrt((arr1[0]-arr[0])**2+(arr1[1]-arr[1])**2+(arr1[2]-arr[2])**2+(arr1[3]-arr[3])**2+(arr1[4]-arr[4])**2+(arr1[5]-arr[5])**2+(arr1[6]-arr[6])**2)
        print (str(counter)+stra+" karşılaştırması sonucu\t: "+str(result))
        return result


def main():
        hu1=hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma1/MEI.bmp")
        directories=os.listdir("/Users/abdurrahman/desktop/goruntu/")
        hu_array=[]
        plotar=[]
        compare_array=[]
        counter=0
        for i in directories:
                        hu_array.append(hu_moments("/Users/abdurrahman/desktop/goruntu/"+i+"/MEI.bmp"))
        for index,moment in enumerate(hu_array):
                index2=index+1
                while(index2<len(hu_array)):                        
                        compare_array.append(counter)
                        plotar.append(compare(hu_array[index],hu_array[index2],"\t"+directories[index]+" ile "+directories[index2],counter))
                        index2=index2+1
                        counter=counter+1
        
        i=77
        summ=0
        while i<105:
                summ=plotar[i]+summ
                i=i+1
        print(summ/28)
        plt.plot(compare_array,plotar)
        plt.grid(True)
        plt.show()
        
if __name__=="__main__":
        main()





        
