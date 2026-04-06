import requests
import time


API_PATH = "https://api.warframe.market"
RATE_LIMIT = 0.35 # 3 requests/second
LANGUAGE = "zh-hant"
PLATFORMS = "pc"
CROSSPLAY = "True"

BASE_HEADER = {
    "Language": LANGUAGE,
    "Platforms":PLATFORMS,
    "Crossplay":CROSSPLAY
}


last_request = 0
def rate_limited_get(endpoint :str):
    global last_request
    while (time.time() - last_request <= RATE_LIMIT):
        pass
    response = requests.get(API_PATH + endpoint, headers=BASE_HEADER)
    last_request = time.time()
    if response.status_code > 400:
        return {"error":"ERROR 404"}
    return response.json()