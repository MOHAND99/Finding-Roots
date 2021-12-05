from PyQt5 import QtCore, QtGui, QtWidgets
from calculator import Ui_MainWindow
from browse import Ui_Browse

class Ui_Form(object):
    def cancelButton(self):
        self.window.closeEvent()

    def okButton(self, data):
        if self.gui.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window, data)
            self.window.show()
        elif self.file.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Browse()
            self.ui.setupUi(self.window, data)
            self.window.show()
        else:
            print("error message")
        self.Form.close()
    

    def setupUi(self, Form, data):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(293, 252)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 251, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        
        self.gui = QtWidgets.QRadioButton(self.groupBox)
        self.gui.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gui.setFont(font)
        self.gui.setObjectName("gui")
        
        self.file = QtWidgets.QRadioButton(self.groupBox)
        self.file.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.file.setFont(font)
        self.file.setObjectName("file")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelButton)
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.okButton(data))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "entry way"))
        self.groupBox.setTitle(_translate("Form", "Equation"))
        self.gui.setText(_translate("Form", "GUI"))
        self.file.setText(_translate("Form", "file"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Ok"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
