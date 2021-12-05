from PyQt5 import QtCore, QtGui, QtWidgets
from number_of_roots import Ui_Form


class Ui_MainWindow(object):
    def __add_to_output(self, text):
        self.outputlabel.setText(self.outputlabel.text() + text)

    def __backspace(self):
        self.outputlabel.setText(self.outputlabel.text()[:-1])

    def __erase(self):
        self.outputlabel.setText("")

    def findRoots(self, data):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        data.equation = self.outputlabel.text()
        self.ui.setupUi(self.window, data)
        self.window.show()
        Ui_MainWindow.equation = self.outputlabel.text()
        self.MainWindow.close()

    def setupUi(self, MainWindow, data):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(10, 20, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setLineWidth(2)
        self.outputlabel.setText("")
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight
                                      | QtCore.Qt.AlignTrailing
                                      | QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.cosine = QtWidgets.QPushButton(self.centralwidget)
        self.cosine.setGeometry(QtCore.QRect(10, 130, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cosine.setFont(font)
        self.cosine.setObjectName("cosine")
        self.cosine.clicked.connect(lambda: self.__add_to_output("cos("))

        self.sine = QtWidgets.QPushButton(self.centralwidget)
        self.sine.setGeometry(QtCore.QRect(120, 130, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sine.setFont(font)
        self.sine.setObjectName("sine")
        self.sine.clicked.connect(lambda: self.__add_to_output("sin("))

        self.exp = QtWidgets.QPushButton(self.centralwidget)
        self.exp.setGeometry(QtCore.QRect(230, 130, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.exp.setFont(font)
        self.exp.setObjectName("exp")
        self.exp.clicked.connect(lambda: self.__add_to_output("exp("))

        self.X_ = QtWidgets.QPushButton(self.centralwidget)
        self.X_.setGeometry(QtCore.QRect(10, 190, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.X_.setFont(font)
        self.X_.setObjectName("X_")
        self.X_.clicked.connect(lambda: self.__add_to_output("x"))

        self.backspace = QtWidgets.QPushButton(self.centralwidget)
        self.backspace.setGeometry(QtCore.QRect(290, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backspace.setFont(font)
        self.backspace.setObjectName("backspace")
        self.backspace.clicked.connect(self.__backspace)

        self.l_bracket = QtWidgets.QPushButton(self.centralwidget)
        self.l_bracket.setGeometry(QtCore.QRect(120, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_bracket.setFont(font)
        self.l_bracket.setObjectName("l_bracket")
        self.r_bracket = QtWidgets.QPushButton(self.centralwidget)
        self.r_bracket.setGeometry(QtCore.QRect(170, 190, 51, 51))

        font = QtGui.QFont()
        font.setPointSize(18)
        self.r_bracket.setFont(font)
        self.r_bracket.setObjectName("r_bracket")

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(60, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.one.setFont(font)
        self.one.setObjectName("one")

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(10, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.three.setFont(font)
        self.three.setObjectName("three")

        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(10, 400, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")

        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(180, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.division.setFont(font)
        self.division.setObjectName("division")
        
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(110, 350, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(230, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
       
        self.erase = QtWidgets.QPushButton(self.centralwidget)
        self.erase.setGeometry(QtCore.QRect(290, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.erase.setFont(font)
        self.erase.setObjectName("erase")
        self.erase.clicked.connect(self.__erase)
        
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(180, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
       
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(60, 350, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
       
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
       
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(230, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
       
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(110, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.two.setFont(font)
        self.two.setObjectName("two")
        
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(110, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.five.setFont(font)
        self.five.setObjectName("five")
       
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(10, 350, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.six.setFont(font)
        self.six.setObjectName("six")
        
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(60, 300, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.four.setFont(font)
        self.four.setObjectName("four")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 470, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.findRoots(data))
        
        self.power = QtWidgets.QPushButton(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(180, 350, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.power.setFont(font)
        self.power.setObjectName("power")
        
        self.space = QtWidgets.QPushButton(self.centralwidget)
        self.space.setGeometry(QtCore.QRect(90, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.space.setFont(font)
        self.space.setObjectName("space")
        self.space.clicked.connect(lambda: self.__add_to_output(" "))
        self.space.clicked.connect(lambda: self.__add_to_output(" "))

        self.multiply.clicked.connect(lambda: self.__add_to_output("*"))
        self.division.clicked.connect(lambda: self.__add_to_output("/"))
        self.plus.clicked.connect(lambda: self.__add_to_output("+"))
        self.minus.clicked.connect(lambda: self.__add_to_output("-"))
        self.power.clicked.connect(lambda: self.__add_to_output("**"))
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cosine.setText(_translate("MainWindow", "cos("))
        self.sine.setText(_translate("MainWindow", "sin("))
        self.exp.setText(_translate("MainWindow", "exp("))
        self.X_.setText(_translate("MainWindow", "x"))
        self.backspace.setText(_translate("MainWindow", "Del"))
        self.l_bracket.setText(_translate("MainWindow", "("))
        self.r_bracket.setText(_translate("MainWindow", ")"))
        self.one.setText(_translate("MainWindow", "1"))
        self.three.setText(_translate("MainWindow", "3"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.division.setText(_translate("MainWindow", "/"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.erase.setText(_translate("MainWindow", "C"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.two.setText(_translate("MainWindow", "2"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.four.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "Find Roots"))
        self.power.setText(_translate("MainWindow", "**"))
        self.space.setText(_translate("MainWindow", "space"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
