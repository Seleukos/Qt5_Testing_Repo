from PyQt5.QtWidgets import *

class Widget(QGraphicsView):
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
        # self.setWindowIcon()


        # Changing the MainWindow geometry:
        # Origin and Size of MainWindow:
        self.int_origin_x = 100
        self.int_origin_y = 100
        self.int_length = 1000
        self.int_width = 800
        self.setGeometry(self.int_origin_x, self.int_origin_y, self.int_length, self.int_width)



