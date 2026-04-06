from PySide6.QtWidgets import QApplication, QMainWindow

from UI_scripts.MainWindow_ui import Ui_MainWindow

class HBMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    hb_window = HBMainWindow()
    hb_window.show()
    app.exec()