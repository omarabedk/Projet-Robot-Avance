import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon

class Window(QtWidgets.QMainWindow):
    def __init__(self, dimension):
        super(Window, self).__init__()
        self.setWindowTitle("Robot Controller")
        self.setWindowIcon(QtGui.QIcon("Icons/Game-controller-Icon.png"))
        x, y = dimension
        self.setFixedWidth(x)
        self.setFixedHeight(y)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Camera widget
        self.camera_widget = QtWidgets.QWidget()
        self.layout.addWidget(self.camera_widget)
        
        self.camera_layout = QtWidgets.QGridLayout(self.camera_widget)
        self.camera_textbox = QtWidgets.QLineEdit()
        self.camera_label = QtWidgets.QLabel('')
        self.camera_textbox.textChanged.connect(self.text_box_changed)
        self.camera_layout.addWidget(self.camera_textbox, 0, 0) 
        self.camera_layout.addWidget(self.camera_label, 0, 1)

        # Modes widget
        self.modes_widget = QtWidgets.QWidget()
        self.layout.addWidget(self.modes_widget)
        
        self.modes_layout = QtWidgets.QGridLayout(self.modes_widget)
        self.modes_textbox = QtWidgets.QLineEdit()
        self.modes_label = QtWidgets.QLabel('')
        self.modes_textbox.textChanged.connect(self.text_box_changed1)
        self.modes_layout.addWidget(self.modes_textbox, 0, 0) 
        self.modes_layout.addWidget(self.modes_label, 0, 1)

    def text_box_changed(self): 
        self.camera_label.setText(self.camera_textbox.text()) 
    def text_box_changed1(self): 
        self.modes_label.setText(self.modes_textbox.text()) 
