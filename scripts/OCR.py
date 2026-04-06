import cv2
import easyocr
import os

def crop(image_path, no_of_people:str):
    if not os.path.exists(image_path):
        print(f"錯誤：找不到檔案 {image_path}")
        return []
    img = cv2.imread(image_path)

    regions = {
        "4" : [
            (480, 413, 240, 50),  # 區域 1
            (723, 413, 240, 50),  # 區域 2
            (966, 413, 240, 50),  # 區域 3
            (1207, 413, 240, 50)  # 區域 4
        ],
        "3" : [
            (600, 413, 240, 50),  # 區域 1
            (845, 413, 240, 50),  # 區域 2
            (1083, 413, 240, 50),  # 區域 3
        ],
        "2" : [
            (723, 413, 240, 50),  # 區域 2
            (966, 413, 240, 50),  # 區域 3
        ],
        "1" : [
            (845, 413, 240, 50),  # 區域 1
        ]
    }

    
    rois = []
    for i, (x, y, w, h) in enumerate(regions[no_of_people]):
        roi = img[y:y+h, x:x+w] # type: ignore
        rois.append(roi)
    return rois

def process_with_easyocr(roi, reader):
    results = reader.readtext(roi, detail=0)
    
    print("="*30)
    final_text = " ".join(results)
    print(f"【結果】")
    print(final_text if final_text else "(無辨識結果)")
    print("-" * 30)
    return final_text


if __name__ == "__main__":
    target_image = r"samples\202604~2.JPG" 
    rois = crop(target_image)
    for roi in rois:
        process_with_easyocr(roi, reader = easyocr.Reader(['ch_tra', 'en'], gpu=True))