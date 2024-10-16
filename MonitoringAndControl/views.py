from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import cv2 as cv
import os
import numpy as np
from ultralytics import YOLO

model = os.path.join("C:\\Dev2\\MiniProject\\dynamicTrafficLightControl\\ProjectFolder\\MonitoringAndControl\\best.pt")

cam = cv.VideoCapture(0)

data = {'noOfVehiclesWest':0,
        'noOfVehiclesNorth':0,
        'noOfVehiclesSouth':0,
        'noOfVehiclesEast':0,        
}

def homepage(request):
    template = loader.get_template('homepage.html')
    context = {
        'noOfVehiclesWest':0,
        'noOfVehiclesNorth':0,
        'noOfVehiclesSouth':0,
        'noOfVehiclesEast':0,
    }
    return HttpResponse(template.render(context,request))


def getData(request):
    ret,frame = cam.read()
    model = YOLO("best.pt")
    results = model(frame)

    for r in results:
        numberOfVehicles = 0
        boxTensor = r.boxes.xyxy
        boxArray = boxTensor.cpu().numpy()
        for i in boxArray:
            numberOfVehicles += 1

    data['noOfVehiclesWest'] = numberOfVehicles
    data['noOfVehiclesNorth'] = numberOfVehicles
    data['noOfVehiclesSouth'] = numberOfVehicles
    data['noOfVehiclesEast'] = numberOfVehicles
    return JsonResponse(data)