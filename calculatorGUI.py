# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from numpy import *
from matplotlib.pyplot import *
import sys


class Ui_calculator(QObject):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(524, 576)
        calculator.setLayoutDirection(QtCore.Qt.LeftToRight)
        calculator.setAutoFillBackground(False)
        calculator.setSizeGripEnabled(False)
        self.groupBox = QtWidgets.QGroupBox(calculator)
        self.groupBox.setGeometry(QtCore.QRect(370, 20, 131, 181))
        self.groupBox.setObjectName("groupBox")
        self.PB_plus = QtWidgets.QPushButton(self.groupBox)
        self.PB_plus.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.PB_plus.setObjectName("PB_plus")
        self.PB_manfi = QtWidgets.QPushButton(self.groupBox)
        self.PB_manfi.setGeometry(QtCore.QRect(10, 100, 51, 31))
        self.PB_manfi.setObjectName("PB_manfi")
        self.PB_zarb = QtWidgets.QPushButton(self.groupBox)
        self.PB_zarb.setGeometry(QtCore.QRect(70, 60, 51, 31))
        self.PB_zarb.setObjectName("PB_zarb")
        self.PB_taghsim = QtWidgets.QPushButton(self.groupBox)
        self.PB_taghsim.setGeometry(QtCore.QRect(70, 100, 51, 31))
        self.PB_taghsim.setObjectName("PB_taghsim")
        self.PB_clear = QtWidgets.QPushButton(self.groupBox)
        self.PB_clear.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.PB_clear.setDefault(True)
        self.PB_clear.setObjectName("PB_clear")
        self.PB_parantez2 = QtWidgets.QPushButton(self.groupBox)
        self.PB_parantez2.setGeometry(QtCore.QRect(70, 140, 51, 31))
        self.PB_parantez2.setObjectName("PB_parantez2")
        self.PB_parantez1 = QtWidgets.QPushButton(self.groupBox)
        self.PB_parantez1.setGeometry(QtCore.QRect(10, 140, 51, 31))
        self.PB_parantez1.setObjectName("PB_parantez1")
        self.PB_x = QtWidgets.QPushButton(self.groupBox)
        self.PB_x.setGeometry(QtCore.QRect(70, 20, 51, 31))
        self.PB_x.setObjectName("PB_x")
        self.groupBox_7 = QtWidgets.QGroupBox(calculator)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 110, 321, 231))
        self.groupBox_7.setObjectName("groupBox_7")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 295, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PB_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_3.setObjectName("PB_3")
        self.gridLayout.addWidget(self.PB_3, 0, 2, 1, 1)
        self.PB_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_2.setObjectName("PB_2")
        self.gridLayout.addWidget(self.PB_2, 0, 1, 1, 1)
        self.PB_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_5.setObjectName("PB_5")
        self.gridLayout.addWidget(self.PB_5, 1, 1, 1, 1)
        self.PB_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_4.setObjectName("PB_4")
        self.gridLayout.addWidget(self.PB_4, 1, 0, 1, 1)
        self.PB_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_9.setObjectName("PB_9")
        self.gridLayout.addWidget(self.PB_9, 2, 2, 1, 1)
        self.PB_mosavi = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_mosavi.setDefault(True)
        self.PB_mosavi.setObjectName("PB_mosavi")
        self.gridLayout.addWidget(self.PB_mosavi, 3, 2, 1, 1)
        self.PB7 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB7.setObjectName("PB7")
        self.gridLayout.addWidget(self.PB7, 2, 0, 1, 1)
        self.PB_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_0.setObjectName("PB_0")
        self.gridLayout.addWidget(self.PB_0, 3, 1, 1, 1)
        self.PB_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_6.setObjectName("PB_6")
        self.gridLayout.addWidget(self.PB_6, 1, 2, 1, 1)
        self.PB_dot = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_dot.setObjectName("PB_dot")
        self.gridLayout.addWidget(self.PB_dot, 3, 0, 1, 1)
        self.PB_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_8.setObjectName("PB_8")
        self.gridLayout.addWidget(self.PB_8, 2, 1, 1, 1)
        self.PB_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_1.setIconSize(QtCore.QSize(30, 30))
        self.PB_1.setDefault(False)
        self.PB_1.setObjectName("PB_1")
        self.gridLayout.addWidget(self.PB_1, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(calculator)
        self.tabWidget.setGeometry(QtCore.QRect(30, 370, 321, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 151, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.PB_cos = QtWidgets.QPushButton(self.groupBox_2)
        self.PB_cos.setGeometry(QtCore.QRect(80, 20, 61, 41))
        self.PB_cos.setObjectName("PB_cos")
        self.PB_tan = QtWidgets.QPushButton(self.groupBox_2)
        self.PB_tan.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.PB_tan.setObjectName("PB_tan")
        self.PB_sin = QtWidgets.QPushButton(self.groupBox_2)
        self.PB_sin.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.PB_sin.setObjectName("PB_sin")
        self.PB_cot = QtWidgets.QPushButton(self.groupBox_2)
        self.PB_cot.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.PB_cot.setObjectName("PB_cot")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 10, 151, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.PB_arccot = QtWidgets.QPushButton(self.groupBox_3)
        self.PB_arccot.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.PB_arccot.setObjectName("PB_arccot")
        self.PB_arcsin = QtWidgets.QPushButton(self.groupBox_3)
        self.PB_arcsin.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.PB_arcsin.setObjectName("PB_arcsin")
        self.PB_arccos = QtWidgets.QPushButton(self.groupBox_3)
        self.PB_arccos.setGeometry(QtCore.QRect(80, 20, 61, 41))
        self.PB_arccos.setObjectName("PB_arccos")
        self.PB_arctan = QtWidgets.QPushButton(self.groupBox_3)
        self.PB_arctan.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.PB_arctan.setObjectName("PB_arctan")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 151, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.PB_cosh = QtWidgets.QPushButton(self.groupBox_4)
        self.PB_cosh.setGeometry(QtCore.QRect(80, 20, 61, 41))
        self.PB_cosh.setObjectName("PB_cosh")
        self.PB_sinh = QtWidgets.QPushButton(self.groupBox_4)
        self.PB_sinh.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.PB_sinh.setObjectName("PB_sinh")
        self.PB_coth = QtWidgets.QPushButton(self.groupBox_4)
        self.PB_coth.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.PB_coth.setObjectName("PB_coth")
        self.PB_tanh = QtWidgets.QPushButton(self.groupBox_4)
        self.PB_tanh.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.PB_tanh.setObjectName("PB_tanh")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(160, 10, 151, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.PB_arccosh = QtWidgets.QPushButton(self.groupBox_5)
        self.PB_arccosh.setGeometry(QtCore.QRect(80, 20, 61, 41))
        self.PB_arccosh.setObjectName("PB_arccosh")
        self.PB_arcsinh = QtWidgets.QPushButton(self.groupBox_5)
        self.PB_arcsinh.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.PB_arcsinh.setObjectName("PB_arcsinh")
        self.PB_arccoth = QtWidgets.QPushButton(self.groupBox_5)
        self.PB_arccoth.setGeometry(QtCore.QRect(80, 70, 61, 41))
        self.PB_arccoth.setObjectName("PB_arccoth")
        self.PB_arctanh = QtWidgets.QPushButton(self.groupBox_5)
        self.PB_arctanh.setGeometry(QtCore.QRect(10, 70, 61, 41))
        self.PB_arctanh.setObjectName("PB_arctanh")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 10, 261, 111))
        self.groupBox_12.setObjectName("groupBox_12")
        self.PB_log = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_log.setGeometry(QtCore.QRect(190, 20, 51, 31))
        self.PB_log.setObjectName("PB_log")
        self.PB_sqrt = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_sqrt.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.PB_sqrt.setObjectName("PB_sqrt")
        self.PB_tenx = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_tenx.setGeometry(QtCore.QRect(130, 60, 51, 31))
        self.PB_tenx.setObjectName("PB_tenx")
        self.PB_tavan2 = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_tavan2.setGeometry(QtCore.QRect(70, 60, 51, 31))
        self.PB_tavan2.setObjectName("PB_tavan2")
        self.PB_ln = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_ln.setGeometry(QtCore.QRect(130, 20, 51, 31))
        self.PB_ln.setObjectName("PB_ln")
        self.PB_persent = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_persent.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.PB_persent.setObjectName("PB_persent")
        self.PB_tavan = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_tavan.setGeometry(QtCore.QRect(70, 20, 51, 31))
        self.PB_tavan.setObjectName("PB_tavan")
        self.PB_EXP = QtWidgets.QPushButton(self.groupBox_12)
        self.PB_EXP.setGeometry(QtCore.QRect(190, 60, 51, 31))
        self.PB_EXP.setObjectName("PB_EXP")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_8 = QtWidgets.QGroupBox(calculator)
        self.groupBox_8.setGeometry(QtCore.QRect(370, 410, 131, 101))
        self.groupBox_8.setObjectName("groupBox_8")
        self.PB_e = QtWidgets.QPushButton(self.groupBox_8)
        self.PB_e.setGeometry(QtCore.QRect(20, 60, 71, 31))
        self.PB_e.setObjectName("PB_e")
        self.PB_pi = QtWidgets.QPushButton(self.groupBox_8)
        self.PB_pi.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.PB_pi.setObjectName("PB_pi")
        self.textEdit = QtWidgets.QTextEdit(calculator)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 321, 61))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_9 = QtWidgets.QGroupBox(calculator)
        self.groupBox_9.setGeometry(QtCore.QRect(370, 200, 131, 201))
        self.groupBox_9.setObjectName("groupBox_9")
        self.PB_plot = QtWidgets.QPushButton(self.groupBox_9)
        self.PB_plot.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.PB_plot.setObjectName("PB_plot")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 60, 111, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit1.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 130, 111, 61))
        self.groupBox_11.setObjectName("groupBox_11")
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit2.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label = QtWidgets.QLabel(calculator)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(120, 540, 301, 20))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.retranslateUi(calculator)
        self.tabWidget.setCurrentIndex(2)
        self.PB_clear.clicked.connect(self.textEdit.clear)
        self.PB_1.clicked.connect(self.num1)
        self.PB_2.clicked.connect(self.num2)
        self.PB_3.clicked.connect(self.num3)
        self.PB_4.clicked.connect(self.num4)
        self.PB_5.clicked.connect(self.num5)
        self.PB_6.clicked.connect(self.num6)
        self.PB7.clicked.connect(self.num7)
        self.PB_8.clicked.connect(self.num8)
        self.PB_9.clicked.connect(self.num9)
        self.PB_0.clicked.connect(self.num0)
        self.PB_mosavi.clicked.connect(self.mosavi)
        self.PB_dot.clicked.connect(self.dot)
        self.PB_x.clicked.connect(self.x)
        self.PB_plus.clicked.connect(self.plus)
        self.PB_zarb.clicked.connect(self.zarb)
        self.PB_manfi.clicked.connect(self.manfi)
        self.PB_taghsim.clicked.connect(self.taghsim)
        self.PB_parantez1.clicked.connect(self.parantez1)
        self.PB_parantez2.clicked.connect(self.parantez2)
        self.PB_plot.clicked.connect(self.plot)
        self.PB_pi.clicked.connect(self.pi)
        self.PB_e.clicked.connect(self.e)
        self.PB_sin.clicked.connect(self.sin)
        self.PB_cos.clicked.connect(self.cos)
        self.PB_tan.clicked.connect(self.tan)
        self.PB_cot.clicked.connect(self.cot)
        self.PB_arcsin.clicked.connect(self.arcsin)
        self.PB_arccos.clicked.connect(self.arccos)
        self.PB_arctan.clicked.connect(self.arctan)
        self.PB_arccot.clicked.connect(self.arccot)
        self.PB_sinh.clicked.connect(self.sinh)
        self.PB_cosh.clicked.connect(self.cosh)
        self.PB_tanh.clicked.connect(self.tanh)
        self.PB_coth.clicked.connect(self.coth)
        self.PB_arcsinh.clicked.connect(self.arcsinh)
        self.PB_arccosh.clicked.connect(self.arccosh)
        self.PB_arctanh.clicked.connect(self.arctanh)
        self.PB_arccoth.clicked.connect(self.arccoth)
        self.PB_persent.clicked.connect(self.persent)
        self.PB_tavan.clicked.connect(self.tavan)
        self.PB_ln.clicked.connect(self.ln)
        self.PB_log.clicked.connect(self.log)
        self.PB_sqrt.clicked.connect(self.radical)
        self.PB_tavan2.clicked.connect(self.tavan)
        self.PB_tenx.clicked.connect(self.tenx)
        self.PB_EXP.clicked.connect(self.EXP)
        self.PB_clear.clicked.connect(self.lineEdit1.clear)
        self.PB_clear.clicked.connect(self.lineEdit2.clear)
        QtCore.QMetaObject.connectSlotsByName(calculator)
        calculator.setTabOrder(self.PB_1, self.PB_2)
        calculator.setTabOrder(self.PB_2, self.PB_3)
        calculator.setTabOrder(self.PB_3, self.PB_4)
        calculator.setTabOrder(self.PB_4, self.PB_5)
        calculator.setTabOrder(self.PB_5, self.PB_6)
        calculator.setTabOrder(self.PB_6, self.PB7)
        calculator.setTabOrder(self.PB7, self.PB_8)
        calculator.setTabOrder(self.PB_8, self.PB_9)
        calculator.setTabOrder(self.PB_9, self.PB_0)
        calculator.setTabOrder(self.PB_0, self.PB_dot)
        calculator.setTabOrder(self.PB_dot, self.PB_mosavi)
        calculator.setTabOrder(self.PB_mosavi, self.PB_clear)
        calculator.setTabOrder(self.PB_clear, self.PB_plus)
        calculator.setTabOrder(self.PB_plus, self.PB_zarb)
        calculator.setTabOrder(self.PB_zarb, self.PB_manfi)
        calculator.setTabOrder(self.PB_manfi, self.PB_taghsim)
        calculator.setTabOrder(self.PB_taghsim, self.PB_parantez1)
        calculator.setTabOrder(self.PB_parantez1, self.PB_parantez2)
        calculator.setTabOrder(self.PB_parantez2, self.PB_pi)
        calculator.setTabOrder(self.PB_pi, self.PB_e)
        calculator.setTabOrder(self.PB_e, self.PB_x)
        calculator.setTabOrder(self.PB_x, self.PB_plot)
        calculator.setTabOrder(self.PB_plot, self.tabWidget)
        calculator.setTabOrder(self.tabWidget, self.PB_sin)
        calculator.setTabOrder(self.PB_sin, self.PB_cos)
        calculator.setTabOrder(self.PB_cos, self.PB_tan)
        calculator.setTabOrder(self.PB_tan, self.PB_cot)
        calculator.setTabOrder(self.PB_cot, self.PB_arcsin)
        calculator.setTabOrder(self.PB_arcsin, self.PB_arccos)
        calculator.setTabOrder(self.PB_arccos, self.PB_arctan)
        calculator.setTabOrder(self.PB_arctan, self.PB_arccot)
        calculator.setTabOrder(self.PB_arccot, self.PB_sinh)
        calculator.setTabOrder(self.PB_sinh, self.PB_cosh)
        calculator.setTabOrder(self.PB_cosh, self.PB_tanh)
        calculator.setTabOrder(self.PB_tanh, self.PB_coth)
        calculator.setTabOrder(self.PB_coth, self.PB_arcsinh)
        calculator.setTabOrder(self.PB_arcsinh, self.PB_arccosh)
        calculator.setTabOrder(self.PB_arccosh, self.PB_arctanh)
        calculator.setTabOrder(self.PB_arctanh, self.PB_arccoth)
        calculator.setTabOrder(self.PB_arccoth, self.textEdit)

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Dialog"))
        self.groupBox.setTitle(_translate("calculator", "Basic"))
        self.PB_plus.setText(_translate("calculator", "+"))
        self.PB_manfi.setText(_translate("calculator", "-"))
        self.PB_zarb.setText(_translate("calculator", "*"))
        self.PB_taghsim.setText(_translate("calculator", "/"))
        self.PB_clear.setText(_translate("calculator", "C"))
        self.PB_parantez2.setText(_translate("calculator", ")"))
        self.PB_parantez1.setText(_translate("calculator", "("))
        self.PB_x.setText(_translate("calculator", "x"))
        self.groupBox_7.setTitle(_translate("calculator", "Number"))
        self.PB_3.setText(_translate("calculator", "3"))
        self.PB_2.setText(_translate("calculator", "2"))
        self.PB_5.setText(_translate("calculator", "5"))
        self.PB_4.setText(_translate("calculator", "4"))
        self.PB_9.setText(_translate("calculator", "9"))
        self.PB_mosavi.setText(_translate("calculator", "="))
        self.PB7.setText(_translate("calculator", "7"))
        self.PB_0.setText(_translate("calculator", "0"))
        self.PB_6.setText(_translate("calculator", "6"))
        self.PB_dot.setText(_translate("calculator", "."))
        self.PB_8.setText(_translate("calculator", "8"))
        self.PB_1.setText(_translate("calculator", "1"))
        self.groupBox_2.setTitle(_translate("calculator", "Basic"))
        self.PB_cos.setText(_translate("calculator", "Cos"))
        self.PB_tan.setText(_translate("calculator", "tan"))
        self.PB_sin.setText(_translate("calculator", "Sin"))
        self.PB_cot.setText(_translate("calculator", "cot"))
        self.groupBox_3.setTitle(_translate("calculator", "Reverse"))
        self.PB_arccot.setText(_translate("calculator", "arccot"))
        self.PB_arcsin.setText(_translate("calculator", "arcsin"))
        self.PB_arccos.setText(_translate("calculator", "arccos"))
        self.PB_arctan.setText(_translate("calculator", "arctan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("calculator", "trigonometry"))
        self.groupBox_4.setTitle(_translate("calculator", "Basic"))
        self.PB_cosh.setText(_translate("calculator", "cosh"))
        self.PB_sinh.setText(_translate("calculator", "sinh"))
        self.PB_coth.setText(_translate("calculator", "coth"))
        self.PB_tanh.setText(_translate("calculator", "tanh"))
        self.groupBox_5.setTitle(_translate("calculator", "Reverse"))
        self.PB_arccosh.setText(_translate("calculator", "arccosh"))
        self.PB_arcsinh.setText(_translate("calculator", "arcsinh"))
        self.PB_arccoth.setText(_translate("calculator", "arccoth"))
        self.PB_arctanh.setText(_translate("calculator", "arctanh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("calculator", "Hyperbolic"))
        self.groupBox_12.setTitle(_translate("calculator", "Advanced"))
        self.PB_log.setText(_translate("calculator", "log"))
        self.PB_sqrt.setText(_translate("calculator", "Radical"))
        self.PB_tenx.setText(_translate("calculator", "10^x"))
        self.PB_tavan2.setText(_translate("calculator", "x^2"))
        self.PB_ln.setText(_translate("calculator", "ln"))
        self.PB_persent.setText(_translate("calculator", "%"))
        self.PB_tavan.setText(_translate("calculator", "^"))
        self.PB_EXP.setText(_translate("calculator", "EXP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("calculator", "Advanced"))
        self.groupBox_8.setTitle(_translate("calculator", "Special numbers"))
        self.PB_e.setText(_translate("calculator", "e"))
        self.PB_pi.setText(_translate("calculator", "pi"))
        self.textEdit.setHtml(_translate("calculator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_9.setTitle(_translate("calculator", "show"))
        self.PB_plot.setText(_translate("calculator", "plot"))
        self.groupBox_10.setTitle(_translate("calculator", "From :"))
        self.groupBox_11.setTitle(_translate("calculator", "To :"))
        self.label.setText(_translate("calculator", "This calculator created by \'\'Yasin Khosh manesh\'\'"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QDialog()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())
