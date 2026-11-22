import os
from ultralytics import YOLO

model = YOLO(os.path.join(os.path.dirname(__file__), 'best.pt'))

def model_img_box(img_path):
    results = model(img_path)
    res_plotted = results[0].plot()
    return res_plotted