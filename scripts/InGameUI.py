from PySide6.QtWidgets import QWidget
from scripts.UI_scripts.InGameUI_ui import Ui_Form
from PySide6.QtCore import Qt

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
        
        self.move(15,180)