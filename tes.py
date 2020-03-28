import ui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class App(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.var_interval.setText('2')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    form = App()
    form.show()

    app.exec_()