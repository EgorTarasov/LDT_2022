import time
import multiprocessing
from argparse import ArgumentParser

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas
import numpy as np

base_url = "https://yandex.ru/maps/213/moscow/?ll=37.617700%2C55.755863&z=10"

def get_point(driver: webdriver, address: str):
    driver.get(base_url)
    time.sleep(2)
    inp = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/header/div/div/div/form/div[2]/div/span/span/input")
    inp.click()
    inp.send_keys(address)
    time.sleep(2)
    
        
    find_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/header/div/div/div/form/div[3]/button")
    find_btn.click()
    time.sleep(3)
while True:
        try:
            coordinates = driver.find_element(By.CLASS_NAME, "toponym-card-title-view__coords-badge")
            long, lat = map(float, coordinates.text.split(","))
            print(address, long, lat)
            return long, lat
        except NoSuchElementException:
            time.sleep(2)



def main(filename): 
    options = Options().add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(base_url) 
    time.sleep(5)
    df = pandas.read_csv(filename)
    long = []
    lat = []
    addresses = df["address"]  
    for adr in addresses:
        point_long, point_lat = get_point(driver, adr)
        long.append(point_long)
        lat.append(point_lat)
    
    df["long"] = np.array(long)
    df["lat"] = np.array(lat)
    name, ext = filename.split(".")
    df.to_csv(name+"_v1"+ext)
    driver.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="csv file", metavar="FILE")
    filename = parser.parse_args().filename    
    main(filename=filename)
