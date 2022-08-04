import requests as rs
import pandas as pd
import geohash2

def oneroom(addr):
    url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"
    response = rs.get(url)
    data = response.json()["items"][0]

    lat, lng = data['lat'], data['lng'] # 위도 경도
    lat, lng
    
    geohash = geohash2.encode(lat, lng, precision=5)
    
    url_2 = f'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'
    response_2 = rs.get(url_2)
    items_2 = response_2.json()['items']
    ids_2 = [item["item_id"] for item in items_2]
    items_3 = response_3.json()["items"]
    columns_3 = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    df = pd.DataFrame(items_3)[columns_3]
    return df
