##############
# Modul_Main #
##############

# import libraries:
import sys
import PyQt5.uic as uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


# import moduls:
#from modul_stretchdata import StretchData
#from modul_project_data import ProjectData

# package_gui
from package_gui.modul_mainwindow import *




def init_program(str_logfile_name):

    print("The method has been called!")


def main():
    # Variables:
    str_logfile_name = "Test"

    # Initialization of the QApplication:
    app = QtWidgets.QApplication(sys.argv)

    # Initialization of the 'SuMo' program
    init_program(str_logfile_name)


    #stretch_data = StretchData()
    main_window = create_mainwindow()
    print("main_window has been created!")

    # Application is closed:

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()








