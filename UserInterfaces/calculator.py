from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        loadUi('calculator.ui', self)

        self.cosine.clicked.connect(self.__add_to_output("cos("))
        self.sine.clicked.connect(self.__add_to_output("sin("))
        self.exp.clicked.connect(self.__add_to_output("exp("))
        
        self.show()

    def __add_to_output(self, text):
        self.outputlabel.setText(self.outputlabel.text + text + " ")


app = QApplication(sys.argv)   # Create an instance of QtWidgets.QApplication
window = Calculator()   # Create an instance of our class
app.exec_()
