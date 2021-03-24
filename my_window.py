#!/usr/bin/env python3
import os
import sys

from PyQt5 import QtWidgets, uic
from egcd1 import *

_scriptdir = os.path.dirname(os.path.realpath(__file__))


class MainDialog(*uic.loadUiType(os.path.join(_scriptdir, 'window.ui'))):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bind_events()

    def bind_events(self):
        self.cancel.clicked.connect(self.close)
        self.input.clicked.connect(self.egcd_buttom)

    def egcd_buttom(self):
        first = self.first_space.text()
        second = self.second_space.text()
        string = result(first, second)
        self.output.setText(str(string))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()

    sys.exit(app.exec_())
