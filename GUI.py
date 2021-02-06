import sys
from PyQt5.QtWidgets import QApplication, QtWidgets
from PyQt5.QtGui import QIcon

class MainGui(QtWidget):
    def __init__(self):
            super.__init__()
            self.initUI()

    def initUI(self):
        self.setWindowTitle("GetALL")
        self.setWindowIcon(Qicon(''))
        self.setGeometry(500, 500, 700, 700)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainGui()
    sys.exit(app.exec_())
    