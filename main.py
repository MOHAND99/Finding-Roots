import sys
import os.path
if '/' in os.path.dirname(__file__):
    sys.path.append(os.path.dirname(__file__) + r'/UserInterfaces')
else:
    sys.path.append(os.path.dirname(__file__) + r'\UserInterfaces')
from PyQt5 import QtWidgets
from UserInterfaces.entry_way import Ui_Form
from UserInterfaces.output_window import Ui_output
from dataclasses import dataclass
from decimal import Decimal
from Algorithm.secant import secant_eq
from Algorithm.newton_raphson import newton_eq
from Algorithm.fixed_point import fixed_pt
from Algorithm.bisection import bisection
from Algorithm.falseposition import falsePosition
from Algorithm.m_r_m1 import multiple_root_mod_one
from Algorithm.m_r_m2 import multiple_root_mod_two
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

print(data.method)
print(data.equation)
method_return = []

if data.method == "Secant":
    method_return = secant_eq(
                        data.equation,
                        data.first_point, 
                        data.second_point,
                        data.max_iterations,
                        data.precision)

elif data.method == "Newton Raphson":
    method_return = newton_eq(
                        data.equation,
                        data.first_point, 
                        data.max_iterations,
                        data.precision)

elif data.method == "Fixed Point":
    method_return = fixed_pt(
                        data.equation,
                        data.first_point, 
                        data.max_iterations,
                        data.precision)

if data.method == "Bisection":
    method_return = bisection(
                        data.equation,
                        data.first_point, 
                        data.second_point,
                        data.max_iterations,
                        data.precision)

if data.method == "False Position":
    method_return = falsePosition(
                        data.equation,
                        data.first_point, 
                        data.second_point,
                        data.max_iterations,
                        data.precision)

if data.method == "m_multiple_roots":
    method_return = multiple_root_mod_one(
                        data.equation,
                        data.first_point, 
                        data.m,
                        data.max_iterations,
                        data.precision)

if data.method == "multiple_roots":
    method_return = multiple_root_mod_two(
                        data.equation,
                        data.first_point, 
                        data.max_iterations,
                        data.precision)



output = QtWidgets.QDialog()
ui = Ui_output()
ui.setupUi(output)
ui.set_iteration_value(method_return[3])
ui.set_prec_val(method_return[4])
ui.set_root_value(method_return[1])
ui.set_table_vals(method_return[0])
output.show()
sys.exit(app.exec_())
