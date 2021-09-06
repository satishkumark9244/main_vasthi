import json
import boto3
import uuid
# import ast
import decimal
# import html
import pystache
from boto3.dynamodb.conditions import Key, Attr
from dynamodb_json import json_util as util
import time
import datetime
import pytz


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def render_html(filename):
    template = open(filename).read()
    html = pystache.render(template)
    return html


def lambda_handler(event, context):
    global response, dynamodb
    print(event)
    responseText = ""
    dynamodb = boto3.resource('dynamodb')
    try:
        url = event['queryStringParameters']['url']
    except:
        url = ""

    print("")
    table = dynamodb.Table('vasthi_enviro_site')

    if url == "login":
        responseText = render_html("login.html") + render_html("script.html")
    elif url == "dashboard":
        responseText = render_html("header.html") + render_html("dashboard.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "readings":
        responseText = render_html("header.html") + render_html("readings.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "remote_calibration":
        responseText = render_html("header.html") + render_html("remote_calibration.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "calibration_graph":
        responseText = render_html("header.html") + render_html("calibration_graph.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "download_page":
        responseText = render_html("header.html") + render_html("download_page.html") + render_html(
            "websql.html") + render_html("script.html") + render_html("footer_download.html")
    elif url == "industry_report_page":
        responseText = render_html("header.html") + render_html("industry_report_page.html") + render_html(
            "script.html")
    elif url == "stationlist":
        responseText = render_html("header.html") + render_html("stationlist.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "license_renew":
        responseText = render_html("header.html") + render_html("license_renew.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "report_view":
        responseText = render_html("header.html") + render_html("report_view.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "industry_report":
        responseText = render_html("header.html") + render_html("industry_report.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "allstations":
        responseText = render_html("header.html") + render_html("all_stations.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "graph_view":
        responseText = render_html("header.html") + render_html("graph_view.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "graph_view_main":
        responseText = render_html("header.html") + render_html("graphviewmain.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "readingdata":
        responseText = render_html("header.html") + render_html("readingdata.html") + render_html("script.html")
    elif url == "stationview":
        responseText = render_html("header.html") + render_html("stationview.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "stationviewalldata":
        responseText = render_html("header.html") + render_html("stationviewalldata.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "camera_view":
        responseText = render_html("header.html") + render_html("stream.html") + render_html(
            "script.html") + render_html("footer.html")
    elif url == "api":
        responseText1 = ""
        try:
            data = json.loads(event['body'])
            cmd = data['cmd']
        except:
            cmd = "7"
            print("sss")
        if cmd == "1":  # site/plant creation
            industry_id = data['industry_id']
            sort_key = data['sort_key']
            industry_name = data['industry_name']
            industry_cat = data['industry_cat']
            industry_type = data['industry_type']
            industry_mis_id = data['industry_mis_id']
            site_address = data['site_address']
            remote_calibration = data['remote_calibration']
            camera = data['camera']
            schedule = data['schedule']
            city = data['city']
            district = data['district']
            state = data['state']
            pincode = data['pincode']
            installed_pc = data['installed_pc']
            contact_name = data['contact_name']
            designation = data['designation']
            mobile = data['mobile']
            email = data['email']
            user_name = data['user_name']
            password = data['password']
            stations = data['stations']
            analyser_details = data['analyser_details']
            other_mobile = data['other_mobile']
            gturl = data['gturl']
            gtemail = data['gtemail']
            gtpassword = data['gtpassword']
            cameraurl = data['cameraurl']

            response = ""
            response = table.put_item(Item={
                'industry_id': industry_id,
                'sort_key': sort_key,
                'industry_name': industry_name,
                'industry_cat': industry_cat,
                'industry_type': industry_type,
                'industry_mis_id': industry_mis_id,
                'remote_calibration': remote_calibration,
                'camera': camera,
                'schedule': schedule,
                'site_address': site_address,
                'city': city,
                'district': district,
                'state': state,
                'pincode': pincode,
                'installed_pc': installed_pc,
                'contact_name': contact_name,
                'designation': designation,
                'mobile': mobile,
                'email': email,
                'user_name': user_name,
                'password': password,
                'stations': stations,
                'analyser_details': analyser_details,
                'other_mobile': other_mobile,
                'gturl': gturl,
                'gtemail': gtemail,
                'gtpassword': gtpassword,
                'cameraurl': cameraurl,

            })
            print(response)
            responseText1 = "success"
        elif cmd == "2":  # return all site/plant data
            response = table.scan()
            responseText1 = json.dumps(response['Items'])
            print(responseText1)
        elif cmd == "3":
            table = dynamodb.Table('vasthi_enviro_site_readings')
            industry_id = data['industry_id']
            station_id = data['station_id']
            device_id = data['device_id']
            reading = data['reading']
            parameter_id = data['parameter_id']
            analyser_id = data['analyser_id']
            datentime = data['datentime']
            try:
                unit = data['unit']
            except():
                unit = ""

            ts = time.time()
            time1 = str(ts)[0:10]
            response = table.put_item(Item={
                'industry_id': industry_id,
                'station_id': "STATION_" + str(station_id) + "#" + time1,
                'device_id': device_id,
                'reading': reading,
                'parameter_id': parameter_id,
                'analyser_id': analyser_id,
                'datentime': datentime,
                'unit': unit,
            })
            # print(response)xkdskdjskjdsk
            responseText1 = "success"
        elif cmd == "4":  # return all site/plant data
            industry_id = data['industry_id']
            station_id = data['station_id']
            datentime = data['datentime']
            table = dynamodb.Table('vasthi_enviro_site_readings')
            response = table.query(
                KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').begins_with(
                    station_id),
                FilterExpression=Attr('datentime').begins_with(datentime)
            )
            responseText1 = json.dumps(response['Items'])
            # print("****************")
            # print(responseText1)
            # print("****************")
            # updatedddd-24

        elif cmd == "555":  # return all site/plant data
            industry_id = data['industry_id']
            station_id = data['station_id']
            analyser_id = data['analyser_id']
            datentime = data['datentime']
            table = dynamodb.Table('vasthi_enviro_site_readings')
            response = table.query(
                KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').begins_with(
                    station_id),
                FilterExpression=Attr('datentime').begins_with(datentime) & Attr('analyser_id').contains(analyser_id)
            )
            responseText1 = json.dumps(response['Items'])
            print("****************")
            print(responseText1)
            print("****************")
        elif cmd == "5":  # return data in this day for table and graph view
            industry_id = data['industry_id']
            station_id = data['station_id']
            analyser_id = data['analyser_id']
            datentime = data['datentime']
            table = dynamodb.Table('vasthi_enviro_site_readings')

            toUnixTime = str(time.time())[0:10]
            just_date = int(datetime.datetime.now().strftime("%d"))-1
            just_month = int(datetime.datetime.now().strftime("%m"))
            # just_date = 31
            # just_month = 8
            just_year = int(datetime.datetime.now().strftime("%Y"))
            fromUnixTime = str(datetime.datetime(just_year, just_month, just_date, 18, 30).timestamp())[:-2]


            response = table.query(
                KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').between(station_id+"#"+fromUnixTime, station_id+"#"+toUnixTime)
                    # .begins_with(str(station_id))
                # FilterExpression=Attr('datentime').begins_with(str(datentime)) & Attr('analyser_id').contains(str(analyser_id))
            )
            responseText1 = json.dumps(response['Items'])
            print("****************")
            print(responseText1)
            print("****************")
        elif cmd == "6":  # return all
            email = data['email']
            password = data['password']
            table = dynamodb.Table('vasthi_enviro_site')
            response = table.scan(
                FilterExpression=Attr('email').eq(str(email)) & Attr('password').eq(str(password))
            )
            count = response['Count']
            if count > 0:
                responseText1 = json.dumps(response['Items'])
            else:
                responseText1 = "fail"
        elif cmd == "77":  # return all site/plant data
            table = dynamodb.Table('vasthi_enviro_site')
            response = table.scan(
                FilterExpression=Key('industry_id').begins_with(str("SITE"))
            )

            responseText1 = json.dumps(response['Items'])

        elif cmd == "78":  # return all site/plant data
            industry_id = data['industry_id']
            license_to = data['license_to']
            license_from = data['license_from']
            print("------------------here-----------")
            print(industry_id)
            print("------------------here-----------")
            update_license(industry_id, license_to, license_from)
            responseText1 = {
                "status": 1,

            }


        elif cmd == "777":  # return all site/plant data
            industry_id = data['industry_id']
            station_id = data['station_id']
            analyser_id = data['analyser_id']
            datentime = data['datentime']
            table = dynamodb.Table('vasthi_enviro_site_readings')
            array_to_send = []
            for i in range(0, len(analyser_id)):
                try:
                    response = table.query(
                        KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').begins_with(
                            "STATION_" + str(station_id[i])),
                        # FilterExpression=Attr('datentime').begins_with(datentime) & Attr('analyser_id').eq(
                        # analyser_id[i]),
                        Limit=1,
                        ScanIndexForward=False,
                    )
                    print(response)
                except:
                    print("")
                try:
                    array_to_send.append(json.dumps(response['Items'][0]))
                except:
                    nullarray = []
                    array_to_send.append(nullarray)
            responseText1 = str(array_to_send).replace("'", " ")
            print("****************")
            print(responseText1)
            print("****************")
        elif cmd == "7":  # return live site details for last 30 min newly created to show NA in website
            industry_id = data['industry_id']
            station_id = data['station_id']
            analyser_id = data['analyser_id']
            datentime = data['datentime']
            table = dynamodb.Table('vasthi_enviro_site_readings')

            array_to_send = []
            if industry_id == "SITE_100000":#for testing delete this condition laTER
                # todate_minus = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) - datetime.timedelta(minutes=15)
                # todate = todate_minus.strftime("%Y-%m-%d %H:%M:%S")
                # fromdate_minus = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) - datetime.timedelta(minutes=30)
                # fromdate = fromdate_minus.strftime("%Y-%m-%d %H:%M:%S")

                todate_minus = datetime.datetime.now() - datetime.timedelta(minutes=15)
                just_date_to = int(todate_minus.strftime("%d"))
                just_month_to = int(todate_minus.strftime("%m"))
                just_year_to = int(todate_minus.strftime("%Y"))
                just_hour_to = int(todate_minus.strftime("%H"))
                just_min_to = int(todate_minus.strftime("%M"))
                todate = str(datetime.datetime(just_year_to, just_month_to, just_date_to, just_hour_to, just_min_to).timestamp())[:-2]

                fromdate_minus = datetime.datetime.now() - datetime.timedelta(minutes=30)
                just_date_from = int(fromdate_minus.strftime("%d"))
                just_month_from = int(fromdate_minus.strftime("%m"))
                just_year_from = int(fromdate_minus.strftime("%Y"))
                just_hour_from = int(fromdate_minus.strftime("%H"))
                just_min_from = int(fromdate_minus.strftime("%M"))
                fromdate = str(datetime.datetime(just_year_from, just_month_from, just_date_from, just_hour_from,
                                               just_min_from).timestamp())[:-2]

            else:
                # todate = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
                # fromdate_minus = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) - datetime.timedelta(minutes=15)
                # fromdate = fromdate_minus.strftime("%Y-%m-%d %H:%M:%S")

                todate = str(time.time())[0:10]

                fromdate_minus = datetime.datetime.now() - datetime.timedelta(minutes=15)
                just_date_from = int(fromdate_minus.strftime("%d"))
                just_month_from = int(fromdate_minus.strftime("%m"))
                just_year_from = int(fromdate_minus.strftime("%Y"))
                just_hour_from = int(fromdate_minus.strftime("%H"))
                just_min_from = int(fromdate_minus.strftime("%M"))
                fromdate = str(datetime.datetime(just_year_from, just_month_from, just_date_from, just_hour_from,
                                                 just_min_from).timestamp())[:-2]

            for i in range(0, len(analyser_id)):
                try:
                    response = table.query(
                        KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').between(
                            "STATION_" + str(station_id[i])+"#"+fromdate,"STATION_" + str(station_id[i])+"#"+todate),
                        # FilterExpression=Attr('datentime').between(fromdate, todate),
                        # FilterExpression=Attr('datentime').begins_with(datentime) & Attr('analyser_id').eq(
                        # analyser_id[i]),
                        # Limit=1,
                        # ScanIndexForward=False,
                    )
                    print(response)
                except:
                    print("")
                try:
                    array_to_send.append(json.dumps(response['Items'][0]))
                except:
                    nullarray = []
                    array_to_send.append(nullarray)
            # array_to_send.append(industry_id)
            # array_to_send.append("STATION_" + str(station_id[0]))
            # array_to_send.append(fromdate)
            # array_to_send.append(todate)
            # array_to_send.append("STATION_" + str(station_id[0])+"#"+fromdate)
            # array_to_send.append("STATION_" + str(station_id[0])+"#"+todate)

            responseText1 = str(array_to_send).replace("'", " ")
            print("****************")
            print(responseText1)
            print("****************")
        elif cmd == '70':
            responseText1 = "{ \"site_details\":\"all site details induvidually\", \"stations\":[ {\"stationorstack_name\":\"station1\",\"station_id\":\"station1_id\",\"monitoring_id\":\"monitor1\",\"analysers\":[\"analyser1\",\"analyser2\",\"analyser3\"]}, {\"stationorstack_name\":\"station2\",\"station_id\":\"station2_id\",\"monitoring_id\":\"monitor2\",\"analysers\":[\"analyser4\",\"analyser5\",\"analyser6\"]}, {\"stationorstack_name\":\"station3\",\"station_id\":\"station3_id\",\"monitoring_id\":\"monitor3\",\"analysers\":[\"analyser7\",\"analyser8\",\"analyser9\"]} ], \"analyser_details\":[ {\"analyser_id\":\"analyser1\", \"parameters\":[ {\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}, {\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}] }, {\"analyser_id\":\"analyser2\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser3\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser4\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser5\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser6\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser7\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser8\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]}, {\"analyser_id\":\"analyser9\",\"parameters\":[{\"parameter_name\":\"SO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"},{\"parameter_name\":\"CO2\",\"parameter_unit\":\"PPM\",\"max_range\":\"1000\",\"min_range\":\"0\"}]} ] }"
        elif cmd == '71':
            responseText1 = "{\"station_id\":\"STATION_SMS_SECONDRY_INDUSTRY2#1621245517\",\"analyser_id\":[\"V120210077\",\"V120210070\"],\"parameter_id\":[[\"SO\",\"NO\",\"CO\"],[\"SO\",\"NO\",\"CO\"]],\"device_id\":\"JHE01\",\"industry_id\":\"SITE_1\",\"datentime\":\"2021-05-17 15:12:11.614\",\"reading\":[[\"42.722\",\"40.722\",\"43.722\"],[\"44.722\",\"45.722\",\"46.722\"]]}"
            # industry_id = data['industry_id']
            # datentime = data['datentime']
            # table = dynamodb.Table('vasthi_enviro_site_readings')
            # response = table.query(
            #     KeyConditionExpression=Key('industry_id').eq(str(industry_id)) & Key('station_id').begins_with(
            #         station_id),
            #     FilterExpression=Attr('datentime').begins_with(datentime) & Attr('analyser_id').eq(analyser_id)
            # )
            # responseText1 = json.dumps(response['Items'])
            # print("****************")
            # print(responseText1)
            # print("****************")
        elif cmd == "79":
            industry_id = data['industry_id']
            station_id = data['station_id']
            fromdate = data['fromdate']
            todate = data['todate']
            table = dynamodb.Table('vasthi_enviro_site_readings')
            try:
                response = table.query(
                    KeyConditionExpression=Key('industry_id').eq(industry_id) & Key('station_id').between(fromdate,
                                                                                                          todate)
                )
            except():
                response = table.query(
                    KeyConditionExpression=Key('industry_id').eq(industry_id) & Key('station_id').between(todate,
                                                                                                          fromdate)
                )

            responseText1 = json.dumps(response['Items'])
            print("****************")
            print(responseText1)
            print("****************")

        elif cmd == "80":
            industry_id = data['industry_id']
            fromdate = data['fromdate']
            todate = data['todate']
            table = dynamodb.Table('vasthi_enviro_site_readings')
            try:
                response = table.query(
                    KeyConditionExpression=Key('industry_id').eq(industry_id),
                    FilterExpression=Attr('datentime').between(fromdate, todate)
                )
            except():
                response = table.query(
                    KeyConditionExpression=Key('industry_id').eq(industry_id),
                    FilterExpression=Attr('datentime').between(todate, fromdate)
                )

            responseText1 = json.dumps(response['Items'])
            print("****************")
            print(responseText1)
            print("****************")
        responseText = str(responseText1)
    else:
        responseText = render_html("login.html") + render_html("script.html")

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "multiValueHeaders": {
            "X-Test-Header": ["baking experiment"],
            "Content-Type": ["text/html", "text/plain"]
        },
        "body": responseText,
    }


def update_license(industry_id, license_to, license_from):
    table = dynamodb.Table('vasthi_enviro_site')

    response = table.update_item(
        Key={
            'industry_id': industry_id,
            'sort_key': "1",
        },
        UpdateExpression="set license_to=:license_to, license_from=:license_from",
        ExpressionAttributeValues={
            ':license_to': str(license_to),
            ':license_from': str(license_from)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
