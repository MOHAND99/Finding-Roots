from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
from output_window import Ui_output


class Ui_Dialog(object):
    def okAction(self, data):
        # here if he choose known method we need to send data to out window
        if self.radioButton.isChecked():
            # self.window = QtWidgets.QMainWindow()
            # self.ui = Ui_output()
            # self.ui.setupUi(self.window)
            # self.window.show()
            data.m = int(self.roots_count.text())
            data.method = "m_multiple_roots"

        # here if he choose unknown method we need to send data to out window
        elif self.radioButton_2.isChecked():
            data.method = "multiple_roots"
        else:
            # here we need to show message of error
            print("Error must choose way to choose algorithms")
        self.Dialog.close()

    # action of close button to close the current window
    def cancelAction(self):
        self.window.closeEvent

    def setupUi(self, Dialog, data):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(308, 300)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(308, 300))
        Dialog.setMaximumSize(QtCore.QSize(308, 300))
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 241, 151))
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
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.roots_count = QtWidgets.QLineEdit(Dialog)
        self.roots_count.setGeometry(QtCore.QRect(110, 190, 113, 31))
        self.roots_count.setObjectName("roots_count")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 190, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(162, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.okAction(data))
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancelAction)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "multi root"))
        self.groupBox.setTitle(_translate("Dialog", "Points Count"))
        self.radioButton.setText(_translate("Dialog", "known"))
        self.radioButton_2.setText(_translate("Dialog", "unknown"))
        self.label.setText(_translate("Dialog", "m = "))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
