import sys
import os.path
sys.path.append(os.path.dirname(__file__) + r'\UserInterfaces')
from PyQt5 import QtWidgets
from UserInterfaces.entry_way import Ui_Form
from dataclasses import dataclass


@dataclass
class Data:
    equation: str = ""
    method: str = ""


data = Data()
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form, data)
Form.show()
sys.exit(app.exec_())
