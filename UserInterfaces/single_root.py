from PyQt5 import QtCore, QtGui, QtWidgets
from output_window import Ui_output


class Ui_single(object):
    def open_method_type(self):
        if self.radioButton_2.isChecked():
            self.comboBox.clear()
            self.comboBox.addItems(
                ["Secant", "Newton Raphson", "Fixed Points"])

    def bracket_method_type(self):
        if self.radioButton.isChecked():
            self.comboBox.clear()
            self.comboBox.addItems(
                ["Bisection", "False Position"])

    # action of ok button to move to output window need here
    # to call algorithms depend on radio button
    def okAction(self, data):
        # here if he choose bracket method we need to send data to out window
        data.method = self.comboBox.currentText()
        if self.radioButton.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_output()
            self.ui.setupUi(self.window)
            self.window.show()
        # here if he choose open method we need to send data to out window
        elif self.radioButton_2.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_output()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            # here we need to show message of error
            print("Error must choose way to choose algorithms")

    # action of close button to close the current window
    def cancelAction(self):
        self.window.closeEvent

    def setupUi(self, single, data):
        single.setObjectName("single")
        single.resize(296, 300)
        single.setMinimumSize(QtCore.QSize(296, 300))
        single.setMaximumSize(QtCore.QSize(296, 300))
        
        self.pushButton_2 = QtWidgets.QPushButton(single)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelAction)

        self.groupBox = QtWidgets.QGroupBox(single)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 251, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.bracket_method_type)
       
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.open_method_type)
        
        
        self.label = QtWidgets.QLabel(single)
        self.label.setGeometry(QtCore.QRect(30, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(single)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.okAction(data))
       
        self.comboBox = QtWidgets.QComboBox(single)
        self.comboBox.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.comboBox.setObjectName("comboBox")
        

        self.retranslateUi(single)
        QtCore.QMetaObject.connectSlotsByName(single)

    def retranslateUi(self, single):
        _translate = QtCore.QCoreApplication.translate
        single.setWindowTitle(_translate("single", "single root"))
        self.pushButton_2.setText(_translate("single", "Cancel"))
        self.groupBox.setTitle(_translate("single", "Method Type"))
        self.radioButton.setText(_translate("single", "bracket"))
        self.radioButton_2.setText(_translate("single", "open"))
        self.label.setText(_translate("single", "method"))
        self.pushButton.setText(_translate("single", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    single = QtWidgets.QWidget()
    ui = Ui_single()
    ui.setupUi(single)
    single.show()
    sys.exit(app.exec_())
