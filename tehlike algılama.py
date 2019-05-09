import numpy as np
import cv2
import back_sub as bs
from denoise import denoise as denoise
import MEI
import humoments as hm

kac_kez_tas_atildi_yazdi=0
tas_atildi_mi=False
kac_frame_gecti=0


tas=[]
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma1/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma2/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma3/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma4/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma5/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma6/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma7/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma8/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma9/MEI.bmp"))
tas.append(hm.hu_moments("/Users/abdurrahman/desktop/goruntu/tasatma10/MEI.bmp"))

cam = cv2.VideoCapture(0)
i=0
while i<5:
  ret,frame = cam.read()
  i=i+1

frame = denoise(frame)
frame = cv2.resize(frame,(0,0),fx=1/3, fy=1/3)

if ret is True:
        backSubtractor = bs.BackGroundSubtractor(frame)
        run = True
else:
        run = False
counter=1
boolMEI=False
while(run):
        
        ret,frame = cam.read()
        
        if ret is True:
                frame = denoise(frame)
                frame = cv2.resize(frame,(0,0),fx=1/3, fy=1/3)
                foreGround = backSubtractor.getForeground(frame)
                ret, mask = cv2.threshold(foreGround, 20, 255, cv2.THRESH_BINARY)
                mask = cv2.medianBlur(mask,11)
                cv2.imshow('mask',mask)
                cv2.imwrite("/Users/abdurrahman/desktop/goruntu/canli/"+str(counter)+".bmp",mask)
                if counter==20:
                  counter=1
                  if boolMEI==False:
                    boolMEI=True

                
                if boolMEI==True:
                  MEI.create_MEI("/Users/abdurrahman/desktop/goruntu/canli")
                  canli_hu=hm.hu_moments("/Users/abdurrahman/desktop/goruntu/canli/MEI/MEI.bmp")                  
                  i=1
                  action=0
                  kac_frame_gecti=kac_frame_gecti+1
                  if kac_frame_gecti% 30==0:  #kaç framede bir ne kadar taş atıldı yazdığını kontrol etme sayacı
                    kac_kez_tas_atildi_yazdi=0
                  while(i<10):
                    distance=hm.compare(canli_hu,tas[i],"deneme",i)
                    i=i+1
                    
                    if distance<0.00006:
                      action=action+1
                  if action>5:
                    print("Taş atıldı")
                    kac_kez_tas_atildi_yazdi=kac_kez_tas_atildi_yazdi+1
                    if kac_kez_tas_atildi_yazdi>=4:
                      tas_atildi_mi=True
                  



              
                counter = counter+1
                key = cv2.waitKey(10) & 0xFF
        else:
                break

        if key == 27:
                break
                
if tas_atildi_mi:
  print ("Tas kesin atıldı ")

cam.release()
cv2.destroyAllWindows()
