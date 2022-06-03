from itertools import count
from unittest import result
from Deteck2 import DetectHtmlElements
import cv2



def makeCroppedImages(img_path,df):
    count = 0
    img = cv2.imread(img_path)
    for i in df:
        cropped_img = img[int(i['y']):int(i['ymax']),int(i['x']):int(i['xmax'])]
        cv2.imwrite('cropped_images/'+str(count)+'.png',cropped_img)      
        df[count]['associated_text'] = 'cropped_images/' + str(count) + '.png'
        # df[count]['associated_text'] = str(count) + '.png'
        count += 1 
    return df    
        