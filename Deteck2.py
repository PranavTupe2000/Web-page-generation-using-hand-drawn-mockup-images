import torch

# # Model
# model = torch.load('./best.pt')

# # Image
# img = '0.png'

# # Result
# result = model(img)
# result.save()

def DetectHtmlElements(imgPath):
    model = torch.hub.load('./yolov5', 'custom', path='best1.pt', force_reload=True, source='local') 
    result = model(imgPath)
    # result.save()
    return result.pandas().xyxy[0]