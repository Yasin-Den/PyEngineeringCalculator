from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from calculatorGUI import Ui_calculator
from numpy import *
from matplotlib.pyplot import *
import sys

class APPclass(Ui_calculator):
    def __init__(self):
        super().__init__()

    def num0(self):
        self.textEdit.insertPlainText('0')

    def num1(self):
        self.textEdit.insertPlainText('1')

    def num2(self):
        self.textEdit.insertPlainText('2')

    def num3(self):
        self.textEdit.insertPlainText('3')

    def num4(self):
        self.textEdit.insertPlainText('4')

    def num5(self):
        self.textEdit.insertPlainText('5')

    def num6(self):
        self.textEdit.insertPlainText('6')

    def num7(self):
        self.textEdit.insertPlainText('7')

    def num8(self):
        self.textEdit.insertPlainText('8')

    def num9(self):
        self.textEdit.insertPlainText('9')

    def dot(self):
        self.textEdit.insertPlainText('.')

    def x(self):
        self.textEdit.insertPlainText('x')

    def plus(self):
        self.textEdit.insertPlainText('+')

    def zarb(self):
        self.textEdit.insertPlainText('*')

    def manfi(self):
        self.textEdit.insertPlainText('-')

    def taghsim(self):
        self.textEdit.insertPlainText('/')

    def parantez1(self):
        self.textEdit.insertPlainText('(')

    def parantez2(self):
        self.textEdit.insertPlainText(')')

    def pi(self):
        self.textEdit.insertPlainText('pi')

    def e(self):
        self.textEdit.insertPlainText('e')

    def persent(self):
        self.textEdit.insertPlainText('%')

    def tavan(self):
        self.textEdit.insertPlainText('^')

    def ln(self):
        self.textEdit.insertPlainText('ln')

    def log(self):
        self.textEdit.insertPlainText('log')

    def radical(self):
        self.textEdit.insertPlainText('sqrt')

    def tavan2(self):
        self.textEdit.insertPlainText('^2')

    def tenx(self):
        self.textEdit.insertPlainText('10^')

    def EXP(self):
        self.textEdit.insertPlainText('exp')

    def sin(self):
        self.textEdit.insertPlainText('sin')

    def cos(self):
        self.textEdit.insertPlainText('cos')

    def tan(self):
        self.textEdit.insertPlainText('tan')

    def cot(self):
        self.textEdit.insertPlainText('cot')

    def arcsin(self):
        self.textEdit.insertPlainText('arcsin')

    def arccos(self):
        self.textEdit.insertPlainText('arccos')

    def arctan(self):
        self.textEdit.insertPlainText('arctan')

    def arccot(self):
        self.textEdit.insertPlainText('arccot')

    def sinh(self):
        self.textEdit.insertPlainText('sinh')

    def cosh(self):
        self.textEdit.insertPlainText('cosh')

    def tanh(self):
        self.textEdit.insertPlainText('tanh')

    def coth(self):
        self.textEdit.insertPlainText('coth')

    def arcsinh(self):
        self.textEdit.insertPlainText('arcsinh')

    def arccosh(self):
        self.textEdit.insertPlainText('arccosh')

    def arctanh(self):
        self.textEdit.insertPlainText('arctanh')

    def arccoth(self):
        self.textEdit.insertPlainText('arccoth')

    def plot(self):
        a=float(self.lineEdit1.text())
        b=float(self.lineEdit2.text())
        x=arange(a,b,(b-a)/1000)
        expression=self.texeEdit.toPlainText()
        y=eval(expression)
        plot(x,y)
        grid()
        show()
    
    def mosavi(self):
        expression=self.texeEdit.toPlainText()
        answer=eval(expression)
        self.texeEdit.toPlainText(' =\n\n'+str(answer))
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = APPclass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
