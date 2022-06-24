from zdm import zdm
from bsp import board

from components.dht11 import DHT11
from components.bmp180 import bmp180

from libs.lcd import lcd
from libs.hallSensor import hallSensor
from libs.arducam import arduchip, OV2640, arducam_setup
from libs.keypad import keypad
from libs.stepper import stepper

from networking import wifi
from networking import wifi
from protocols import http, mqtt, ntp

import mcu
import json
import adc
import gpio
import threading
import time



def floatToString(value, precision):                                                                        #convert float to string with given precision
    s = str(value)
    i = s.find('.')
    s1 = s[:i]
    s2 = s[i+1:]
    s2 = s2[:precision]
    return s1 + '.' + s2

def measureWindSpeed():
    global windSpeed
    i = 0
    oldWind = None                                                                                          #variable to store the last read value
    oldTime = None
    wind = hallSensor.hallSensor(33)
    while True:
        try:
            newWind = wind.read()
        except Exception as e:
            print(e)

        if newWind is None: continue

        if oldWind is 1 and newWind is 0:                                                                   #trigger the measurement on falling edge
            i = 0
            # print("ok")
            if oldTime is None:
                oldTime = time.millis()
            else:
                newTime = time.millis()
                windLock.acquire()
                windSpeed = 628/(newTime - oldTime)                                                         #calculate the wind speed using a lock for thread safety
                windLock.release()
                oldTime = newTime
        oldWind = newWind
        i+=1
        if i > 5000:
            i = 0
            windSpeed = 0
        sleep(5)

def httpSend():
    global measureBuffer
    while True:
        sleep(500)
        bufferLock.acquire()                                                                                #lock the buffer for thread safety
        if len(measureBuffer) < 10:
            bufferLock.release()
            continue
        httpBuffer=measureBuffer                                                                            #copy the buffer to a local variable
        measureBuffer.clear()
        bufferLock.release()                                                                                #unlock the buffer after clearing it
        try:
            conn = http.HTTP()                                                                              #create a new HTTP connection
            res = conn.post("SERVER_ADDRESS", body=json.dumps(httpBuffer))            #send the data to the server
            print("Sent")
        except Exception as e:
            print(e)
        if res.data != "OK":                                                                                #if the server returns an error, print it
            print("Error: " + res.data)
        conn.destroy()                                                                                      #destroy the connection
        httpBuffer.clear()                                                                                  #clear the copy buffer

def main():
    global measureBuffer
    global windSpeed

    try:                                                                                                    #try to initialize the bmp180 sensor
        bmp.init()
    except Exception as e:                                                                                  #if something goes wrong, print the error
        bmp = None
        print(e)

    oldHum, oldTemp, oldPressure, oldWindSpeed = None, None, None, None

    while True:

        hum =40.3;
        temp = bmp.get_temp()                                                                               #read the dht11 sensor
        pres =  bmp.get_pres()                                                                              #read the pressure sensor

        windLock.acquire()
        wind_speed = windSpeed
        windLock.release()

        #print data to the console
        print("Temp:" + floatToString(temp, 1) + "C" + " Hum:" + floatToString(hum, 1) + "%" + " Pressure:" + floatToString(pres/1000, 1) + "kPa" + " WindSpeed:" + floatToString(wind_speed, 1) + "m/s")

        #if there is new data, print it on the LCD
        if oldTemp is not temp:
            lcd.setCursorPosition(0, 0)
            lcd.writeString("T: " + floatToString(temp, 1) + "C")
            oldTemp = temp
        if oldPressure is not pres:
            lcd.setCursorPosition(9, 0)
            lcd.writeString("P: " + floatToString(pres/1000, 1) + "kPa")
            oldPressure = pres
        if oldHum is not hum:
            lcd.setCursorPosition(0, 1)
            lcd.writeString("H: " + str(int(hum)) + "%")
            oldHum = hum
        if oldWindSpeed is not wind_speed:
            lcd.setCursorPosition(7, 1)
            lcd.writeString("W: " + floatToString(wind_speed, 1) + "m/s")
            oldWindSpeed = wind_speed

        new = {"temp": temp, "hum": hum, "pres": pres, "windspeed": wind_speed}

        bufferLock.acquire()
        measureBuffer.append(new)
        bufferLock.release()

        try:
            agent.publish(new, "measurements")
        except Exception as e:
            print(e)

        sleep(2000)                                                                                             #DHT readings are pretty slow, so we wait a bit to avoid overloading the sensor


def sendPhoto():
    while True:
        buf = arduchip.take_photo()
        print("Sending...")
        try:
            conn = http.HTTP()
            res = conn.post(CAM_ROUTE,body=bytes(buf),  headers={'Content-Type': 'application/octet-stream'})
            if res.status == 200:
                lock(False)
                break
            else:
                print("unauthorized")
            conn.destroy()
        except Exception as e:
            print(e)
        sleep(1000)

def readKey():
    global n
    while True:
        lock.acquire()
        n = kp.get_key()
        lock.release()
        sleep(1)

def accessKey():
    global psw
    while True:
        lock.acquire()
        gpio.mode(greenLed, OUTPUT)
        gpio.mode(redLed, OUTPUT)
        if len(psw) >= 4:
            if psw in accessPsw:
                print("Access granted")
                lock(False)
                psw = []
                gpio.set(greenLed, HIGH)
                sleep(3000)
            else:
                print("Access denied")
                psw = []
                gpio.set(redLed, HIGH)
                sleep(3000)
        lock.release()
        sleep(200)
        gpio.set(greenLed, LOW)
        gpio.set(redLed, LOW)

def printKey():
    global n
    while True:
        lock.acquire()
        if n is not None:
            print(n)
            n = None
        lock.release()
        sleep(200)

def costPsw():
    global psw,n
    while True:
        lock.acquire()
        if n is not None:
            psw.append(n)
        lock.release()
        sleep(200)

def lock(closed):
    global lock_closed
    lock_closed = closed
    if closed:
        stepper.rotate(360, 1)
    else:
        stepper.rotate(360, 0)

########################################################################################################################this code runs at the start of the program########################################################################################################################

try:                                                                                                            #try connecting to the wifi network
    wifi.configure(
        ssid = "Nick",
        password="ciao1234")
    wifi.start()
    ntp.sync_time()
    print(wifi.info())                                                                                          #print the wifi info
except Exception as e:                                                                                          #if something goes wrong, print the error
        print("wifi exec",e)

print("Initializing camera...")

stepper = stepper.Stepper(14, 13, 22, 9)

kp = keypad.KEYPAD([D25, D33, D32, D35],[D15, D2, D19, D21])

accessPsw = [
    [5,2,4,6],
    [5,3,4,6],
    [2,3,4,5],
    [6,7,8,5]
]
psw = []
greenLed = D26
redLed = D27
n = None

arduchip = arduchip.Arduchip(nss=D5)
internal_sensor = OV2640.OV2640()
arducam_setup.init_camera(arduchip, internal_sensor)

SERVER_IP = ""
SERVER_PORT = ""
SERVER_ROUTE = ""

CAM_ROUTE = SERVER_IP + ":" + SERVER_PORT + SERVER_ROUTE

windSpeed = 0                                                                                                   #initialize the wind speed to 0
measureBuffer = []                                                                                              #initialize the buffer for the measurements

bufferLock = threading.Lock()
windLock = threading.Lock()
lock = threading.Lock()

lcd = lcd.LCD(I2C0)
dhtPin = D18
bmp = bmp180.BMP180(I2C0)
agent = zdm.Agent()

windSpeedThread = threading.Thread(target=measureWindSpeed)                                                     #create a thread to measure the wind speed
httpThread = threading.Thread(target=httpSend)                                                                  #create a thread to send the measurements to the server
mainThread = threading.Thread(target=main)                                                                      #create a thread for the main function

camThread = threading.Thread(target=sendPhoto)                                                                  #create a thread to send the photo to the server

keyThread = threading.Thread(target=readKey)
accessThread = threading.Thread(target=accessKey)
costThread = threading.Thread(target=costPsw)
printThread = threading.Thread(target=printKey)

try:                                                                                                            #try to establish a connection to ZDM
    agent.start()
except Exception as e:
    print(e)

windSpeedThread.start()                                                                                         #start all the threads
mainThread.start()
httpThread.start()
camThread.start()

keyThread.start()
costThread.start()
printThread.start()
accessThread.start()
