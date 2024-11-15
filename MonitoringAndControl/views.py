from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import cv2 as cv
import numpy as np
from ultralytics import YOLO
import datetime
from django.http import StreamingHttpResponse
import threading
import time

model = YOLO("best.pt")

#cam = cv.VideoCapture(0)
token = 1

data = {'noOfVehiclesWest':0,
        'timerWest':0,
        'estimatedWaitTimeWest':0,
        'noOfVehiclesNorth':0,
        'timerNorth':0,
        'estimatedWaitTimeNorth':0,
        'noOfVehiclesSouth':0,
        'timerSouth':0,
        'estimatedWaitTimeSouth':0,
        'noOfVehiclesEast':0,   
        'timerEast':0, 
        'estimatedWaitTimeEast':0,    
}

timeTemp = datetime.datetime.now() + datetime.timedelta(0,2,0)

def detectVehicleSouth():
    global model
    frame = cv.imread('trafficTest4.jpeg')
    results = model(frame)

    
    for r in results:
        numberOfVehicles = 0
        boxTensor = r.boxes.xyxy
        boxArray = boxTensor.cpu().numpy()
        for i in boxArray:
            numberOfVehicles += 1
    data['noOfVehiclesSouth'] = numberOfVehicles
    time.sleep(5)
    detectVehicleSouth()


def detectVehicleNorth():
    global model
    
    frame = cv.imread('trafficTest2.jpeg')
    results = model(frame)
    
    for r in results:
        numberOfVehicles = 0
        boxTensor = r.boxes.xyxy
        boxArray = boxTensor.cpu().numpy()
        for i in boxArray:
            numberOfVehicles += 1
    data['noOfVehiclesNorth'] = numberOfVehicles
    time.sleep(5)
    detectVehicleNorth()



def detectVehicleWest():
    global model
    
    frame = cv.imread('trafficTest.jpeg')
    results = model(frame)
    for r in results:
        numberOfVehicles = 0
        boxTensor = r.boxes.xyxy
        boxArray = boxTensor.cpu().numpy()
        for i in boxArray:
            numberOfVehicles += 1
    data['noOfVehiclesWest'] = numberOfVehicles
    time.sleep(5)
    detectVehicleWest()

def detectVehicleEast():
    global model
    
    frame = cv.imread('trafficTest3.jpeg')
    results = model(frame)
    for r in results:
        numberOfVehicles = 0
        boxTensor = r.boxes.xyxy
        boxArray = boxTensor.cpu().numpy()
        for i in boxArray:
            numberOfVehicles += 1
    data['noOfVehiclesEast'] = numberOfVehicles
    time.sleep(5)
    detectVehicleEast()

f5 = threading.Thread(target=detectVehicleWest)
f2 = threading.Thread(target=detectVehicleEast)
f3 = threading.Thread(target=detectVehicleSouth)
f4 = threading.Thread(target=detectVehicleNorth)

f5.start()
f2.start()
f3.start()
f4.start()


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
        timeAlloted = data["noOfVehiclesNorth"]*0.57+9.40
        if(timeAlloted<15):
            timeAlloted = 15
        #data['noOfVehiclesNorth'] = numberOfVehicles
        timeTemp += datetime.timedelta(0,timeAlloted,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerNorth'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token ==2 and data['timerNorth']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerNorth'] = difference.seconds
        return JsonResponse(data) 
    elif(token == 2 and data['timerNorth'] == 0):
        token = 3
        timeAlloted = data["noOfVehiclesEast"]*0.57+9.40
        if(timeAlloted<15):
            timeAlloted = 15
        timeTemp += datetime.timedelta(0,timeAlloted,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerEast'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 3 and data['timerEast']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerEast'] = difference.seconds
        return JsonResponse(data)
    elif(token == 3 and data['timerEast']==0):
        token = 4
        timeAlloted = data["noOfVehiclesSouth"]*0.57+9.40
        if(timeAlloted<15):
            timeAlloted = 15
        
        timeTemp += datetime.timedelta(0,timeAlloted,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerSouth'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 4 and data['timerSouth']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerSouth'] = difference.seconds
        return JsonResponse(data)
    elif(token == 4 and data['timerSouth'] == 0):
        token = 1
        timeAlloted = data["noOfVehiclesWest"]*0.57+9.40
        if(timeAlloted<15):
            timeAlloted = 15
        timeTemp += datetime.timedelta(0,timeAlloted,0)
        difference = timeTemp - datetime.datetime.now()
        data['timerWest'] = difference.total_seconds()
        return JsonResponse(data)
    elif(token == 1 and data['timerWest']!=0):
        difference = timeTemp - datetime.datetime.now()
        data['timerWest'] = difference.seconds
        return JsonResponse(data)
    return JsonResponse(data)

def displayWest(request):
    template = loader.get_template('display_west.html')
    return HttpResponse(template.render())


def vidStreamWest():
    #frame = cv.imread('trafficTest2.jpeg')
    while True:
        frame = cv.imread('trafficTest2.jpeg')
        image_bytes = cv.imencode('.jpg',frame)[1].tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        
def videoFeedWest(request):
    return StreamingHttpResponse(vidStreamWest(),content_type = 'multipart/x-mixed-replace; boundary=frame')

def displayEast(request):
    template = loader.get_template('display_east.html')
    return HttpResponse(template.render())

def vidStreamEast():
    #frame = cv.imread('trafficTest2.jpeg')
    while True:
        frame = cv.imread('trafficTest.jpeg')
        image_bytes = cv.imencode('.jpg',frame)[1].tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        
def videoFeedEast(request):
    return StreamingHttpResponse(vidStreamEast(),content_type = 'multipart/x-mixed-replace; boundary=frame')


def displayNorth(request):
    template = loader.get_template('display_north.html')
    return HttpResponse(template.render())

def vidStreamNorth():
    #frame = cv.imread('trafficTest2.jpeg')
    while True:
        frame = cv.imread('trafficTest3.jpeg')
        image_bytes = cv.imencode('.jpg',frame)[1].tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        
def videoFeedNorth(request):
    return StreamingHttpResponse(vidStreamNorth(),content_type = 'multipart/x-mixed-replace; boundary=frame')


def displaySouth(request):
    template = loader.get_template('display_south.html')
    return HttpResponse(template.render())

def vidStreamSouth():
    #frame = cv.imread('trafficTest2.jpeg')
    while True:
        frame = cv.imread('trafficTest5.jpeg')
        image_bytes = cv.imencode('.jpg',frame)[1].tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
        
def videoFeedSouth(request):
    return StreamingHttpResponse(vidStreamSouth(),content_type = 'multipart/x-mixed-replace; boundary=frame')