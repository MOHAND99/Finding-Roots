import sys
import  os
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class OutputWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super(OutputWindow, self).__init__()
        loadUi(r"UserInterfaces\output.ui", self)
        self.iteration_value = self.findChild(QtWidgets.QLabel,"iteration_value")
    
    def set_iteration_value(self, v):
        self.iteration_value.setText(v)



app = QtWidgets.QApplication(sys.argv)
OutputWindow = OutputWindow()
OutputWindow.set_iteration_value("22")
widget = QtWidgets.QStackedWidget()
widget.addWidget(OutputWindow)
widget.resize(700,700)
widget.show()
sys.exit(app.exec_())













