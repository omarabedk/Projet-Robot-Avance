from PyQt5 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QMainWindow):
    def __init__(self, dimension):
        super(Window, self).__init__()
        self.setWindowTitle("Robot Controller")
        x, y = dimension
        self.setFixedWidth(x)
        self.setFixedHeight(y)

        self.Create_menu_bar()
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.modes_and_stacked_layout = QtWidgets.QHBoxLayout()

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.Create_Camera_Widget()
        self.Create_Modes_Widget()
        self.Create_Stacked_Widget()

        with open("styles.css", "r") as file:
            self.setStyleSheet(file.read())

    def Create_Camera_Widget(self):
        self.camera_widget = QtWidgets.QWidget(objectName="camera_widget")
        self.camera_layout = QtWidgets.QGridLayout(self.camera_widget)
        self.Camera_label = QtWidgets.QLabel('      Camera')
        self.IRGauche_label = QtWidgets.QLabel('IR Gauche: ')
        self.IRGauche_label.setFixedWidth(200)
        self.IRGaucheValue_label = QtWidgets.QLabel('')
        self.IRGaucheValue_label.setFixedWidth(150)
        self.IRDroite_label = QtWidgets.QLabel('IR Droite: ')
        self.IRDroite_label.setFixedWidth(200)
        self.IRDroiteValue_label = QtWidgets.QLabel('')
        self.IRDroiteValue_label.setFixedWidth(150)
        self.DistanceSensor_label = QtWidgets.QLabel('Capteur de distance: ')
        self.DistanceSensor_label.setFixedWidth(200)
        self.DistanceSensorValue_label = QtWidgets.QLabel('')
        self.DistanceSensorValue_label.setFixedWidth(150)
        self.camera_layout.addWidget(self.Camera_label, 0, 0) 
        self.camera_layout.addWidget(self.IRGauche_label, 1, 1) 
        self.camera_layout.addWidget(self.IRGaucheValue_label, 1, 2)
        self.camera_layout.addWidget(self.IRDroite_label, 2, 1) 
        self.camera_layout.addWidget(self.IRDroiteValue_label, 2, 2)
        self.camera_layout.addWidget(self.DistanceSensor_label, 3, 1) 
        self.camera_layout.addWidget(self.DistanceSensorValue_label, 3, 2)
        self.layout.addWidget(self.camera_widget)

    def Create_Modes_Widget(self):
        self.modes_widget = QtWidgets.QWidget(objectName="modes_widget")
        self.modes_layout = QtWidgets.QGridLayout(self.modes_widget)
        self.modes_label = QtWidgets.QLabel('      Modes')
        self.modes_label.setFixedHeight(50)
        self.Manual_Button = QtWidgets.QPushButton('Manual')
        self.Tracking_Button = QtWidgets.QPushButton('Tracking')
        self.Random_Button = QtWidgets.QPushButton('Random')
        self.modes_layout.addWidget(self.modes_label, 0, 0)
        self.modes_layout.addWidget(self.Manual_Button, 1, 0)
        self.modes_layout.addWidget(self.Tracking_Button, 2, 0)
        self.modes_layout.addWidget(self.Random_Button, 3, 0)
        self.modes_and_stacked_layout.addWidget(self.modes_widget)

    def Create_Stacked_Widget(self):
        self.stacked_widget = QtWidgets.QStackedWidget(objectName="stacked_widget")
        self.modes_and_stacked_layout.addWidget(self.stacked_widget)
        self.layout.addLayout(self.modes_and_stacked_layout)
        self.stacked_widget.setFixedWidth(800)
        self.stacked_widget.setFixedHeight(400)
        
        self.page1 = QtWidgets.QWidget(objectName="page1")
        self.page2 = QtWidgets.QWidget(objectName="page2")
        self.page3 = QtWidgets.QWidget(objectName="page3")
        
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        
        page1_Vlayout = QtWidgets.QVBoxLayout(self.page1)
        page1_Hlayout1 = QtWidgets.QHBoxLayout()
        page1_Hlayout2 = QtWidgets.QHBoxLayout()
        page2_layout = QtWidgets.QVBoxLayout(self.page2)
        page3_layout = QtWidgets.QVBoxLayout(self.page3)
        
        spacer1 = QtWidgets.QWidget()
        spacer1.setFixedSize(50, 50)
        page1_Hlayout1.addWidget(spacer1)
        self.Up_Bttn = QtWidgets.QPushButton()
        self.Up_Bttn.setIcon(QtGui.QIcon('Icons/up.png'))
        self.Up_Bttn.setIconSize(QtCore.QSize(80, 80))  # Adjust size as needed
        self.Up_Bttn.setFixedWidth(100)
        self.Up_Bttn.setFixedHeight(100)
        page1_Hlayout1.addWidget(self.Up_Bttn)
        spacer2 = QtWidgets.QWidget()
        spacer2.setFixedSize(50, 50)
        page1_Hlayout1.addWidget(spacer2)
        page1_Vlayout.addLayout(page1_Hlayout1)
        self.Left_Bttn = QtWidgets.QPushButton()
        self.Left_Bttn.setIcon(QtGui.QIcon('Icons/left.png'))
        self.Left_Bttn.setIconSize(QtCore.QSize(80, 80))  # Adjust size as needed
        self.Left_Bttn.setFixedWidth(100)
        self.Left_Bttn.setFixedHeight(100)
        self.Down_Bttn = QtWidgets.QPushButton()
        self.Down_Bttn.setIcon(QtGui.QIcon('Icons/down.png'))
        self.Down_Bttn.setIconSize(QtCore.QSize(80, 80))  # Adjust size as needed
        self.Down_Bttn.setFixedWidth(100)
        self.Down_Bttn.setFixedHeight(100)
        self.Right_Bttn = QtWidgets.QPushButton()
        self.Right_Bttn.setIcon(QtGui.QIcon('Icons/right.png'))
        self.Right_Bttn.setIconSize(QtCore.QSize(80, 80))  # Adjust size as needed
        self.Right_Bttn.setFixedWidth(100)
        self.Right_Bttn.setFixedHeight(100)
        page1_Hlayout2.addWidget(self.Left_Bttn)
        page1_Hlayout2.addWidget(self.Down_Bttn)
        page1_Hlayout2.addWidget(self.Right_Bttn)
        page1_Vlayout.addLayout(page1_Hlayout2)
        page2_layout.addWidget(QtWidgets.QLabel("You are currently on Tracking mode ..."))
        page3_layout.addWidget(QtWidgets.QLabel("You are currently on Random mode ..."))

        self.Manual_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0) and self.setFocusPolicy(QtCore.Qt.StrongFocus))
        self.Tracking_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.Random_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

    

    def keyPressEvent(self, event):
        if self.stacked_widget.currentWidget() == self.page1:
            if event.key() == QtCore.Qt.Key_Up:
                self.Up_Bttn.click()
            elif event.key() == QtCore.Qt.Key_Down:
                self.Down_Bttn.click()
            elif event.key() == QtCore.Qt.Key_Left:
                self.Left_Bttn.click()
            elif event.key() == QtCore.Qt.Key_Right:
                self.Right_Bttn.click()
        else:
            super(Window, self).keyPressEvent(event)


    def Create_menu_bar(self):
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu('Help')
        about_action = QtWidgets.QAction('About Us', self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    def show_about_dialog(self):
        about_msg = QtWidgets.QMessageBox(self)
        about_msg.setWindowTitle("About Us")
        about_msg.setText("-------------------------------------------------\n"
                          "This is a Robot Controller application created with PyQt5.\n"
                          "-------------------------------------------------\n"
                           "Omar ABDEL KADER | All Rights Reserved \u00A9")
        about_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        about_msg.setStyleSheet("QLabel {color: #000000;}")
        about_msg.exec_()

