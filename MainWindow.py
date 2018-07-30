from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QFileDialog, QMainWindow, QMessageBox)

from spliter import Spliter


class MainWindow(QMainWindow):
    isFileChoosen = False
    isOutputDirChoosen = False

    def __init__(self):
        super().__init__()
        print("test")

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
        self.chooseFileBtn.clicked[bool].connect(self.chooseFileDialog)

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
        self.chooseOutputDirBtn.clicked[bool].connect(self.chooseOutputDirBtnDialog)

        self.SplitMp3Btn = QPushButton('Split', self)
        self.SplitMp3Btn.move(460, 140)
        self.SplitMp3Btn.resize(80, 30)
        self.SplitMp3Btn.clicked[bool].connect(self.splitMp3)

        self.setGeometry(300, 300, 550, 180)
        self.setWindowTitle('Toggle button')
        self.show()

    def splitMp3(self):
        if self.isOutputDirChoosen and self.isFileChoosen:
            fileName = self.filePathLine.text()
            outputDir = self.outputDirLine.text()
            chunkCount = 10
            Spliter.splitFile(fileName, outputDir, chunkCount)
            QMessageBox.about(self, "Success", "File has been splitted successfully!")
        else:
            QMessageBox.about(self, "Error", "You must choose output dir and input file")


    def chooseFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                  "/home/user", "Music (*.mp3)", options=options)
        if fileName:
            self.filePathLine.setText(fileName)
            self.isFileChoosen = True

    def chooseOutputDirBtnDialog(self):
        dirName = str(QFileDialog.getExistingDirectory(self, "Select Directory", '/home/user/'))
        if dirName:
            self.outputDirLine.setText(dirName)
            self.isOutputDirChoosen = True
