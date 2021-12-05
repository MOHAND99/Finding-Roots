from PyQt5 import QtCore, QtGui, QtWidgets
from multi_root import Ui_Dialog
from single_root import Ui_single

class Ui_Form(object):
    
    def cancelActio(self):
        self.window.closeEvent()


##problem here if the radiocheck button of single_root is checked manually?? bec. it not print error if you don't choose method
    def okAction(self):
        if self.radioButton.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
        elif self.radioButton_2.isChecked():
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_single()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("Must choose method to solve")


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(314, 332))
        Form.setMaximumSize(QtCore.QSize(314, 332))
       
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 270, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelActio)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 270, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.okAction)
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 251, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
       
## here we need to make single radio button unchecked  
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 180, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("50")
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 220, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("0.00001")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "number of roots"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.groupBox.setTitle(_translate("Form", "Roots"))
        self.radioButton.setText(_translate("Form", "multi"))
        self.radioButton_2.setText(_translate("Form", "single"))
        self.label_2.setText(_translate("Form", "max iterations"))
        self.label_3.setText(_translate("Form", "precision"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
