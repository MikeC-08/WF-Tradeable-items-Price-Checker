from scripts import req
import json
import os


def itemList():
    new_item_dict_zh_hant = {}
    json_response :dict= req.rate_limited_get(f"/v2/items")

    item_datas = json_response.get("data", [])
    for item_data in item_datas:
        new_item_dict_zh_hant[item_data["i18n"]["zh-hant"]["name"]] = item_data["slug"]
        
        # new_item_dict_zh_hant[item_data["i18n"]["zh-hant"]["name"].strip().replace(" ","")] = item_data["slug"]
    pre_remove = []
    keys = new_item_dict_zh_hant.keys()
    for key in keys:
        key: str
        if key.endswith("Prime"):
            if key.replace(" Prime", "") in keys:
                pre_remove.append(key.replace(" Prime", ""))
    
    for key in pre_remove:
        new_item_dict_zh_hant.pop(key)
    
    new_item_dict_zh_hant['Forma'] = "Forma"

    if not os.path.exists("data"):
        os.mkdir("data")
    with open(r"data\items_list.json", 'w', encoding="utf-8") as file:
        json.dump(new_item_dict_zh_hant, file, ensure_ascii=False , indent=4)
    
    
if __name__ == "__main__":
    itemList()
