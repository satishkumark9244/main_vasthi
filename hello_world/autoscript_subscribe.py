import time as t
import json

import AWSIoTPythonSDK.MQTTLib as AWSIotPyMQTT

def callback(client, userdata, message):
    print("custom1111")


myAWSIoTMQTTClient = AWSIotPyMQTT.AWSIoTMQTTClient("vasthienviroiot1")
myAWSIoTMQTTClient.configureEndpoint('aj99nsf392yjz-ats.iot.ap-south-1.amazonaws.com', 8883)
myAWSIoTMQTTClient.configureCredentials('certificates/root.pem', 'certificates/bc150401ad-private.pem.key',
                                        'certificates/bc150401ad-certificate.pem.crt')

myAWSIoTMQTTClient.connect()

# print('Begin Publish')

# for i in range(5):
#     message = '{"industry_id": "AASITEABCD", "sort_key": "10", "user_name": ' \
#               '"seema.kumari@vedanta.co.in" } '
#     myAWSIoTMQTTClient.publish("test", message, 1)
#     print("published:" + str(i + 1))
#     t.sleep(0.1)

# print("publish end")

# myAWSIoTMQTTClient.disconnect()


# myAWSIoTMQTTClient.subscribe("myTopic/#", 1, ackCallback=mySubackCallback, messageCallback=customMessageCallback)
while True:
    myAWSIoTMQTTClient.subscribe("test", 1, callback)
    t.sleep(60)
    print("done")

#
 #pip install AWSIoTPythonSDK


