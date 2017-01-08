#!/usr/bin/python2.7

import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("pyDwarf GUI")
        self.setWindowIcon(QtGui.QIcon('dwarf.png'))
        self.show()
        
app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
