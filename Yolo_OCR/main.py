from ultralytics import YOLO
import cv2
import pandas as pd
from PIL import Image
import numpy as np
import os, PIL, io, cv2, torch
import easyocr
import csv

#easyocr
reader = easyocr.Reader(['ar'], gpu=False)

#Class_names
class_names = ['Date_N_cin', 'Lieu_cin', 'Nom_cin', 'Num_cin', 'Prenom2_cin', 'Prenom_cin']

#load models
Num_cin_detector = YOLO('Model/weights/best.pt')

#input_image
image_path='image/72.jpeg'

#image_directory = 'image/'
# Loop through each image file
#image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
#for image_file in image_files:
#    image_path = os.path.join(image_directory, image_file)
#    original_image = Image.open(image_path)

# Get a list of all image files in the directory

original_image = Image.open(image_path)
results= Num_cin_detector.predict(source=image_path, conf=0.6)
    # Process each set of detection results
for i in range(len(results[0].boxes)):
        x_min, y_min, x_max, y_max = map(int, results[0].boxes.xyxy[i].tolist())
        confidence = results[0].boxes.conf[i]
        class_index = int(results[0].boxes.cls[i])

        if confidence >= 0.6:  
            class_name = class_names[class_index]

            # Crop the image using the bounding box coordinates
            cropped_image = original_image.crop((x_min, y_min, x_max, y_max))
            
            # Save the cropped image for inspection
            cropped_image.convert('RGB').save(os.path.join(f'cropped', f'{class_name}.jpg'))



def extract_cin_text(in_crop):
    detections=reader.readtext(in_crop)
    for detection in detections:
        bbox, text, score = detection
        text = text.upper().replace(' ', ' ')
    return text


Date='cropped/Date_N_cin.jpg'
Lieu='cropped/Lieu_cin.jpg'
Nom='cropped/Nom_cin.jpg'
Num='cropped/Num_cin.jpg'
Prenom='cropped/Prenom_cin.jpg'
Prenom2='cropped/Prenom2_cin.jpg'    

date = extract_cin_text(Date)
lieu= extract_cin_text(Lieu)
nom= extract_cin_text(Nom)
num= extract_cin_text(Num)
prenom= extract_cin_text(Prenom)
prenom2= extract_cin_text(Prenom2)


data = {'Numero Cin': [num],
               'Nom': [nom],
            'Prenom': [prenom],
           'Prenom2': [prenom2],
    'Date_Naissance': [date],
    'Lieu_Naissance': [lieu]}

df = pd.DataFrame(data)
df.to_csv('csv/output.csv',index=False)
df
