####################
# Modul_MainWindow #
####################

from PyQt5.QtCore import *
## For background:
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure



def create_widget():
    main_window = Widget()
    return main_window


class Widget(QWidget):

    # Constructor of "Main_Window"
    def __init__(self):

        super().__init__()

        self.initui()

    def initui(self):

        #############################################################################################################
        # Modifications:                                                                                            #
        #############################################################################################################

        # Window-Title of Main_Window
        self.str_windowname = 'TestingWidget'
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

        #

        gridlayout = QGridLayout()

        ################################
        self.instance_qgraphicsview = QGraphicsView()

        self.instance_ggraphicsscene = QGraphicsScene()

        self.instance_qgraphicsview.setScene(self.instance_ggraphicsscene)

        self.blackpen = QPen(Qt.red)
        self.blackpen.setWidth(6)

        self.instance_ggraphicsscene.addEllipse(10,10, 1000, 10000, self.blackpen)
        self.instance_ggraphicsscene.addText("Hello World!")
        self.button = QPushButton("Test")
        self.instance_ggraphicsscene.addWidget(self.button)
        self.instance_qgraphicsview.setMaximumSize(100, 100)

        ################################
        self.instance_qgraphicsview2 = QGraphicsView()

        self.instance_ggraphicsscene2 = QGraphicsScene()

        self.instance_qgraphicsview2.setScene(self.instance_ggraphicsscene)


        width = 5
        height = 5
        dpi = 100
        self.figure = Figure(figsize=(width, height), dpi=dpi)

        self.instance_qgraphicsview.setMaximumSize(100, 100)

        self.instance_ggraphicsscene.addWidget(self.figure)

        canvas = FigureCanvasQTAgg()
        canvas.add_figure(self.figure)


        gridlayout.addWidget(self.instance_qgraphicsview, 0, 0, 1, 1)
        gridlayout.addWidget(self.instance_ggraphicsscene, 0, 1, 1, 1)
        self.setLayout(gridlayout)

        print("Geschafft!")


        # Show object of "MainWindow":
        self.show()

