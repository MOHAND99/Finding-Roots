  
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

    def set_table_vals(self, data):
        col_count = len(data[0])
        row_count = len(data) - 1
        self.table.setRowCount(row_count)
        self.table.setColumnCount(col_count)
        self.table.setHorizontalHeaderLabels(data[0])      
        for i in range(row_count+1):
            col_ind = 0
            for j in range(col_count):    
                self.table.setItem(i,col_ind+j,QtWidgets.QTableWidgetItem(str(data[i+1][j])))
        self.table.resizeColumnsToContents()
       

    def set_iteration_value(self, v):      
        self.iteration_value.setText(v)

    def set_root_value(self, v):
        self.root_val.setText(v)

    def set_prec_val(self, v):
        self.precision.setText(v)


                # self.table.setItem(i,col_ind+1,QtWidgets.QTableWidgetItem(str(data[i+1][1])))
                # self.table.setItem(i,col_ind+2,QtWidgets.QTableWidgetItem(str(data[i+1][2])))
                # self.table.setItem(i,col_ind+3,QtWidgets.QTableWidgetItem(str(data[i+1][3])))
            
        # elif type == "falseposition":
        #     pass
        # elif type == "newton":
        #     pass
        # elif type == "fixed_pt":
        #     pass
        # elif type == "biesection":
        #     pass 
        # elif type == "mr_first":
        #     pass
        # else:
        #     pass