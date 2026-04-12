from scripts import req
import json
from rapidfuzz import process
from os import path

if not path.exists(r"data\items_list.json"):
    from scripts import update
    update.itemList()
with open(r"data\items_list.json", 'r', encoding="utf-8") as file:
    item_list_json : dict = json.load(file)


def guess_item_name(text):
    item_list_keys = list(item_list_json.keys())
    item_name, confident, index = process.extractOne(text.strip().replace(" ", ""), item_list_keys)
    return item_name, confident, index


def get_price_from_WF_Market(item_name):
    if item_name == 'Forma':
        return 0
    
    item_slug : str = item_list_json[item_name]
    json_response :dict= req.rate_limited_get(f"/v2/orders/item/{item_slug}")
    item_prices = []
    for item in json_response['data']:
        if item['user']['status'] == 'ingame' and item['type'] == 'sell':
            item_prices.append(item['platinum'])
    top_5_price = sorted(item_prices, reverse=False)[:5]
    if len(top_5_price)>0:
        average_price : float = sum(top_5_price)/len(top_5_price)
        return round(average_price, 1)
    else:
        return None

            


if __name__ == "__main__":
    item_name, confident, index = guess_item_name("calibam prime 頭部")
    print(item_name, confident, index)
    item_price = get_price_from_WF_Market(item_name)
    print(item_name,">",item_price)
    # get_price_from_WF_Market()