from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from calculator import Calculator


class EntryWay(QMainWindow):
    def __init__(self):
        super(EntryWay, self).__init__()
        loadUi('entry_way.ui', self)
        self.gui.toggled.connect(self.__get_equation)
        self.show()

    def __get_equation(self):
        self.close()
        if self.gui.isChecked():
            return Calculator()
        return # get from file gui object


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EntryWay()   # Create an instance of our class
    app.exec_()

