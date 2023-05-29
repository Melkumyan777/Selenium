#SpaceTrack
import multiprocessing
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv


browser = webdriver.Chrome()
response = browser.get('https://www.space-track.org/#catalog')
time.sleep(10)

#блок авторизации и переход к информации о КА
input_login = browser.find_element(By.XPATH, '//*[@id="identity"]').send_keys('melkumyanmarat9@gmail.com')
input_password = browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('MelkumyanMarat777')
button_enter = browser.find_element(By.NAME, 'btnLogin').click()

while(len(browser.find_elements(By.XPATH, "//a[contains(text(), 'Satellite Search')]")) < 0):
    time.sleep(1)
button_satellite = browser.find_element(By.LINK_TEXT, 'Satellite Search').click()
while(len(browser.find_elements(By.XPATH, "//*[@id='satCatTable_length']/label/select")) < 0):
    time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='satCatTable_length']/label/select").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='satCatTable_length']/label/select/option[4]").click()
time.sleep(1)

#списки с данными 
catList = []
satnameList = []
intldesList = []
typeList = []
countryList = []
launchList = []
siteList = []
decayList = []
j = 1

#основной блок программы, в которым заполняем каждый список отдельно
cycleFlag = True
try:
    while cycleFlag:
        rowNumber = int(len(browser.find_elements(By.XPATH, "//*[@id='satCatTable']/tbody/tr"))) #количество строк
        print(f'Количество строк на текущей странице: {rowNumber}')
        i = 1
        while (i <= rowNumber):
            catList.append(browser.find_element(By.XPATH, f"//*[@id='satCatTable']/tbody/tr[{i}]/td[1]").text)
            satnameList.append(browser.find_element(By.XPATH, f"//*[@id='satCatTable']/tbody/tr[{i}]/td[2]").text)
            intldesList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[3]").text)
            typeList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[4]").text)
            countryList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[5]").text)
            launchList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[6]").text)
            siteList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[7]").text)
            decayList.append(browser.find_element(By.XPATH, f"//table[@id='satCatTable']//tbody/tr[{i}]//td[8]").text)
            print(f"{catList[-1]}, {satnameList[-1]}, {intldesList[-1]}, {typeList[-1]}, {countryList[-1]}, {launchList[-1]}, {siteList[-1]},{siteList[-1]}") 
            i += 1
        j += 1
        print(f'Страница номер {j-2}')

        #проверка на наличие страниц
        if j < 564: 
            print("Переход на новую страницу")
            print(j)
            click = True
            while (click):
                try:
                    browser.find_element(By.XPATH, f"//*[@id='satCatTable_next']/a").click()
                    time.sleep(1)
                    click = False
                except:
                    time.sleep(2)
            time.sleep(5)
        else:
            print("Страницы закончились")
            cycleFlag = False
finally:
    browser.quit()

#создание csv файла
with open('satellites2.csv', 'a') as f: 
                writer = csv.writer(f)
                writer.writerows(('CAT ID', 'SATNAME', 'INTLDES', 'TYPE', 'COUNTRY', 'LAUNCH DATE', 'SITE', 'DECAY') for i in range(1))
                writer.writerows([(catList[i], satnameList[i], intldesList[i], typeList[i], countryList[i], launchList[i], siteList[i], decayList[i]) for i in range(len(decayList))])
