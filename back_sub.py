import cv2
import numpy as np
class BackGroundSubtractor:
        
        def __init__(self,firstFrame):
                
                self.backGroundModel = firstFrame

        def getForeground(self,frame):
                        return cv2.absdiff(self.backGroundModel.astype(np.uint8),frame)

##
##        def back_sub_2(self,frame):
##                ret=frame
##                print (frame.dtype)
##                print (ret.dtype)
##                print (self.backGroundModel.dtype)
##                
##                for x in range(0,240):
##                
##                        for y in range(0,320):
##                                if ((frame[x][y]-self.backGroundModel[x][y])>120) or ((frame[x][y]-self.backGroundModel[x][y])<120) :
##                                        ret[x][y]=255
##                                        print frame[x][y]
##                                else:
##                                        ret[x][y]=0
##                                
##
##                return ret
