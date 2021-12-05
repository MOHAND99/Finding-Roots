import sys
import os.path
sys.path.append(os.path.dirname(__file__) + r'\UserInterfaces')
from PyQt5 import QtWidgets
from UserInterfaces.entry_way import Ui_Form


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
