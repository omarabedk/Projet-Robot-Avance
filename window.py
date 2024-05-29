from PyQt5 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QMainWindow):
    def __init__(self, dimension):
        super(Window, self).__init__()
        self.setWindowTitle("Robot Controller")
        x, y = dimension
        self.setFixedWidth(x)
        self.setFixedHeight(y)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.modes_and_stacked_layout = QtWidgets.QHBoxLayout()

        self.Create_Camera_Widget()
        self.Create_Modes_Widget()
        self.Create_Stacked_Widget()
        self.apply_styles()

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
        self.modes_label.setFixedHeight(100)
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
        
        page1 = QtWidgets.QWidget(objectName="page1")
        page2 = QtWidgets.QWidget(objectName="page2")
        page3 = QtWidgets.QWidget(objectName="page3")
        
        self.stacked_widget.addWidget(page1)
        self.stacked_widget.addWidget(page2)
        self.stacked_widget.addWidget(page3)
        
        page1_Vlayout = QtWidgets.QVBoxLayout(page1)
        page1_Hlayout1 = QtWidgets.QHBoxLayout()
        page1_Hlayout2 = QtWidgets.QHBoxLayout()
        page2_layout = QtWidgets.QVBoxLayout(page2)
        page3_layout = QtWidgets.QVBoxLayout(page3)
        
        spacer1 = QtWidgets.QWidget()
        spacer1.setFixedSize(50, 50)
        page1_Hlayout1.addWidget(spacer1)
        Up_Bttn = QtWidgets.QPushButton("up")
        Up_Bttn.setFixedWidth(100)
        Up_Bttn.setFixedHeight(100)
        page1_Hlayout1.addWidget(Up_Bttn)
        spacer2 = QtWidgets.QWidget()
        spacer2.setFixedSize(50, 50)
        page1_Hlayout1.addWidget(spacer2)
        page1_Vlayout.addLayout(page1_Hlayout1)
        Left_Bttn = QtWidgets.QPushButton("left")
        Left_Bttn.setFixedWidth(100)
        Left_Bttn.setFixedHeight(100)
        Down_Bttn = QtWidgets.QPushButton("down")
        Down_Bttn.setFixedWidth(100)
        Down_Bttn.setFixedHeight(100)
        Right_Bttn = QtWidgets.QPushButton("right")
        Right_Bttn.setFixedWidth(100)
        Right_Bttn.setFixedHeight(100)
        page1_Hlayout2.addWidget(Left_Bttn)
        page1_Hlayout2.addWidget(Down_Bttn)
        page1_Hlayout2.addWidget(Right_Bttn)
        page1_Vlayout.addLayout(page1_Hlayout2)
        page2_layout.addWidget(QtWidgets.QLabel("You are currently on Tracking mode ..."))
        page3_layout.addWidget(QtWidgets.QLabel("You are currently on Random mode ..."))

        self.Manual_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.Tracking_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.Random_Button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))


        def keyPressEvent(self, event):
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

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
                color: #E0E0E0;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLabel {
                color: #E0E0E0;
                font-size: 16px;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
            QWidget#camera_widget {
                padding: 10px;
                border-radius: 10px;
                background-color: #666;
                margin: 10px;
            }
            QWidget#modes_widget {
                padding: 10px;
                border-radius: 10px;
                background-color: #666;
                margin: 10px;
            }
            QStackedWidget {
                padding: 10px;
                border-radius: 10px;
                background-color: #666;
                margin: 10px;
            }
            QWidget#page1 {
                padding: 10px;
                border-radius: 10px;
                margin: 10px;
            }
            QWidget#page2 {
                padding: 10px;
                border-radius: 10px;
                margin: 10px;
            }
            QWidget#page3 {
                padding: 10px;
                border-radius: 10px;
                background-color: #666;
                margin: 10px;
            }
        """)