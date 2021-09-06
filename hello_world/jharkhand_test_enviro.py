import requests

url = "http://vasthienviro.com/electrosteel/cmd.php"
data = {
    "station_id": "SINTER_PROPORTIONATE",
    "process_value": sendParameterValue,
    "analyser_id": "V120210047",
}
resp = requests.post(url, json=data)