import sys
import  os
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class OutputWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super(OutputWindow, self).__init__()
        loadUi(r"UserInterfaces\output.ui", self)


app = QtWidgets.QApplication(sys.argv)
OutputWindow = OutputWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(OutputWindow)
widget.resize(700,700)
widget.show()
sys.exit(app.exec_())













