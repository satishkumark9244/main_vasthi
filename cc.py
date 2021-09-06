#!/usr/bin/env python3
import json

import os
import sys
import psutil
import logging
import zipfile
import time
import requests
import csv
import time
from config import *
from random import randrange
from pip._vendor import requests
import random
import configuration_modbus as CONF
import util as UTIL
import serial
#from datetime import datetime
from datetime import timedelta
import time
import math
#from datetime import datetime as dt
#from datetime import datetime, timedelta
#import datetime
from datetime import datetime
DEVICE_ID = ""
emptyRXReceivedCount = 0
global parameter_array_for_avg
global count_for_avg
parameter_array_for_avg = []
count_for_avg = 0






def sendRequest():


    while True:


        try:
            time_minus_16 = datetime.now() - timedelta(minutes=16)
            vender_id = "14"
            timestamp1 = str(time_minus_16)[0:-9]
            timestamp = timestamp1+"00"
            flag = "1"

            datetimex = time_minus_16
            datetime_main = str(datetimex)
            minutes = datetime_main[14:16]
            standarddateformat = datetime_main[0:17] + "00"
            print(minutes)
            print(timestamp)
            print("222222222222222222222222")

            if minutes == '00' or minutes == '15' or minutes == '30' or minutes == '45':
                sendParameterValue11 =round(random.uniform(130.000, 130.999), 3)
                sendParameterValue12 =round(random.uniform(21.000, 21.999), 3)
                sendParameterValue13 =round(random.uniform(5.000, 5.999), 3)
                sendParameterValue14 =round(random.uniform(33.000, 42.999), 3)
                multipl_parameters4 = str(sendParameterValue11) +","+str(sendParameterValue12)+","+str(sendParameterValue13)+","+str(sendParameterValue14)
                url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                vender_id) + "&industry_id=SITE_1&stationId=WHRB1&analyserId=VE202100149,V120210076&processValue=" + multipl_parameters4 + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3,mg/Nm3,mg/Nm3,mg/Nm3&parameter=SO2,NOX,CO,SPM"
                print(url)
                response = requests.get(url)
                print(response.text)


                url = "https://beta.vasthienviro.com/?url=api"
                data = {
                    "industry_id": "SITE_1",
                    "station_id": "WHRB1",
                    "reading": [[str(sendParameterValue11),str(sendParameterValue12),str(sendParameterValue13)],[str(sendParameterValue14)]],
                    "analyser_id": ["VE202100149","V120210076"],
                    "parameter_id": [["SO2", "NOX", "CO"],["SPM"]],
                    "device_id": "JHE01",
                    "datentime": str(timestamp),
                    "cmd": "3",
                    "unit": [["mg/Nm3", "mg/Nm3", "mg/Nm3"],["SPM"]]
                }
                resp = requests.post(url, json=data)
                print(resp.text)




                sendParameterValue4 =round(random.uniform(173.000, 173.999), 3)
                sendParameterValue5 =round(random.uniform(109.000, 109.999), 3)
                sendParameterValue6 =round(random.uniform(20.000, 30.999), 3)
                multipl_parameters = str(sendParameterValue4) +","+str(sendParameterValue5)+","+str(sendParameterValue6)
                url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                vender_id) + "&industry_id=SITE_1&stationId=BF3_STOVE_FLUE_STACK&analyserId=VE202100146&processValue=" + multipl_parameters + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3,mg/Nm3,mg/Nm3&parameter=SO2,NOX,CO"
                print(url)
                response = requests.get(url)
                print(response.text)

                url = "https://beta.vasthienviro.com/?url=api"
                data = {
                    "industry_id": "SITE_1",
                    "station_id": "BF3_STOVE_FLUE_STACK",
                    "reading": [[str(sendParameterValue4),str(sendParameterValue5),str(sendParameterValue6)]],
                    "analyser_id": ["VE202100146"],
                    "parameter_id": [["SO2","NOX","CO"]],
                    "unit":[["mg/Nm3","mg/Nm3","mg/Nm3"]],
                    "device_id":"JE04",
                    "datentime":str(timestamp),
                    "cmd":"3"
                }
                print(data)
                resp = requests.post(url, json=data)
                print(resp.text)

                # time_minus_16 = datetime.now() - timedelta(minutes=16)
                # vender_id = "14"
                sendParameterValue7 =round(random.uniform(163.000, 164.999), 3)
                sendParameterValue8 =round(random.uniform(40.000, 41.999), 3)
                sendParameterValue9 =round(random.uniform(28.000, 29.999), 3)
                multipl_parameters1 = str(sendParameterValue7) +","+str(sendParameterValue8)+","+str(sendParameterValue9)
                url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                vender_id) + "&industry_id=SITE_1&stationId=BF2_STOVE_FLUE_STACK&analyserId=VE202100150&processValue=" + multipl_parameters1 + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3,mg/Nm3,mg/Nm3&parameter=SO2,NOX,CO"
                print(url)
                response = requests.get(url)
                print(response.text)

                url = "https://beta.vasthienviro.com/?url=api"
                data = {
                    "industry_id": "SITE_1",
                    "station_id": "BF2_STOVE_FLUE_STACK",
                    "reading": [[str(sendParameterValue7),str(sendParameterValue8),str(sendParameterValue9)]],
                    "analyser_id": ["VE202100150"],
                    "parameter_id": [["SO2","NOX","CO"]],
                    "unit":[["mg/Nm3","mg/Nm3","mg/Nm3"]],
                    "device_id":"JE04",
                    "datentime":str(timestamp),
                    "cmd":"3"
                }
                print(data)
                resp = requests.post(url, json=data)
                print(resp.text)
                # timestamp = str(time_minus_16)[0:-3]


                flag = "1"
                sendParameterValue17 =round(random.uniform(37.000, 43.999), 3)
                multipl_parameters2 = str(sendParameterValue17)
                url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                vender_id) + "&industry_id=SITE_1&stationId=BF2_STOCK_HOUSE_DE_DUSTING&analyserId=V120210070&processValue=" + multipl_parameters2 + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                print(url)
                response = requests.get(url)
                print(response.text)

                url = "https://beta.vasthienviro.com/?url=api"
                data = {
                    "industry_id": "SITE_1",
                    "station_id": "BF2_STOCK_HOUSE_DE_DUSTING",
                    "reading": [[str(sendParameterValue17)]],
                    "analyser_id": ["V120210070"],
                    "parameter_id": [["SPM"]],
                    "unit":[["mg/Nm3"]],
                    "device_id":"JE04",
                    "datentime":str(timestamp),
                    "cmd":"3"
                }
                print(data)
                resp = requests.post(url, json=data)
                print(resp.text)

                # sendParameterValue6 =round(random.uniform(20.000, 27.999), 3)
                # multipl_parameters = str(sendParameterValue6)
                # url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                # vender_id) + "&industry_id=SITE_1&stationId=SINTER_PROPORTIONATE&analyserId=V120210047&processValue=" + multipl_parameters + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                # print(url)
                # response = requests.get(url)
                # print(response.text)
                # time.sleep(10)
                # url = "https://beta.vasthienviro.com/?url=api"
                # data = {
                #     "industry_id": "SITE_1",
                #     "station_id": "SINTER_PROPORTIONATE",
                #     "reading": [[multipl_parameters]],
                #     "analyser_id": ["V120210047"],
                #     "parameter_id": [["SPM"]],
                #     "unit":[["mg/Nm3"]],
                #     "device_id":"JE04",
                #     "datentime":str(timestamp),
                #     "cmd":"3"
                # }
                # print(data)
                # resp = requests.post(url, json=data)
                # print(resp.text)
                #
                #
                #
                #
                # time.sleep(10)
                # time_minus_16 = datetime.now() - timedelta(minutes=16)
                # vender_id = "14"
                #
                # timestamp = str(time_minus_16)[0:-3]
                # flag = "1"
                #
                # sendParameterValue6 =round(random.uniform(17.000, 34.999), 3)
                # multipl_parameters = str(sendParameterValue6)
                # url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                # vender_id) + "&industry_id=SITE_1&stationId=Sinter_Discharge_End2&analyserId=V120210049&processValue=" + multipl_parameters + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                # print(url)
                # response = requests.get(url)
                # print(response.text)
                # time.sleep(10)
                # url = "https://beta.vasthienviro.com/?url=api"
                # data = {
                #     "industry_id": "SITE_1",
                #     "station_id": "Sinter_Discharge_End2",
                #     "reading": [[multipl_parameters]],
                #     "analyser_id": ["V120210049"],
                #     "parameter_id": [["SPM"]],
                #     "unit":[["mg/Nm3"]],
                #     "device_id":"JE04",
                #     "datentime":str(timestamp),
                #     "cmd":"3"
                # }
                # print(data)
                # resp = requests.post(url, json=data)
                # print(resp.text)
                # time.sleep(200)

                sendParameterValue1 =round(random.uniform(17.33, 24.66), 2)

                # url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                # vender_id) + "&industry_id=SITE_2&stationId=HT_Furnace_Stack_B_Shed_1&analyserId=V120210075&processValue=" + str(sendParameterValue1) + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                # print(url)
                # response = requests.get(url)
                # print(response.text)
                #
                # url = "https://beta.vasthienviro.com/?url=api"
                # data = {
                #     "industry_id": "SITE_3",
                #     "station_id": "HT_Furnace_Stack_B_Shed_1",
                #     "reading": [[str(sendParameterValue1)]],
                #     "analyser_id": ["V120210075"],
                #     "parameter_id": [["SPM"]],
                #     "unit":[["mg/Nm3"]],
                #     "device_id":"JE04",
                #     "datentime":str(timestamp),
                #     "cmd":"3"
                # }
                # print(data)
                # resp = requests.post(url, json=data)
                # print(resp.text)

                # sendParameterValue2 =round(random.uniform(17.33, 24.66), 2)
                # url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                # vender_id) + "&industry_id=SITE_2&stationId=Water_Dry_Off_Oven&analyserId=V120210073&processValue=" + str(sendParameterValue2) + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                # print(url)
                # response = requests.get(url)
                # print(response.text)
                #
                # url = "https://beta.vasthienviro.com/?url=api"
                # data = {
                #     "industry_id": "SITE_3",
                #     "station_id": "Water_Dry_Off_Oven",
                #     "reading": [[str(sendParameterValue2)]],
                #     "analyser_id": ["V120210073"],
                #     "parameter_id": [["SPM"]],
                #     "unit":[["mg/Nm3"]],
                #     "device_id":"JE04",
                #     "datentime":str(timestamp),
                #     "cmd":"3"
                # }
                # print(data)
                # resp = requests.post(url, json=data)
                # print(resp.text)

                # sendParameterValue3 =round(random.uniform(17.33, 24.66), 2)
                # sendParameterValue2 =round(random.uniform(17.33, 24.66), 2)
                # url = "https://jsac.jharkhand.gov.in/pollution/WebService.asmx/getdata?vender_id=" + str(
                # vender_id) + "&industry_id=SITE_2&stationId=Hot_Water_Generator&analyserId=V120210071&processValue=" + str(sendParameterValue2) + "&scaledValue=1000&flag=1&timestamp=" + str(timestamp) + "&unit=mg/Nm3&parameter=SPM"
                # print(url)
                # response = requests.get(url)
                # print(response.text)
                #
                # url = "https://beta.vasthienviro.com/?url=api"
                # data = {
                #     "industry_id": "SITE_3",
                #     "station_id": "Hot_Water_Generator",
                #     "reading": [[str(sendParameterValue3)]],
                #     "analyser_id": ["V120210071"],
                #     "parameter_id": [["SPM"]],
                #     "unit":[["mg/Nm3"]],
                #     "device_id":"JE04",
                #     "datentime":str(timestamp),
                #     "cmd":"3"
                # }
                # print(data)
                # resp = requests.post(url, json=data)
                # print(resp.text)



            time.sleep(30)

        except Exception as e:
            print("eeeeeeeeeeeeeeeeeeee"+str(e))
            time.sleep(10)

       # data = {"parameters": parameters, "device_id": ""+DEVICE_ID}





def average(a, n):
    # Find sum of array element
    sum = 0
    for i in range(n):
        try:
            sum += float(a[i])
        except Exception as e:
            print("")
            n= n-1
            if n==0:
                n=1

    return sum / n





if __name__ == '__main__':
    sendRequest()