from scripts import prices, update, screenshot, OCR, InGameUI, log
from PySide6.QtWidgets import QApplication, QMainWindow
from scripts.UI_scripts.MainWindow_ui import Ui_MainWindow
from PySide6.QtCore import QTimer
from pynput import keyboard
import easyocr
import win32gui
import threading



class HBMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.has_setWFAsParent = False
        self.WF_ID = win32gui.FindWindow(None, u"Warframe")
        self.reader = easyocr.Reader(['ch_tra', 'en'], gpu=True) 
        update.itemList()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WF遺物小助手")
        
        self.inGameUI = InGameUI.Window()
        self.inGameUI_status = 0
        
        self.result_items = [self.inGameUI.ui.item_1,self.inGameUI.ui.item_2,self.inGameUI.ui.item_3,self.inGameUI.ui.item_4]
        self.price_items = [self.inGameUI.ui.price_1,self.inGameUI.ui.price_2,self.inGameUI.ui.price_3,self.inGameUI.ui.price_4]
        
        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(50)          
        self._poll_timer.timeout.connect(self.communicator)
        self._poll_timer.start()
    
        self.log_checker = threading.Thread(target=log.log_checker)
        self.log_checker.start()
        self.TeamMenber = 4
    

    def communicator(self):
        if not log.ready.empty():
            self.ui.status_value.setText("就緒")
        
        if not screenshot.Shoted.empty():
            screenshot.Shoted.get()
            print(f"\t* 查詢中")
            self.Shot2Price(self.TeamMenber)
        
        if not screenshot.Shot_Request.empty():
            screenshot.Shot_Request.get()
            print(f"\t* 截圖中")
            screenshot.take_screenshot()
        
        if not log.void_drops.empty():
            message = log.void_drops.get()
            if message > 0:
                print(f"* 選擇階段 【{message}選1】")
                for item in self.result_items:
                    item.setText("查詢中...")
                for item in self.price_items:
                    item.setText("-")
                if not self.has_setWFAsParent:
                    self.inGameUI.setWFAsParent()
                    self.has_setWFAsParent=True
                self.inGameUI.show()
                self.TeamMenber = message
                screenshot.Shot_Request.put(1)
            if message < 0:
                print(f"* 選擇階段結束")
                self.inGameUI.hide()


    def Shot2Price(self, no_of_people = 1):
        rois = OCR.crop(r"screenshots\temp.png", str(no_of_people))
        for i in range(4-len(rois)):
            self.result_items[3-i].setText("")
            self.price_items[3-i].setText("")
            
        for i, roi in enumerate(rois):
            text_result = OCR.process_with_easyocr(roi, self.reader)
            price, price_result = prices.get(text_result)
            if price_result:
                if price >= 0:
                    print(f"\t\t【{price_result[0]}】| => {price}\t信心:{price_result[1]}")
                    self.result_items[i].setText(price_result[0])
                    self.price_items[i].setText(str(price)+"P")
                else:
                    print(f"\t\t【{text_result}】查詢失敗\t猜測:【{price_result[0]}】|信心:{price_result[1]}")
                    self.result_items[i].setText("-")
                    self.price_items[i].setText("-P")
                self.inGameUI_status = 2
            else:
                print(f"\t\t【{text_result}】 查詢失敗")

    def closeEvent(self, event):
        log.shotdown.put(1)
        self.inGameUI.destroy()
        event.accept()


def main():
    app = QApplication([])
    hb_window = HBMainWindow()
    hb_window.show()
    app.exec()

if __name__ == "__main__":
    main()