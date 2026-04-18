from scripts import prices, update, screenshot, OCR, InGameUI, log
from PySide6.QtWidgets import QApplication, QMainWindow
from scripts.UI_scripts.MainWindow_ui import Ui_MainWindow
from PySide6.QtCore import QTimer, Signal, QObject
import win32gui
import threading
from paddleocr import PaddleOCR
import queue

prices_Queue = queue.Queue(4)

class UISignalBridge(QObject):
    update_item_text = Signal(int, str)
    update_price_text = Signal(int, str)
    update_status_text = Signal(str)

class HBMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.has_setWFAsParent = False
        self.WF_ID = win32gui.FindWindow(None, u"Warframe")
        self.PaddleOCR = None
        # self.reader = easyocr.Reader(['ch_tra', 'en'], gpu=True) 

        update.itemList()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WF遺物小助手")
        
        
        self.inGameUI = InGameUI.Window()
        self.inGameUI_status = 0
        
        self.result_items = [self.inGameUI.ui.item_1,self.inGameUI.ui.item_2,self.inGameUI.ui.item_3,self.inGameUI.ui.item_4]
        self.price_items = [self.inGameUI.ui.price_1,self.inGameUI.ui.price_2,self.inGameUI.ui.price_3,self.inGameUI.ui.price_4]
        
        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(500)          
        self._poll_timer.timeout.connect(self.communicator)
        self._poll_timer.start()
    
        self.log_checker = threading.Thread(target=log.log_checker)
        self.log_checker.start()
        self.TeamMenber = 4
        
        self.prices = []
        self.price_print_index = 0
        
        
        self.ui_signal = UISignalBridge()
        self.ui_signal.update_item_text.connect(lambda idx, text: self.result_items[idx].setText(text))
        self.ui_signal.update_price_text.connect(lambda idx, text: self.price_items[idx].setText(text))
        self.ui_signal.update_status_text.connect(lambda text: self.inGameUI.ui.Status_Holder.setText(text))

    def communicator(self):
        
        if not log.log_message.empty():
            message = log.log_message.get()
            self.ui.status_message_textBox.setText(message)
        
        # check if warframe launch
        self.inGameUI.pid = win32gui.FindWindow(None, u"Warframe")
        if self.inGameUI.pid == 0:
            self.ui.status_value.setText("未偵測到Warframe主體")
            self._poll_timer.setInterval(1000)
            self.has_setWFAsParent=False
            
            
        else:
            self.ui.status_value.setText("Warframe EE.log 讀取中")
            self.inGameUI.ui.Status_Holder.setText("Warframe EE.log 讀取中")
            if self.PaddleOCR is None:
                self.ui.status_value.setText("模型讀取中")
                self.inGameUI.ui.Status_Holder.setText("模型讀取中")
                self.PaddleOCR = PaddleOCR(
                    text_detection_model_name="PP-OCRv5_mobile_det",
                    text_recognition_model_name="PP-OCRv5_mobile_rec",
                    use_doc_orientation_classify=False,
                    use_doc_unwarping=False,
                    use_textline_orientation=False)
            self._poll_timer.setInterval(500)
            

        
        # check if app ready
        if not log.ready.empty() and self.inGameUI.pid != 0:
            self.ui.status_value.setText("就緒")
            self.inGameUI.ui.Status_Holder.setText("遺物小助手已就緒")
            if not self.has_setWFAsParent:
                self.inGameUI.setWFAsParent()
                self.has_setWFAsParent=True
                self.inGameUI.ui.Status_Holder.setText("")
                self.inGameUI.ui.Message_holder.setText("")
                self.inGameUI.ui.Status_Holder1.setText("")
                self.inGameUI.show()
                self.inGameUI.ui.VoidDrop_Frame.setVisible(False)

        
        # screenshot ~callback
        if not screenshot.Shoted.empty():
            screenshot.Shoted.get()
            self.Shot2Price()
        
        # when drop item
        if not log.void_drops.empty():
            message = log.void_drops.get()
            if message > 0:
                self.inGameUI.ui.Message_holder.setText(f"* 選擇階段 【{message}選1】")
                print(f"* 選擇階段 【{message}選1】")
                # self.inGameUI.show()
                self.inGameUI.ui.VoidDrop_Frame.setVisible(True)
                for index in range(4):
                    self.result_items[index].show()
                    self.result_items[index].setText("<掃描中>")
                    self.price_items[index].show()
                    self.price_items[index].setText("-")

                self.TeamMenber = message
                # self.inGameUI.ui.Status_Holder.setText(f"> 截圖中")
                print(f"* 截圖中")
                screenshot.take_screenshot()
            if message < 0:
                print(f"* 選擇階段結束")
                self.inGameUI.ui.Message_holder.setText(f"")
                self.inGameUI.ui.Status_Holder.setText(f"")
                self.inGameUI.ui.VoidDrop_Frame.setVisible(False)

        
        if not prices_Queue.empty():
            item_price, index = prices_Queue.get()
            if item_price is None:
                self.price_items[index].setText("請求失敗")
            elif item_price > 0:
                self.price_items[index].setText(f"{item_price}P")
            else:
                self.price_items[index].setText("-P")


    def Shot2Price(self):
        rois = OCR.crop(r"screenshots\temp.png", str(self.TeamMenber))
        for i in range(4-len(rois)):
            self.result_items[3-i].setText("")
            self.result_items[3-i].hide()
            self.price_items[3-i].setText("")  
            self.price_items[3-i].hide()  
            
        def price_get_worker(rois):
            try:
                self.ui_signal.update_status_text.emit(f"> 文字掃描中")
                ocr_text_results = OCR.process_with_PaddleOCR(rois, self.PaddleOCR)
                self.ui_signal.update_status_text.emit(f"> 正在請求WF Market")
                for i, ocr_text_result in enumerate(ocr_text_results):
                    item_name, confident, _ = prices.guess_item_name(ocr_text_result)
                    if confident>80:     
                        self.ui_signal.update_item_text.emit(i, item_name)
                        self.ui_signal.update_price_text.emit(i, "請求中")
                        print(f"* 請求WF Market中【{item_name}】OCR信心:{confident}")
                        item_price = prices.get_price_from_WF_Market(item_name)
                        print(f"{i}【{item_name}】| => {item_price}")
                        prices_Queue.put((item_price, i), block=False)
                    else:
                        self.ui_signal.update_item_text.emit(i, item_name)
                        self.ui_signal.update_price_text.emit(i, "請求中")
                        print(f"* 請求WF Market中【{item_name}】OCR信心:{confident} ** {ocr_text_result} **")
                        item_price = -1
                        print(f"{i}【{item_name}】| => {item_price}")
                        prices_Queue.put((item_price, i), block=False)
            except Exception as e:
                print(f"[ERROR] 工作執行緒失敗: {repr(e)}")
                import traceback
                traceback.print_exc()
            finally:
                del rois
                import gc
                gc.collect()
                    
        print("* OCR階段")
        print("="*30)

        worker_thread = threading.Thread(target=price_get_worker, args=(rois,), daemon=True)
        worker_thread.start()

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