from scripts import prices, update, screenshot, OCR, InGameUI
from PySide6.QtWidgets import QApplication, QMainWindow
from scripts.UI_scripts.MainWindow_ui import Ui_MainWindow
from PySide6.QtCore import QTimer
from pynput import keyboard
import pyautogui
import easyocr
import queue

STOP_shot = queue.Queue(1)

class HBMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.has_setWFAsParent = False
        self.reader = easyocr.Reader(['ch_tra', 'en'], gpu=False) 
        update.itemList()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WF遺物小助手")
        self.ui.Stop_btn.setDisabled(True)

        self.ui.Start_btn.clicked.connect(self.Start_Listening)
        self.ui.Stop_btn.clicked.connect(self.Stop_Listening)
        
        self.inGameUI = InGameUI.Window()
        self.inGameUI_status = 0
        
        self.result_items = [self.inGameUI.ui.item_1,self.inGameUI.ui.item_2,self.inGameUI.ui.item_3,self.inGameUI.ui.item_4]
        self.price_items = [self.inGameUI.ui.price_1,self.inGameUI.ui.price_2,self.inGameUI.ui.price_3,self.inGameUI.ui.price_4]
        
        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(50)          
        self._poll_timer.timeout.connect(self.isShoted_checker)
        self._poll_timer.start()
        
    
    def isShoted_checker(self):
        if not screenshot.Shoted.empty():
            self.Shot2Price()
            screenshot.Shoted.get()


    def Shot2Price(self):
        rois = OCR.crop(r"screenshots\temp.png", self.ui.no_of_people_Dropdown.currentText())
        for i in range(4-len(rois)):
            self.result_items[3-i].setText("")
            self.price_items[3-i].setText("")
            
        for i, roi in enumerate(rois):
            text_result = OCR.process_with_easyocr(roi, self.reader)
            price, price_result = prices.get(text_result)
            if price_result:
                if price >= 0:
                    print(f"[{price_result[0]}]| => {price}\t信心:{price_result[1]}")
                    self.result_items[i].setText(price_result[0])
                    self.price_items[i].setText(str(price)+"P")
                else:
                    print(f"[{text_result}] 查詢失敗\t猜測:[{price_result[0]}]|信心:{price_result[1]}")
                    self.result_items[i].setText("-")
                    self.price_items[i].setText("-P")
                self.inGameUI_status = 2
            else:
                print(f"[{text_result}] 查詢失敗")

                
    def on_release(self, key):
        try:
            if not STOP_shot.empty():
                STOP_shot.get()
                print(" [i] 停止監控程序。")
                return False
            
            # 監測 Enter 鍵
            if key == keyboard.Key.enter:
                print(" [!] 偵測到 Enter 鍵放開，正在截圖...")
                if self.inGameUI_status == 0:
                    for item in self.result_items:
                        item.setText("查詢中...")
                    for item in self.price_items:
                        item.setText("-")
                    if not self.has_setWFAsParent:
                        self.inGameUI.setWFAsParent()
                        self.has_setWFAsParent=True
                    self.inGameUI_status = 1
                    self.inGameUI.show()
                    screenshot.take_screenshot()
                elif self.inGameUI_status == 2:
                    self.inGameUI.hide()
                    self.inGameUI_status = 0

        except Exception as e:
            print(f"錯誤: {e}")
            
    def Start_Listening(self):
        listener = keyboard.Listener(on_release=self.on_release) # type: ignore
        listener.start() 
        print(">>> 監控中... (按下 Enter 截圖")
        self.ui.Start_btn.setDisabled(True)
        self.ui.Stop_btn.setDisabled(False)
        

    def Stop_Listening(self):
        STOP_shot.put(1)
        pyautogui.press('enter')
        self.ui.Start_btn.setDisabled(False)
        self.ui.Stop_btn.setDisabled(True)
        

    def closeEvent(self, event):
        self.inGameUI.destroy()
        event.accept()


def main():
    app = QApplication([])
    hb_window = HBMainWindow()
    hb_window.show()
    app.exec()

if __name__ == "__main__":
    main()