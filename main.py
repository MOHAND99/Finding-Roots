from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget
# from UserInterfaces.calculator import Ui_MainWindow
# from UserInterfaces.browse import Ui_Browse
from UserInterfaces import *
# from UserInterfaces.number_of_roots import Ui_Form
# import UserInterfaces.entry_way

app = QApplication(argv)
Form = QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
exit(app.exec_())
