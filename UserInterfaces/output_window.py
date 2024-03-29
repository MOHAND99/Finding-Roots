from PyQt5 import QtCore, QtWidgets


class Ui_output(object):

    def setupUi(self, output):
        output.setObjectName("output")
        output.resize(667, 706)
        output.setAutoFillBackground(False)
        self.iteration_label = QtWidgets.QLabel(output)
        self.iteration_label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.iteration_label.setObjectName("iteration_label")
        self.iteration_value = QtWidgets.QLabel(output)
        self.iteration_value.setGeometry(QtCore.QRect(270, 20, 55, 16))
        self.iteration_value.setObjectName("iteration_value")
        self.time_label = QtWidgets.QLabel(output)
        self.time_label.setGeometry(QtCore.QRect(20, 50, 141, 21))
        self.time_label.setObjectName("time_label")
        self.time_value = QtWidgets.QLabel(output)
        self.time_value.setGeometry(QtCore.QRect(270, 50, 55, 16))
        self.time_value.setObjectName("time_value")
        self.root_label = QtWidgets.QLabel(output)
        self.root_label.setGeometry(QtCore.QRect(20, 90, 141, 21))
        self.root_label.setObjectName("root_label")
        self.root_value = QtWidgets.QLabel(output)
        self.root_value.setGeometry(QtCore.QRect(270, 90, 200, 16))
        self.root_value.setObjectName("root_value")
        self.precision_label = QtWidgets.QLabel(output)
        self.precision_label.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.precision_label.setObjectName("precision_label")
        self.precision_value = QtWidgets.QLabel(output)
        self.precision_value.setGeometry(QtCore.QRect(270, 120, 55, 16))
        self.precision_value.setObjectName("precision_value")

        self.table = QtWidgets.QTableWidget(output)
        self.table.setGeometry(QtCore.QRect(20, 170, 631, 371))
        self.table.setObjectName("table_iteration")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        # self.restart = QtWidgets.QPushButton(output)
        # self.restart.setText("restart")
        # self.restart.setGeometry(QtCore.QRect(510, 650, 141, 31))
        # self.restart.setObjectName("restart")
        # self.restart.clicked.connect(self.restart)

        self.retranslateUi(output)
        QtCore.QMetaObject.connectSlotsByName(output)

    def retranslateUi(self, output):
        _translate = QtCore.QCoreApplication.translate
        output.setWindowTitle(_translate("output", "Output"))
        self.iteration_label.setText(
            _translate("output", "Number Of Iteration"))
        self.iteration_value.setText(_translate("output", "50"))
        self.time_label.setText(_translate("output", "Execution Time (sec.)"))
        self.time_value.setText(_translate("output", "3000"))
        self.root_label.setText(_translate("output", "Approximate Root"))
        self.root_value.setText(_translate("output", "5"))
        self.precision_label.setText(_translate("output", "Precision"))
        self.precision_value.setText(_translate("output", "0.00005"))

    def set_table_vals(self, data):
        col_count = len(data[0])
        row_count = len(data) - 1

        self.table.setRowCount(row_count)
        self.table.setColumnCount(col_count)
        self.table.setHorizontalHeaderLabels(data[0])

        for i in range(row_count):
            col_ind = 0
            for j in range(col_count):
                self.table.setItem(
                    i, col_ind+j, QtWidgets.QTableWidgetItem(str(data[i+1][j])))
                self.table.horizontalHeader().setSectionResizeMode(
                    j, QtWidgets.QHeaderView.Stretch)

    def set_time(self, time):
        self.time_value.setText(str(time))

    def set_iteration_value(self, v):
        self.iteration_value.setText(str(v))

    def set_root_value(self, v):
        self.root_value.setText(str(v))

    def set_prec_val(self, v):
        self.precision_value.setText(str(v))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    output = QtWidgets.QDialog()
    ui = Ui_output()
    ui.setupUi(output)
    ui.set_time(300)
    l = [['Xi', 'Xi+1', 'Prec'], [2, 3, 444444444444],
         [2, 3, 4], [2, 3, 4], [2, 3, 4]]
    ui.set_table_vals(l)
    output.show()
    sys.exit(app.exec_())
