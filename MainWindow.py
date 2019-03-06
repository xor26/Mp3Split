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
        self.chooseFileBtn.clicked[bool].connect(self.choose_file_dialog)

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
        self.chooseOutputDirBtn.clicked[bool].connect(self.choose_output_dir_btn_dialog)

        self.SplitMp3Btn = QPushButton('Split', self)
        self.SplitMp3Btn.move(460, 140)
        self.SplitMp3Btn.resize(80, 30)
        self.SplitMp3Btn.clicked[bool].connect(self.split_file)

        self.setGeometry(300, 300, 550, 180)
        self.setWindowTitle('mp3Split')
        self.show()

    def split_file(self):
        if self.isOutputDirChoosen and self.isFileChoosen:
            file = self.filePathLine.text()
            output_dir = self.outputDirLine.text()
            chunk_count = 10
            Spliter.split_file(file, output_dir, chunk_count)
            QMessageBox.about(self, "Success", "File has been splitted successfully!")
        else:
            QMessageBox.about(self, "Error", "You must choose output dir and input file")

    def choose_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                  "/home/user", "Music (*.mp3)", options=options)
        if file_name:
            self.filePathLine.setText(file_name)
            self.isFileChoosen = True

    def choose_output_dir_btn_dialog(self):
        dir_name = str(QFileDialog.getExistingDirectory(self, "Select Directory", '/home/user/'))
        if dir_name:
            self.outputDirLine.setText(dir_name)
            self.isOutputDirChoosen = True
