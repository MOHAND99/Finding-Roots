from PyQt5 import QtCore, QtGui, QtWidgets
from multi_root import Ui_Dialog
from single_root import Ui_single
from decimal import Decimal


class Ui_Form(object):
    def cancelAction(self):
        self.window.closeEvent()

# #problem here if the radiocheck button of single_root is checked manually??
#  bec. it not print error if you don't choose method

    def okAction(self, data):
        self.window = QtWidgets.QMainWindow()
        data.first_point = Decimal(str(self.first_root.text()))
        data.second_point = Decimal(
            str(self.sec_root.text())
            ) if self.sec_root.text() else data.second_point
        data.precision = Decimal(str(self.precision.text()))
        data.max_iterations = int(self.max_iterations.text())
        if self.radioButton.isChecked():
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window, data)
            self.window.show()
        elif self.radioButton_2.isChecked():
            self.ui = Ui_single()
            self.ui.setupUi(self.window, data)
            self.window.show()
        else:
            print("Must choose method to solve")

        self.Form.close()

    def setupUi(self, Form, data):
        self.Form = Form
        Form.setObjectName("Form")

        Form.resize(314, 430)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(314, 430))
        Form.setMaximumSize(QtCore.QSize(314, 430))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelAction)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.okAction(data))

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 251, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        # here we need to make single radio button unchecked
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

        self.max_iterations = QtWidgets.QLineEdit(Form)
        self.max_iterations.setGeometry(QtCore.QRect(170, 180, 113, 31))
        self.max_iterations.setObjectName("max_iterations")
        self.max_iterations.setText(str(data.max_iterations))

        self.first_root = QtWidgets.QLineEdit(Form)
        self.first_root.setGeometry(QtCore.QRect(170, 260, 113, 30))
        self.first_root.setObjectName("first_root")

        self.sec_root = QtWidgets.QLineEdit(Form)
        self.sec_root.setGeometry(QtCore.QRect(170, 300, 113, 30))
        self.sec_root.setObjectName("sec_root")
        self.sec_root.setPlaceholderText("Enter If Exist")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.first_root_label = QtWidgets.QLabel(Form)
        self.first_root_label.setGeometry(QtCore.QRect(30, 260, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_root_label.setFont(font)
        self.first_root_label.setObjectName("first_root_label")

        self.sec_root_label = QtWidgets.QLabel(Form)
        self.sec_root_label.setGeometry(QtCore.QRect(30, 300, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sec_root_label.setFont(font)
        self.sec_root_label.setObjectName("sec_root_label")

        self.precision = QtWidgets.QLineEdit(Form)
        self.precision.setGeometry(QtCore.QRect(170, 220, 113, 31))
        self.precision.setObjectName("precision")
        self.precision.setText(str(data.precision))

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
        self.first_root_label.setText(_translate("Form", "First Point"))
        self.sec_root_label.setText(_translate("Form", "Second Point"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
