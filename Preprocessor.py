# Import

from Deteck2 import DetectHtmlElements
from HtmlGenerator import HtmlPage
from CropImages import makeCroppedImages
from Tesseract import textRecognizer
# from TRclient import textRecognizer

import datetime
import math



# Distance Formula
def getDistance(element1,element2):
    return math.sqrt((element1['xcenter'] - element2['xcenter']) ** 2 + (element1['ycenter'] - element2['ycenter']) ** 2)

# Get min distant element
def getMinDistantElement(input_element,associated_text):
    distance = []
    for k in associated_text:
        distance.append(getDistance(input_element,k))
    main_associated_text = associated_text[distance.index(min(distance))]
    return main_associated_text

# Preprocessing
def ElementMaker(img_path,title='',theme=''):
    df = DetectHtmlElements(img_path)

    elements = []
    text_elements = []
    input_elements = []

    for i in df.index:
        if df['name'][i] == 'Text':
            text_elements.append({
                'class': df['name'][i],
                'associated_text': 'Lorem',
                'x': df['xmin'][i],
                'xmax': df['xmax'][i],
                'y': df['ymin'][i],
                'ymax': df['ymax'][i],
                'width': df['xmax'][i] - df['xmin'][i],
                'height': df['ymax'][i] - df['ymin'][i],
                'xcenter': df['xmin'][i] + ((df['xmax'][i] - df['xmin'][i])/2),
                'ycenter': df['ymin'][i] + ((df['ymax'][i] - df['ymin'][i])/2)
            })
        elif df['name'][i] in ['Textbox', 'Select', 'Checkbox', 'Radio', 'Image']:
            input_elements.append({
                'class': df['name'][i],
                'associated_text': '',
                'x': df['xmin'][i],
                'xmax': df['xmax'][i],
                'y': df['ymin'][i],
                'ymax': df['ymax'][i],
                'width': df['xmax'][i] - df['xmin'][i],
                'height': df['ymax'][i] - df['ymin'][i],
                'xcenter': df['xmin'][i] + ((df['xmax'][i] - df['xmin'][i])/2),
                'ycenter': df['ymin'][i] + ((df['ymax'][i] - df['ymin'][i])/2)
            }) 
        elif df['name'][i] == 'Button':
            if df['confidence'][i] > 0.55:
                 input_elements.append({
                    'class': df['name'][i],
                    'associated_text': '',
                    'x': df['xmin'][i],
                    'xmax': df['xmax'][i],
                    'y': df['ymin'][i],
                    'ymax': df['ymax'][i],
                    'width': df['xmax'][i] - df['xmin'][i],
                    'height': df['ymax'][i] - df['ymin'][i],
                    'xcenter': df['xmin'][i] + ((df['xmax'][i] - df['xmin'][i])/2),
                    'ycenter': df['ymin'][i] + ((df['ymax'][i] - df['ymin'][i])/2)
                }) 
        else:
            elements.append({
                'class': df['name'][i],
                'associated_text': '',
                'x': df['xmin'][i],
                'xmax': df['xmax'][i],
                'y': df['ymin'][i],
                'ymax': df['ymax'][i],
                'width': df['xmax'][i] - df['xmin'][i],
                'height': df['ymax'][i] - df['ymin'][i],
                'xcenter': df['xmin'][i] + ((df['xmax'][i] - df['xmin'][i])/2),
                'ycenter': df['ymin'][i] + ((df['ymax'][i] - df['ymin'][i])/2)
            })
    
    # Crop Images
    text_elements = makeCroppedImages(img_path,text_elements)
    
    # Text Recognizing
    for i in range(len(text_elements)):
        text_elements[i]['associated_text'] = textRecognizer(text_elements[i]['associated_text'])
    
    # Associted Text Generation 
    
    count = 0 
    remove_text_elements = []      
    for i in input_elements:
        ## For Button
        if i['class'] == 'Button':
            associated_text = [j for j in text_elements if ( j['x']>i['x'] and j['y']>i['y'] and j['xmax']<i['xmax'] and j['ymax']<i['ymax'] )]
            if len(associated_text) != 0:
                input_elements[count]['associated_text'] = associated_text[0]['associated_text']
            else:
                input_elements[count]['associated_text'] = ''
            remove_text_elements = remove_text_elements + associated_text
            
            for i in remove_text_elements:
                if i in text_elements:
                    text_elements.remove(i)
          
        ## For Textbox
        elif i['class'] == 'Textbox':
            associated_text = [j for j in text_elements if ( j['x']<i['xcenter'] and j['y'] < i['ycenter'])]
            if len(associated_text) != 0:
                main_associated_text = getMinDistantElement(i,associated_text)
                input_elements[count]['associated_text'] = main_associated_text['associated_text']
            else:
                main_associated_text = ''
                input_elements[count]['associated_text'] = ''
            text_elements.remove(main_associated_text)
            
            # remove_text_elements = remove_text_elements + [main_associated_text]
            # for i in remove_text_elements:
            #     if i in text_elements:
            #         text_elements.remove(i)
 
       
        ## For Select
        elif i['class'] == 'Select':
            associated_text = [j for j in text_elements if (j['x']<i['xcenter'] and j['y'] < i['ycenter'])]
            if len(associated_text) != 0:
                main_associated_text = getMinDistantElement(i,associated_text)
                input_elements[count]['associated_text'] = main_associated_text['associated_text']
            else:
                main_associated_text = ''
                input_elements[count]['associated_text'] = ''
            text_elements.remove(main_associated_text)
            
                
        
        ## For Checkbox & Radio Button
        elif i['class'] in ['Checkbox','Radio']:
            associated_text = [j for j in text_elements if (j['xcenter']>i['xcenter'] and j['y'] < i['ycenter'])]
            if len(associated_text) != 0:
                main_associated_text = getMinDistantElement(i,associated_text)
                input_elements[count]['associated_text'] = main_associated_text['associated_text']
            else:
                main_associated_text = ''
                input_elements[count]['associated_text'] = ''
            text_elements.remove(main_associated_text)
        
        
        ## For Image
        elif i['class'] in ['Image','Video']:
            associated_text = [j for j in text_elements if (j['x']<i['xcenter'] and j['xmax']>i['xcenter'] and j['y'] > i['ycenter'])]
            if len(associated_text) != 0:
                main_associated_text = getMinDistantElement(i,associated_text)
                input_elements[count]['associated_text'] = main_associated_text['associated_text']
            else:
                main_associated_text = ''
                input_elements[count]['associated_text'] = ''
            text_elements.remove(main_associated_text) 
        
        
        count += 1
            
    # for i in remove_text_elements:
    #     if i in text_elements:
    #         text_elements.remove(i)
            
            
    
    # test = HtmlPage(title,True,elements+input_elements+text_elements,theme)
    # test.gridInit()
    # test.generate()
    return elements+input_elements+text_elements
    


# ElementMaker('test.jpeg')
if __name__ == '__main__':
    time = datetime.datetime.now()
    ElementMaker('0.png','OCR3000','success')
    print(datetime.datetime.now() - time)