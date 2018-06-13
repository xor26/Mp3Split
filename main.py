import random
import sys
from PyQt5 import QtGui

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication, QLabel, QLineEdit, QInputDialog, QTextEdit, QAction, QFileDialog,
                             QMainWindow)
from PyQt5.QtGui import QColor, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        newFont = QtGui.QFont("Times", 12)
        self.fileLabel = QLabel(self)
        self.fileLabel.setGeometry(10, 20, 200, 20)
        self.fileLabel.setText("da fuck")
        self.fileLabel.setFont(newFont)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Toggle button')
        self.show()

        # self.col = QColor(0, 0, 0)
        #
        # splitBtn = QPushButton('Split', self)
        # splitBtn.setCheckable(True)
        # splitBtn.move(250, 250)
        #
        # splitBtn.clicked[bool].connect(self.splitMp3)







    def splitMp3(self):
        print("hello")

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            # self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
