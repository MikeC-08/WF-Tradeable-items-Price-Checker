from scripts import req
import json
from rapidfuzz import process
from os import path

if not path.exists(r"data\items_list.json"):
    from scripts import update
    update.itemList()
with open(r"data\items_list.json", 'r', encoding="utf-8") as file:
    item_list_json : dict = json.load(file)


def get(item_name = "Mesa Prime 系統 藍圖"):
    item_list_keys = list(item_list_json.keys())
    result = process.extractOne(item_name.strip().replace(" ", ""), item_list_keys)
    if not result:
        return -1.0, result
    if result[1] > 80:
        item_slug : str = item_list_json[result[0]]
        json_response :dict= req.rate_limited_get(f"/v2/orders/item/{item_slug}")
        with open(r"data\temp.json", 'w', encoding='utf-8') as f:
            json.dump(json_response, f, indent=4, ensure_ascii=False)
        # sell_list = json_response['data']['sell']
        item_prices = []
        for item in json_response['data']:
            # print(item['user']['status'] == 'ingame')
            if item['user']['status'] == 'ingame' and item['type'] == 'sell':
                item_prices.append(item['platinum'])
        top_5_price = sorted(item_prices, reverse=False)[:5]
        
        if len(top_5_price)>0:
            average_price : float = sum(top_5_price)/len(top_5_price)
            return average_price, result
        else:
            return -1.0, result
    else:
        return -1.0, result

            


if __name__ == "__main__":
    get()