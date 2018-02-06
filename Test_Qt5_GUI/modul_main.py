##############
# Modul_Main #
##############

# import libraries:
import sys
import PyQt5.uic as uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

# package_gui
from Test_Qt5_GUI.package_gui.module_widget import *

def main():

    # Initialization of the QApplication:
    app = QtWidgets.QApplication(sys.argv)

    main_window = create_widget()
    print("Widget has been created!")

    # Application is closed:
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()








