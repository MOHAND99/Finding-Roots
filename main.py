from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget
# from UserInterfaces.calculator import Ui_MainWindow
# from UserInterfaces.browse import Ui_Browse
# from UserInterfaces import *
# from UserInterfaces.number_of_roots import Ui_Form
# import UserInterfaces.entry_way
# from UserInterfaces.output_window import Ui_output
# from UserInterfaces.multi_root import Ui_Dialog
# from UserInterfaces.single_root import Ui_single
# # from UserInterfaces.number_of_roots import Ui_Form
# from UserInterfaces.browse import Ui_Browse
# # from UserInterfaces.number_of_roots import Ui_Form
from UserInterfaces.entry_way import Ui_Form
# from UserInterfaces.calculator import Ui_MainWindow

# from UserInterfaces.number_of_roots import Ui_Form

app = QApplication(argv)
Form = QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
exit(app.exec_())
