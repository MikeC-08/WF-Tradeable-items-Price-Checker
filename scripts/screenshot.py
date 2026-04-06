import pyautogui
import os
import queue


Shoted = queue.Queue(1)

# 建立儲存截圖的資料夾
SAVE_PATH = "screenshots"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

def take_screenshot():
    """執行截圖並儲存"""
    if Shoted.empty():
        filename = f"{SAVE_PATH}/temp.png"
        
        # 截取主顯示器
        pic = pyautogui.screenshot()
        pic.save(filename)
        print(f" [✓] 截圖已儲存: {filename}")
        Shoted.put(1)
    else:
        print(" [!] 截圖失敗")
    

