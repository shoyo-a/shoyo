#from https://newbedev.com/realtime-output-from-a-subprogram-to-stdout-of-a-pyqt-widget
import sys, ctypes, subprocess

# On Windows it looks like cp850 is used for my console. We need it to decode the QByteArray correctly.
# Based on https://forum.qt.io/topic/85064/qbytearray-to-string/2
#import ctypes
#CP_console = "cp" + str(ctypes.cdll.kernel32.GetConsoleOutputCP())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextBrowser

#CP_console = "cp" + str(ctypes.cdll.kernel32.GetConsoleOutputCP())

class gui(QtWidgets.QMainWindow):
    def __init__(self):
        super(gui, self).__init__()
        self.initUI()

    def dataReady(self):
        print('dateReady Startted')
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)

        # Here we have to decode the QByteArray
        cursor.insertText(str(self.process.readLine().data().decode('utf-8')))
        self.output.ensureCursorVisible()
        print('dateReady Finished')

    def callProgram(self):
        print('callProgram Started')
        # run the process
        # `start` takes the exec and a list of arguments
        #subprocess.run('./outputNums/output.exe', shell = True)
        
        self.process.start('python3', ['-u', './tail.py'])
        #self.process.start('python3', ['./run_output copy.py'])
        #self.process.start('tail', ['-n', '1', './outputNums.log'])
        #self.process.start('ping', ['127.0.0.1'])
        print('callProgram Finished')
        


    
    def callRotine(self):
        print('callRoutine')
        self.callProgram()
    
    def cancelProgram(self):
        print('cancelProgram')
        sys.exit()

    def initUI(self):
        # Layout are better for placing widgets
        layout = QtWidgets.QVBoxLayout()
        self.runButton = QtWidgets.QPushButton('Run')
        self.runButton.clicked.connect(self.callProgram)
        self.cancelButton = QtWidgets.QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelProgram)

        #self.output = QtGui.QTextEdit()
        self.output = QTextBrowser()

        layout.addWidget(self.output)
        layout.addWidget(self.runButton)
        layout.addWidget(self.cancelButton)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        #self.process.readyRead.connect(self.dataReady)
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))


#Function Main Start
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui=gui()
    ui.show()
    sys.exit(app.exec_())
#Function Main END

if __name__ == '__main__':
    main() 