import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class OutputWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super(OutputWindow, self).__init__()
        loadUi(r"UserInterfaces/output.ui", self)
        self.iteration_value = self.findChild(QtWidgets.QLabel,"iteration_value")
        self.table = self.findChild(QtWidgets.QTableView, "tabel_iteration")
        self.exec_time = self.findChild(QtWidgets.QLabel, "time_value")
        self.app_root = self.findChild(QtWidgets.QLabel, "root_value")
        self.precision = self.findChild(QtWidgets.QLabel, "precision_value")


    def set_iteration_value(self, v):
        
        self.iteration_value.setText(v)

fn_eq = "x**2+x-6"
res = secant_eq(equ=fn_eq, x_prev=1, x_curr=1.1, iter=50, prec=0.003)
print(res[1])











