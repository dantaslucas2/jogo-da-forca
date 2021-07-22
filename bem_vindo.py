# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bem_vindo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from jogo_da_forca import Ui_jogo

class Ui_Form(object):

    def reabrir(self):
        self.Form.show()

    def comecar_jogo_objeto(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_jogo(0, self.window)
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.window.hide()

    def comecar_jogo_fruta(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_jogo(1, self.window)
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.window.hide()

    def comecar_jogo_marca(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_jogo(2, self.window)
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.window.hide()

    def comecar_jogo_nome(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_jogo(3, self.window)
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.window.hide()

    def setupUi(self, Form):
        self.window = Form
        Form.setObjectName("Form")
        Form.resize(379, 296)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(11, 11, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.comecar_jogo_objeto)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.comecar_jogo_fruta)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.comecar_jogo_marca)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.comecar_jogo_nome)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bem vindo ao jogo da forca!"))
        self.pushButton.setText(_translate("Form", "Objetos"))
        self.pushButton_2.setText(_translate("Form", "Frutas"))
        self.pushButton_3.setText(_translate("Form", "Marcas"))
        self.pushButton_4.setText(_translate("Form", "Nomes"))
        self.label_2.setText(_translate("Form", "Selecione a categoria desejada:"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
