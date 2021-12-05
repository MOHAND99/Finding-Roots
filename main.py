import sys
import os.path
if '/' in os.path.dirname(__file__):
    sys.path.append(os.path.dirname(__file__) + r'/UserInterfaces')
else:
    sys.path.append(os.path.dirname(__file__) + r'\UserInterfaces')
from PyQt5 import QtWidgets
from UserInterfaces.entry_way import Ui_Form
from dataclasses import dataclass
from decimal import Decimal
# from pprint import pprint


@dataclass
class Data:
    first_point: Decimal = Decimal(0)
    second_point: Decimal = Decimal(0)
    equation: str = ""
    method: str = ""
    max_iterations: int = 50
    precision: Decimal = Decimal('0.00001')
    m: int = 0


data = Data()
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form, data)
Form.show()
app.exec_()
# sys.exit()
print(data.equation)
