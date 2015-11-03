# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:45:13 2015
Convertir el ui a py usando pyuic4 -o simpleWindow.py simpleWindow.ui
@author: ale
"""

import sys
from PyQt4 import QtGui
from simpleWindow import Ui_MainWindow as Dlg

class MeinDialog(QtGui.QDialog, Dlg):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)


app = QtGui.QApplication(sys.argv)
main = MeinDialog()
main.show()
sys.exit(app.exec_())