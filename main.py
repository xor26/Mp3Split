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
        self.fileNameLabel = QLabel(self)
        self.fileNameLabel.setText('File:')
        self.fileNameLabel.move(20, 20)

        self.filePathLine = QLineEdit(self)
        self.filePathLine.move(80, 20)
        self.filePathLine.resize(450, 32)
        self.filePathLine.setEnabled(False)
        self.filePathLine.setText("/")

        self.chooseFileBtn = QPushButton('Open', self)
        self.chooseFileBtn.move(460, 20)
        self.chooseFileBtn.resize(70, 31)
        # self.chooseFileBtn.setShortcut('Ctrl+O')
        self.chooseFileBtn.clicked[bool].connect(self.chooseFileDialog)

        # --------------------------
        self.outputDirLabel = QLabel(self)
        self.outputDirLabel.setText('Output:')
        self.outputDirLabel.move(20, 60)

        self.outputDirLine = QLineEdit(self)
        self.outputDirLine.move(80, 60)
        self.outputDirLine.resize(450, 32)
        self.outputDirLine.setEnabled(False)
        self.outputDirLine.setText("/")

        self.chooseOutputDirBtn = QPushButton('Choose', self)
        self.chooseOutputDirBtn.move(460, 60)
        self.chooseOutputDirBtn.resize(70, 31)
        # self.chooseOutputDirBtn.setShortcut('Ctrl+O')
        self.chooseOutputDirBtn.clicked[bool].connect(self.chooseOutputDirBtnDialog)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Toggle button')
        self.show()


    def splitMp3(self):
        print("hello")

    def chooseFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                  "/home/user", "Music (*.mp3)", options=options)
        if fileName:
            self.filePathLine.setText(fileName)
            print(fileName)

    def chooseOutputDirBtnDialog(self):
        print('hello')
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
        #                                           "/home/user", "Music (*.mp3)", options=options)
        # if fileName:
        #     self.filePathLine.setText(fileName)
        #     print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
