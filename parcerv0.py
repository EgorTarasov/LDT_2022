import time
import csv
import json
import os
# Найти центры районов
# пройтись по всем районам с запросами:
# 1) постаматы яндекс маркет ~768
# 2) Цайняо, постаматы ~ 1198
# 3) OZON box ~600
# 4) wildberries пункт выдачи ~ 2400
# 5)
# "add - business - view"



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pydantic import BaseModel, confloat, constr
import requests

from typing import Optional


class MapItem(BaseModel):
    name: constr(min_length=3, max_length=256)
    long: confloat(ge=-180.0, le=180)
    lat: confloat(ge=-90, le=90)
    type: constr(min_length=3, max_length=30)
    rating: Optional[confloat(ge=0.0, le=5.0)]


class Points(BaseModel):
    points: list[MapItem]


options = Options().add_argument("window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# поиск постоматов яндекса
map_url = "https://yandex.ru/maps/213/moscow/"
driver.get(map_url)
time.sleep(10)
# click on find button
inp = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/header/div/div/div/form/div[2]/div/span/span/input")
inp.click()
inp.send_keys("постоматы яндекс маркет")
time.sleep(10)

find_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/header/div/div/div/form/div[3]/button")
find_btn.click()
time.sleep(10)


data: dict[str: list[str]] = {}
arr = []
data_arr = []
data_dict = {}
# with open('parcer/postv3.csv', 'w+', encoding="utf-8") as csvfile:
#     fieldnames = ['name1', 'name2', "lat", "long", "type", "address", "rating", "rating_count", "time_open"]
#     dwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer = csv.writer(csvfile)
while len(arr) < 500:
    results = driver.find_elements(By.CLASS_NAME, "search-snippet-view")
    try:
        end = driver.find_element(By.CLASS_NAME, "add-business-view")
        break
    except NoSuchElementException as e:
        for el in results:
            address = el.text.split("\n")[2]
            data_dict[address] = el.text.split("\n")
            data_arr.append(el.text.split("\n"))
            # print(type(el.text.split("\n")[0]))
            # exit(0)
            # if len(el.text.split("\n")) == 9:
            #     name1, name2, _type, address, _, rating, rating_count, _, time_till_open = el.text.split("\n")
            #     coord = el.find_element(By.CLASS_NAME, "search-snippet-view__body")
            #     long, lat = map(lambda x: float(x), coord.get_attribute("data-coordinates").split(","))
            #     #/html/body/div[1]/div[2]/div[8]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul/li[1]/div
            #     # print(type(name1), type(address))
            #     # print(name1, address)
            #     #
            #     if address in data_arr:
            #         break
            #     data_arr.append(address)
            #     print(lat,long)
            #     rating = float(rating.replace(",", "."))
            #     item = MapItem(
            #             name=name1,
            #             type=name2,
            #             address=address,
            #             lat=lat,
            #             long=long
            #         )
            #
            #     response = requests.post("http://92.243.176.50/places/new",
            #                              json={
            #                                   "name": name1,
            #                                   "long": long,
            #                                   "lat": lat,
            #                                   "type": name2,
            #                                   "rating": rating
            #                                 }
            #                              )
            #     if response.status_code == 200:
            #         pass
            #     else:
            #         print(response.text)
            #         exit(0)
            #     arr.append(
            #         MapItem(
            #             name=name1,
            #             type=name2,
            #             address=address,
            #             lat=lat,
            #             long=long
            #         )
            #     )
            #     _data = [name1, name2, _type, address, rating, rating_count, time_till_open]
            #     data[address] = _data
            #     # writer.writerow(_data)
            # else:
            #     print(el.text.split("\n"))
        # scroll
        print(len(data_arr))
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[8]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]")
        driver.implicitly_wait(5)
        ActionChains(driver).move_to_element(element).click().perform()
        ActionChains(driver).move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()

with open("datav2.txt", "w+", encoding="utf-8") as file:
    for i in data_arr:
        file.write(";".join(i) + "\n")
with open("datav3.txt", "w+", encoding="utf-8") as file:
    for k in data_dict:
        file.write(";".join(i) + "\n")
driver.close()



# <div class="search-snippet-view__body _type_business" data-object="search-list-item" data-id="1335441175" data-log-id="dHlwZT1iaXpmaW5kZXI7aWQ9MTMzNTQ0MTE3NQ==" data-coordinates="37.684670,55.771760"><div><a class="search-snippet-view__link-overlay _focusable" href="/maps/org/perekryostok/1335441175/" tabindex="-1" aria-label="Перекрёсток">Перекрёсток</a><div class="search-business-snippet-view"><div class="search-business-snippet-view__content"><div aria-hidden="true" class="search-business-snippet-view__photo _size_normal"><div class="photos-thumbnail-view _type_serp"><img class="img-with-alt" width="100%" height="100%" src="https://avatars.mds.yandex.net/get-altay/5253303/2a0000017b9cdbab417c8d4688df64ab3dbd/S" style="object-fit: contain;"></div></div><div class="search-business-snippet-view__head"><div class="search-business-snippet-view__title">Перекрёсток<span class="business-verified-badge _prioritized" aria-hidden="true"><span class="inline-image _loaded" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 11A5 5 0 1 1 6 1a5 5 0 0 1 0 10z" fill="#3CB300"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M5.807 6.901l.648.657a.5.5 0 0 0 .84-.227l.694-2.706a.5.5 0 0 0-.609-.608l-2.684.687a.5.5 0 0 0-.232.836l.641.65-2.263 2.265c.137.167.245.29.324.37.08.08.207.192.383.337l2.258-2.26z" fill="#fff"></path></svg></span></span></div><div class="search-business-snippet-view__optional"></div></div><div class="search-business-snippet-view__address">Ладожская ул., 13</div><div class="search-business-snippet-view__rating-and-awards"><div class="search-business-snippet-view__rating"><div class="business-rating-with-text-view"><span class="business-rating-badge-view _size_m"><div class="business-rating-badge-view__stars"><span class="inline-image _loaded business-rating-badge-view__star _full _size_m" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.987 9.42l-3.26 1.991a.48.48 0 0 1-.715-.526l.945-3.764-2.74-2.133A.48.48 0 0 1 .47 4.13l3.586-.295L5.552.348a.48.48 0 0 1 .883.001l1.483 3.486 3.61.296a.48.48 0 0 1 .255.857L9.031 7.121l.943 3.766a.48.48 0 0 1-.715.527L5.987 9.419v.001z" fill="currentColor"></path></svg></span><span class="inline-image _loaded business-rating-badge-view__star _full _size_m" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.987 9.42l-3.26 1.991a.48.48 0 0 1-.715-.526l.945-3.764-2.74-2.133A.48.48 0 0 1 .47 4.13l3.586-.295L5.552.348a.48.48 0 0 1 .883.001l1.483 3.486 3.61.296a.48.48 0 0 1 .255.857L9.031 7.121l.943 3.766a.48.48 0 0 1-.715.527L5.987 9.419v.001z" fill="currentColor"></path></svg></span><span class="inline-image _loaded business-rating-badge-view__star _full _size_m" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.987 9.42l-3.26 1.991a.48.48 0 0 1-.715-.526l.945-3.764-2.74-2.133A.48.48 0 0 1 .47 4.13l3.586-.295L5.552.348a.48.48 0 0 1 .883.001l1.483 3.486 3.61.296a.48.48 0 0 1 .255.857L9.031 7.121l.943 3.766a.48.48 0 0 1-.715.527L5.987 9.419v.001z" fill="currentColor"></path></svg></span><span class="inline-image _loaded business-rating-badge-view__star _full _size_m" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M5.987 9.42l-3.26 1.991a.48.48 0 0 1-.715-.526l.945-3.764-2.74-2.133A.48.48 0 0 1 .47 4.13l3.586-.295L5.552.348a.48.48 0 0 1 .883.001l1.483 3.486 3.61.296a.48.48 0 0 1 .255.857L9.031 7.121l.943 3.766a.48.48 0 0 1-.715.527L5.987 9.419v.001z" fill="currentColor"></path></svg></span><span class="inline-image _loaded business-rating-badge-view__star _half _size_m" aria-hidden="true" role="button" tabindex="-1" style="font-size: 0px; line-height: 0;"><svg width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 .057a.479.479 0 0 1 .435.292l1.483 3.486 3.61.296a.48.48 0 0 1-.255.857L9.031 7.121l.943 3.766a.48.48 0 0 1-.715.527L6 9.427V.057z" fill="#CCC"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M6 .057a.479.479 0 0 0-.435.292L4.082 3.835l-3.61.296a.48.48 0 0 0-.255.857l2.814 2.133-.943 3.766a.48.48 0 0 0 .715.527L6 9.427V.057z" fill="#FC0"></path></svg></span></div><span class="business-rating-badge-view__rating"><span class="a11y-hidden">Рейтинг</span><span class="business-rating-badge-view__rating-text _size_m">4,3</span></span></span><div class="business-rating-with-text-view__count"><span class="business-rating-amount-view">2167 оценок</span></div></div></div><div class="search-business-snippet-view__awards"></div></div><div class="search-business-snippet-view__footer"><div class="search-business-snippet-view__working-status"><div class="business-working-status-view">Круглосуточно</div></div></div></div></div></div></div>

# driver.get("http://www.python.org")
# time.sleep(100)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# html/body/div[1]/div[2]/div[8]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[4]