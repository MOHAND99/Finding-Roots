  
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class OutputWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super(OutputWindow, self).__init__()
        loadUi(r"UserInterfaces/output.ui", self)
        self.iteration_value = self.findChild(QtWidgets.QLabel,"iteration_value")
        self.table = self.findChild(QtWidgets.QTableWidget, "tabel_iteration")
        self.exec_time = self.findChild(QtWidgets.QLabel, "time_value")
        self.root_val = self.findChild(QtWidgets.QLabel, "root_value")
        self.precision = self.findChild(QtWidgets.QLabel, "precision_value")

    def set_table_vals(self, di, type):
        if type == "secant":       
            l_dict = len(di)  
            self.table.setRowCount(l_dict)
            self.table.setColumnCount(4)
            self.table.setHorizontalHeaderLabels(["Xi-1", "Xi", "Xi+1","Precision"])
            r = 0
            c = 0
            for k,v in di.items():
                self.table.setItem(r,c,QtWidgets.QTableWidgetItem(str(v[0])))
                self.table.setItem(r,c+1,QtWidgets.QTableWidgetItem(str(v[1])))
                self.table.setItem(r,c+2,QtWidgets.QTableWidgetItem(str(v[2])))
                self.table.setItem(r,c+3,QtWidgets.QTableWidgetItem(str(v[3])))
                r += 1
            self.table.resizeColumnsToContents()
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass
        elif type == "":
            pass

    def set_iteration_value(self, v):      
        self.iteration_value.setText(v)

    def set_root_value(self, v):
        self.root_val.setText(v)

    def set_prec_val(self, v):
        self.precision.setText(v)
