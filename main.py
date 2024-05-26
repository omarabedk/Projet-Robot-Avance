import sys
from PyQt5 import QtCore,QtGui,QtWidgets

from window import Window

app = QtWidgets.QApplication(sys.argv)

dimension = 1300, 900
mw = Window(dimension)
mw.show()
sys.exit(app.exec_())