from app.sql_app import schemas
import json
import pandas as pd
import requests
from argparse import ArgumentParser


def raw_yandex_upload(filename: str, url: str):
    data = {}
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    items = []
    for key in data.keys():
        l.add(len(data[key]))
        el = data[key]
        if len(el) == 7: 
            el.pop(5)
        if len(el) == 6:
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            rating = 0.0
        if len(el) == 10:
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            if el[6] == "Рейтинг":
                rating = float(el[7].replace(",", ".")) 
            else:
                rating = float(el[6].replace(",", ".")) 
        
        item = schemas.MapItemCreate(
            name=name,
            long=long, 
            lat=lat,
            type=_type,
            rating=rating,
            address=address,
            abbrev_ao="",
            desc=""
        )
        items.append(item)
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)

def raw_wb_upload(filename: str, url: str):
    data = {}
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    items = []

    for key in data.keys():
        el = data[key]
        if len(el) == 6:
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            rating = 0.0
            desc=""
        elif len(el) == 10:
            el.pop(2)
        if len(el) == 9: 
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            rating = float(el[6].replace(",", "."))
            desc=json.dumps({"rating_count": el[7], "time": el[8]})

        item = schemas.MapItemCreate(
            name=name,
            long=long, 
            lat=lat,
            type=_type,
            rating=rating,
            address=address,
            abbrev_ao="",
            desc=""
        )
        items.append(item)
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)

def raw_ozon_upload(filename: str, url: str):
    data = {}
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    items = []

    for key in data.keys():
        el = data[key]
        if len(el) == 6:
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            rating = 0.0
            desc=""
        elif len(el) == 9: 
            lat, long = el[0]
            name = el[1]
            _type = el[3]
            address = el[4]
            if el[6] == "Рейтинг":
                el.pop(2)
            rating = float(el[6].replace(",", "."))
        item = schemas.MapItemCreate(
            name=name,
            long=long, 
            lat=lat,
            type=_type,
            rating=rating,
            address=address,
            abbrev_ao="",
            desc=""
        )
        items.append(item)
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)


def raw_transport_upload(filename: str, url: str):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    items = []
    for key in data.keys():
        el = data[key]
        l.add(len(el))
        lat, long = el[0]
        name = el[1]
        address = el[-1]
        if len(el) == 6:
            el.pop(2)
        if len(el) == 5:
            _type = el[3]
        elif len(el) == 7:
            _type = el[4]
        item = schemas.MapItemCreate(
            name=name,
            long=long,
            lat=lat,
            type=_type,
            rating=0.0,
            address=address,
            abbrev_ao="",
            desc=""
        )
        items.append(item)
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)
    print(l)
    pass


def raw_malls_upload(filename: str, url: str):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    items = []
    for key in data.keys():
        el = data[key]
        l.add(len(el))
        lat, long = el[0]
        name = el[1]
        rating = [float(i.replace(",", ".")) for i in el if (len(i) == 3) and ("," in i)]
        if len(rating) == 1:
            rating = rating[0]
        else:
            rating = 0.0
        if len(el) == 7:
            el.pop(2)
        if len(el) == 6:
            _type = el[3]
            address = el[4]

            desc = ""
        elif len(el) == 9:
            _type = el[3]
            address = el[4]
            desc = f"{el[7]}, {el[8]}"
        elif len(el) == 10:
            _type = el[3]
            address = el[4]
            desc = f"{el[8]}, {el[9]}"
        elif len(el) == 11:
            _type = el[4]
            address = el[5]
            desc = f"{el[8]},{el[9]}"
        elif len(el) == 12:
            _type = el[4]
            address = el[5]
            desc = f"{el[8]},{el[9]},{el[10]}"
        item = schemas.MapItemCreate(
            name=name,
            long=long,
            lat=lat,
            type=_type,
            rating=rating,
            address=address,
            abbrev_ao="",
            desc=desc
        )
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)



def raw_region_upload(filename: str, url: str):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    l = set()
    data = data["features"]

    for el in data:
        r = schemas.RegionBase(
            name=el["properties"]["NAME"],
            name_ao=el["properties"]["NAME_AO"],
            okato=el["properties"]["OKATO_AO"],
            abbrev_ao=el["properties"]["ABBREV_AO"],
            geometry=schemas.Geometry(
                type=el["geometry"]["type"],
                coordinates=el["geometry"]["coordinates"]
            )
        )
        response = requests.post(
            url, json=r.dict()
        )
        if response.status_code != 200:
            print(response.content)


def raw_house_upload(filename: str, url:str):
    pass

def raw_metro_upload(filename: str, url: str):
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        "name	nameOfStation	line	longitude	latitude"
        item = schemas.MapItemCreate(
            name=row["nameOfStation"],
            long=row["longitude"],
            lat=row["latitude"],
            type="выход метро",
            rating=0.0,
            address="",
            abbrev_ao="",
            desc=row["name"]+","+row["line"]
        )
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)


def raw_house_upload(filename: str, url: str):
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        "address	area	year	floors	entrance	flats	latitude	longitude"
        item = schemas.MapItemCreate(
            name=row["address"],
            long=row["longitude"],
            lat=row["latitude"],
            type="выход метро",
            rating=0.0,
            address=row["address"],
            abbrev_ao="",
            desc=f"кол-вл этажей: {row['floors']}, год: {row['year']}, кол-вл квартир: {row['flats']}, вход: {row['entrance']}"
        )
        response = requests.post(
            url, json=item.dict()
        )
        if response.status_code != 200:
            print(response.content)

def main(host:str):

    #
    # raw_house_upload("living_building_with_coords.csv", f"{host}/places/new")
    # )
    # raw_metro_upload("new_metro.csv", f"{host}/places/new")
    # raw_region_upload("regions.json", f"{host}/region/new")
    # raw_transport_upload("transport_v0.json", f"{host}/places/new")
    # raw_malls_upload("shoping_malls.json", f"{host}/places/new")
    # url = "http://92.243.176.50/places/new"
    # filename = "wb_v2.json"
    # raw_wb_upload(filename, url)
    # filename = "ozon_v3.json"
    # raw_ozon_upload(filename, url)
    # filename = "yandex_market_2.json"
    # raw_yandex_upload(filename, url)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-h", "--hos", dest="filename", help="csv file", metavar="FILE")
    filename = parser.parse_args().filename
    main()
    
