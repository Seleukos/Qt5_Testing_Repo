####################
# Modul_MainWindow #
####################

from PyQt5.QtCore import *
## For background:
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *




# import of moduls:





def create_mainwindow():
    #print_append_logfile("The method 'create_new_mainwindow_widget' has been called!")
    main_window = MainWindow()
    return main_window


class MainWindow(QMainWindow):
    # Discription
    # The MainWindow is the central
    # Variables:
    # self.str_windowname = 'Streckenmodulator' (warum passt das nicht hier auch?

    # Constructor of "Main_Window"
    def __init__(self):

        super().__init__()

        self.initui()

    def initui(self):

        #############################################################################################################
        # Modifications:                                                                                            #
        #############################################################################################################

        # Window-Title of Main_Window
        self.str_windowname = '[SuMo]SurroundingsModulator'
        self.setWindowTitle("%s" % self.str_windowname)

        # Change the window icon
        #self.setWindowIcon()


        # Changing the MainWindow geometry:
        # Origin and Size of MainWindow:
        self.int_origin_x = 100
        self.int_origin_y = 100
        self.int_length = 1000
        self.int_width = 800
        self.setGeometry(self.int_origin_x, self.int_origin_y, self.int_length, self.int_width)
        # (x-coordinate of left upper edge, y-coordinate of left upper edge,int_width of window, heigth of window)



        # Show object of "MainWindow":
        self.show()



