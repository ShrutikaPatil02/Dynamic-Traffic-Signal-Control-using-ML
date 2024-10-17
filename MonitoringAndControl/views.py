from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import cv2 as cv
import numpy as np
from ultralytics import YOLO
import datetime

model = YOLO("best.pt")

#cam = cv.VideoCapture(0)
token = 1

timeTemp = datetime.datetime.now() + datetime.timedelta(0,2,0)

data = {'noOfVehiclesWest':0,
        'timerWest':0,
        'noOfVehiclesNorth':0,
        'timerNorth':0,
        'noOfVehiclesSouth':0,
        'timerSouth':0,
        'noOfVehiclesEast':0,   
        'timerEast':0,     
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
    global token,timeTemp
    if(token == 1 and data['timerWest'] == 0):
        token = 2
        frame = cv.imread('trafficTest2.jpeg')
        results = model(frame)

        for r in results:
            numberOfVehicles = 0
            boxTensor = r.boxes.xyxy
            boxArray = boxTensor.cpu().numpy()
            for i in boxArray:
                numberOfVehicles += 1

        data['noOfVehiclesNorth'] = numberOfVehicles
        timeTemp += datetime.timedelta(0,numberOfVehicles,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerNorth'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token ==2 and data['timerNorth']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerNorth'] = difference.seconds
        return JsonResponse(data) 
    elif(token == 2 and data['timerNorth'] == 0):
        token = 3
        frame = cv.imread('trafficTest3.jpeg')
        results = model(frame)

        for r in results:
            numberOfVehicles = 0
            boxTensor = r.boxes.xyxy
            boxArray = boxTensor.cpu().numpy()
            for i in boxArray:
                numberOfVehicles += 1
        data['noOfVehiclesEast'] = numberOfVehicles
        timeTemp += datetime.timedelta(0,numberOfVehicles,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerEast'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 3 and data['timerEast']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerEast'] = difference.seconds
        return JsonResponse(data)
    elif(token == 3 and data['timerEast']==0):
        token = 4
        frame = cv.imread('trafficTest4.jpeg')
        results = model(frame)

        for r in results:
            numberOfVehicles = 0
            boxTensor = r.boxes.xyxy
            boxArray = boxTensor.cpu().numpy()
            for i in boxArray:
                numberOfVehicles += 1
        data['noOfVehiclesSouth'] = numberOfVehicles
        timeTemp += datetime.timedelta(0,numberOfVehicles,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerSouth'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 4 and data['timerSouth']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerSouth'] = difference.seconds
        return JsonResponse(data)
    elif(token == 4 and data['timerSouth'] == 0):
        token = 1
        frame = cv.imread('trafficTest.jpeg')
        results = model(frame)

        for r in results:
            numberOfVehicles = 0
            boxTensor = r.boxes.xyxy
            boxArray = boxTensor.cpu().numpy()
            for i in boxArray:
                numberOfVehicles += 1
        data['noOfVehiclesWest'] = numberOfVehicles
        timeTemp += datetime.timedelta(0,numberOfVehicles,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerWest'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 1 and data['timerWest']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerWest'] = difference.seconds
        return JsonResponse(data)
    return JsonResponse(data)