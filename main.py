import sys
from PyQt5 import QtWidgets
from Algorithm.secant import secant_eq
from UserInterfaces.output_window import OutputWindow

fn_eq = "x**2+x-6"
res = secant_eq(equ=fn_eq, x_prev=1, x_curr=1.1, iter=50, prec=0.00000001)
print(res[1])
app = QtWidgets.QApplication(sys.argv)
output_window = OutputWindow()
output_window.set_iteration_value(str(res[5]))
output_window.set_root_value(str(res[1]))
output_window.set_prec_val(str(res[4]))
output_window.set_table_vals(res[0], res[-1])
widget = QtWidgets.QStackedWidget()
widget.addWidget(output_window)
widget.resize(700, 700)
widget.show()
sys.exit(app.exec_())