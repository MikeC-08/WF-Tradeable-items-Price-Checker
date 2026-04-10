from PySide6.QtWidgets import QWidget
from scripts.UI_scripts.InGameUI_ui import Ui_Form
from PySide6.QtCore import Qt
import win32gui


class Window(QWidget):
    def __init__(self):
        super().__init__()


        flags = (
                    Qt.WindowStaysOnTopHint | # type: ignore
                    Qt.FramelessWindowHint | # type: ignore
                    Qt.WindowDoesNotAcceptFocus | # type: ignore
                    Qt.Tool # type: ignore
                )
        self.setWindowFlags(flags)
        self.setAttribute(Qt.WA_TransparentForMouseEvents) # type: ignore
        self.setAttribute(Qt.WA_DeleteOnClose) # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground) # type: ignore
        
        self.setAutoFillBackground(False)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("WF遺物小助手_InGameUI")
        self.move(15,180)
        
    def setWFAsParent(self):
        cid = self.winId()
        pid = win32gui.FindWindow(None, u"Warframe")
        win32gui.SetParent(cid,pid)