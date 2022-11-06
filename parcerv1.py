from app.sql_app.schemas import *
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pydantic import BaseModel, confloat, constr

import time
import json

options = Options()
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

zoom = 15
map_url = "https://yandex.ru/maps/213/moscow/?ll={lat}%2C{long}}&z={zoom}"
# ~4.5 x ~3.15 6350 
# 55.810437, 37.462320

# url = ozon_box.format(lat=37.470774 , long=55.80060)

# старые координаты
# 0.008 верхняя точка
# 55.5846, 37.5427 # нижняя точка
# 55.7858, 37.3686 # левая точка 
# 55.7858, 37.8410 # правая точка 
# 0.3232 ~ 37 0.0.008 - 1 км, 0.4724 ~ 30  0.0158 - 1 км
# 0.008735135135135135 ~ 1 км

# новые координаты
# 55.903112, 37.586114 - верхняя точка
# 55.578503, 37.594354 - нижняя точка
# 
# идем сверху вниз
def parce_shoping_malls():
    long = 55.5846  # это вверх/вниз
    lat = 37.3686  # вправо + / влево -
    shopping_malls = "https://yandex.ru/maps/213/moscow/category/shopping_mall/184108083/?ll={lat}%2C{long}0&sll={lat}%2C{long}&sspn=0.412208%2C0.126524&z=15"
    data_dict = {}  # словарь формата: "улица" : {data}
    for x in range(11):
        for y in range(11):
            url = shopping_malls.format(long=long, lat=lat)

            driver.get(url)

            time.sleep(9)

            results = driver.find_elements(By.CLASS_NAME, "search-snippet-view")

            print(results)
            for el in results:
                try:
                    
                    print("-" * 30)
                    coord = el.find_element(By.CLASS_NAME, "search-snippet-view__body")
                    el_long, el_lat = map(lambda x: float(x), coord.get_attribute("data-coordinates").split(","))
                    temp = el.text.split("\n")
                    if temp[1].isdigit():
                        address = el.text.split("\n")[4]
                    else:
                        address = el.text.split("\n")[3]
                    print(address)
                    if address in data_dict.keys():
                        continue
                    data_dict[address] = [[el_long, el_lat]] + el.text.split("\n")
                except StaleElementReferenceException:
                    print(el)
            results = []
            long += 0.008 * 3
            time.sleep(5)
        long = 55.5846
        lat += 0.0158 * 3

    with open("shoping_malls.json", "w+", encoding="utf-8") as j:
        json.dump(data_dict, j)

    print(data_dict)
    print(url, len(data_dict))



def parce_stops():
    long = 55.5846  # это вверх/вниз
    lat = 37.3686  # вправо + / влево -
    transport = "https://yandex.ru/maps/213/moscow/category/public_transport_stop/223677355200/?ll={lat}%2C{long}&sspn=1.079407%2C0.409467&z=15"
    data_dict = {}  # словарь формата: "улица" : {data}
    for x in range(11):
        for y in range(11):
            url = transport.format(long=long, lat=lat)

            driver.get(url)

            time.sleep(9)

            results = driver.find_elements(By.CLASS_NAME, "search-snippet-view")

            print(results)
            for el in results:
                try:
                    print(el.text)
                    print("-" * 30)
                    coord = el.find_element(By.CLASS_NAME, "search-snippet-view__body")
                    el_long, el_lat = map(lambda x: float(x), coord.get_attribute("data-coordinates").split(","))
                    address = el.text.split("\n")[3]
                    if address in data_dict.keys():
                        continue
                    data_dict[address] = [[el_long, el_lat]] + el.text.split("\n")
                except StaleElementReferenceException:
                    print(el)
            results = []
            long += 0.008 * 3
            time.sleep(5)
        long = 55.5846
        lat += 0.0158 * 3

    with open("transport.json", "w+", encoding="utf-8") as j:
        json.dump(data_dict, j)

    print(data_dict)
    print(url, len(data_dict))


def parce_service():
    long = 55.5846  # это вверх/вниз
    lat = 37.3686  # вправо + / влево -
    yandex_market = "https://yandex.ru/maps/213/moscow/chain/postamaty_yandeks_marketa/237923876496/?ll={lat}%2C{long}&sll={lat}%2C{long}&sspn=0.114902%2C0.091337&z=15"
    ozon_box = "https://yandex.ru/maps/213/moscow/chain/ozon_box/162902223445/?ll={lat}%2C{long}&sspn=2.158813%2C0.823225&z=15"
    wb = "https://yandex.ru/maps/213/moscow/chain/wildberries/2129228517/?ll={lat}%2C{long}&sspn=0.431813%2C0.342558&z=15"

    data_dict = {} # словарь формата: "улица" : {data}
    for x in range(11):
        for y in range(11):
            url = wb.format(long=long, lat=lat)

            driver.get(url)

            time.sleep(3)
            # how to scroll
            for _ in range(30):
                #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                element = driver.find_element(By.CSS_SELECTOR, "scroll")
                ActionChains(driver).move_to_element(element).click().perform()
                ActionChains(driver).move_to_element(element).send_keys(Keys.DOWN).perform()
                time.sleep(0.5)
            # #driver.implicitly_wait(10)
            results = driver.find_elements(By.CLASS_NAME, "search-snippet-view")

            print(results)
            for el in results:
                    try:
                        print(el.text)
                        print("-"*30)
                        coord = el.find_element(By.CLASS_NAME, "search-snippet-view__body")
                        el_long, el_lat = map(lambda x: float(x), coord.get_attribute("data-coordinates").split(","))
                        address = el.text.split("\n")[3]
                        if address in data_dict.keys():
                            continue
                        data_dict[address] = [[el_long, el_lat]] + el.text.split("\n")
                    except StaleElementReferenceException:
                        print(el)
            results = []
            # scroll
            #element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[8]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]")
            #driver.implicitly_wait(5)
            #ActionChains(driver).move_to_element(element).click().perform()
            #ActionChains(driver).move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()

            long += 0.008 * 3
            time.sleep(3)
            #driver.implicitly_wait(10)
        long = 55.5846
        lat += 0.0158 * 3

    with open("wb_v2.json", "w+", encoding="utf-8") as j:
        json.dump(data_dict, j)

    print(data_dict)
    print(url, len(data_dict))

parce_shoping_malls()