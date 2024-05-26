import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon

class Window(QtWidgets.QMainWindow):
    def __init__(self,dimension):
        super(Window, self).__init__()
        self.setWindowTitle("Robot Controller")
        self.setWindowIcon(QtGui.QIcon("Icons/Game-controller-Icon.png"))
        x,y=dimension
        self.setFixedWidth(x)
        self.setFixedHeight(y)

    
