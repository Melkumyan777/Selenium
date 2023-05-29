#Federal Aviation Administration

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv


browser = webdriver.Chrome()
browser.get('https://www.faa.gov/data_research/commercial_space_data/launches/')
time.sleep(2)

dateList = []
payloadList = []
vehicleList = []
companyList = []
siteList = []

cycleFlag = True
browser.find_element(By.XPATH, "//label/select").click()
time.sleep(1)
browser.find_element(By.XPATH, "//label/select/option[@value='100']").click()
time.sleep(2)
j = 1

try:
    while cycleFlag:
        rowNumber = int(len(browser.find_elements(By.XPATH, "//table[@id='spaceTable']//tbody/tr"))) #количество строк
        i = 1
        while (i <= rowNumber): #пока есть новые строки собирать данные о КА
            dateList.append(browser.find_element(By.XPATH, f"//table[@id='spaceTable']//tbody/tr[{i}]//td//span").text)
            payloadList.append(browser.find_element(By.XPATH, f"//table[@id='spaceTable']//tbody/tr[{i}]//td[2]").text)
            vehicleList.append(browser.find_element(By.XPATH, f"//table[@id='spaceTable']//tbody/tr[{i}]//td[3]").text)
            companyList.append(browser.find_element(By.XPATH, f"//table[@id='spaceTable']//tbody/tr[{i}]//td[4]").text)
            siteList.append(browser.find_element(By.XPATH, f"//table[@id='spaceTable']//tbody/tr[{i}]//td[5]").text)
            print(f"{dateList[-1]}, {payloadList[-1]}, {vehicleList[-1]}, {companyList[-1]}, {siteList[-1]}")
            i += 1 #смена строки 
        j += 1 #смена страницы

        if (len(browser.find_elements(By.XPATH, f"//*[@id='spaceTable_paginate']/span/a[{j}]")) > 0): #пока существуют новые страницы
            print("Переход на новую страницу")
            browser.find_element(By.XPATH, f"//*[@id='spaceTable_paginate']/span/a[{j}]").click() #нахождение и нажатие на кнопку следующей страницы
            time.sleep(2)
        else:
            print("Страницы закончились")
            cycleFlag = False #прерывание цикла
    print('Количество лицензированных запусков:', len(dateList))

finally:
    browser.quit() #завершение всех процессов и закрытие браузера

#запись полученных данных в CSV формат
with open('satellites.csv', 'a') as f: 
                writer = csv.writer(f)
                writer.writerows(('Date', 'Payload', 'Vehicle', 'Company', 'Site') for i in range(1))
                writer.writerows([(dateList[i], payloadList[i], vehicleList[i], companyList[i], siteList[i]) for i in range(len(dateList))])