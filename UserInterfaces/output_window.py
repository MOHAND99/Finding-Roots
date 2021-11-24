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
        self.root_val = self.findChild(QtWidgets.QLabel, "root_value")
        self.precision = self.findChild(QtWidgets.QLabel, "precision_value")

    def set_iteration_value(self, v):      
        self.iteration_value.setText(v)

    def set_root_value(self, v):
        self.root_val.setText(v)










