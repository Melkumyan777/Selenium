#SpaceTrack
import requests
import json

session = requests.Session()
link = "https://www.space-track.org"

requestLogin = "/ajaxauth/login"

data = { 
    'identity': 'melkumyanmarat9@gmail.com',
    'password': 'MelkumyanMarat777'
}
requestCmdAction = "/basicspacedata/query"
requestFind   = "/class/gp/EPOCH/>now-1/NORAD_CAT_ID/>1/"
requestSatcat = "/class/satcat/"
requestBoxscore = "/class/boxscore/"
requestDecay = "/class/decay/"
requestGP = "/class/gp/"
requestLaunchSite = "/class/launch_site/"

with requests.Session() as session:
    resp = session.post(link + requestLogin, data=data)

response1 = session.get(link + requestCmdAction + requestFind)
retData1 = response1.text
json_obj1 = json.loads(retData1)

response2 = session.get(link + requestCmdAction + requestSatcat)
retData2 = response2.text
json_obj2 = json.loads(retData2)

response3 = session.get(link + requestCmdAction + requestBoxscore)
retData3 = response3.text
json_obj3 = json.loads(retData3)

response4 = session.get(link + requestCmdAction + requestDecay)
retData4 = response4.text
json_obj4 = json.loads(retData4)

response5 = session.get(link + requestCmdAction + requestGP)
retData5 = response5.text
json_obj5 = json.loads(retData5)

response6 = session.get(link + requestCmdAction + requestLaunchSite)
retData6 = response6.text
json_obj6 = json.loads(retData6)


with open('data.json', 'w') as f:
    json.dump(json_obj1, f, indent=2)

with open('satcat_data.json', 'w') as f: #Информация о спутниковом каталоге. Предикат "CURRENT" указывает на самую актуальную запись каталога с символом 'Y'. Все более старые записи для этого объекта будут иметь символ 'N'.
    json.dump(json_obj2, f, indent=2)

with open('boxscore_data.json', 'w') as f: #Учет рукотворных объектов, которые были или находятся на орбите. Получен из каталога спутников и сгруппирован по странам/организациям.
    json.dump(json_obj3, f, indent=2)

with open('decay_data.json', 'w') as f: #Прогнозируемая и историческая информация о распаде
    json.dump(json_obj4, f, indent=2)

with open('GP_data.json', 'w') as f: 
    json.dump(json_obj5, f, indent=2)

with open('launch_site_data.json', 'w') as f: #Список площадок запуска, найденных в записях спутниковых каталогов.
    json.dump(json_obj6, f, indent=2)

