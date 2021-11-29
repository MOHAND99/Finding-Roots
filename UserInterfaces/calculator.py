from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
# import sys


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        loadUi('calculator.ui', self)

        self.backspace.clicked.connect(self.__backspace)
        self.erase.clicked.connect(self.__erase)

        self.space.clicked.connect(lambda: self.__add_to_output(" "))

        self.cosine.clicked.connect(lambda: self.__add_to_output("cos("))
        self.sine.clicked.connect(lambda: self.__add_to_output("sin("))
        self.exp.clicked.connect(lambda: self.__add_to_output("exp("))

        self.multiply.clicked.connect(lambda: self.__add_to_output("*"))
        self.division.clicked.connect(lambda: self.__add_to_output("/"))
        self.plus.clicked.connect(lambda: self.__add_to_output("+"))
        self.minus.clicked.connect(lambda: self.__add_to_output("-"))

        self.l_bracket.clicked.connect(lambda: self.__add_to_output("("))
        self.r_bracket.clicked.connect(lambda: self.__add_to_output(")"))

        self.one.clicked.connect(lambda: self.__add_to_output("1"))
        self.two.clicked.connect(lambda: self.__add_to_output("2"))
        self.three.clicked.connect(lambda: self.__add_to_output("3"))
        self.four.clicked.connect(lambda: self.__add_to_output("4"))
        self.five.clicked.connect(lambda: self.__add_to_output("5"))
        self.six.clicked.connect(lambda: self.__add_to_output("6"))
        self.seven.clicked.connect(lambda: self.__add_to_output("7"))
        self.eight.clicked.connect(lambda: self.__add_to_output("8"))
        self.nine.clicked.connect(lambda: self.__add_to_output("9"))
        self.zero.clicked.connect(lambda: self.__add_to_output("0"))

        self.show()

    def __add_to_output(self, text):
        self.outputlabel.setText(self.outputlabel.text() + text)

    def __backspace(self):
        self.outputlabel.setText(self.outputlabel.text()[:-1])

    def __erase(self):
        self.outputlabel.setText("")


# app = QApplication(sys.argv)   # Create an instance of QtWidgets.QApplication
# window = Calculator()   # Create an instance of our class
# app.exec_()
