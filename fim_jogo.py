# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fim.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 133)
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        self.Mensagem = QtWidgets.QLabel(Form)
        self.Mensagem.setGeometry(QtCore.QRect(20, 40, 281, 21))
        self.Mensagem.setAlignment(QtCore.Qt.AlignCenter)
        self.Mensagem.setObjectName("Mensagem")
        self.pb_reiniciar = QtWidgets.QPushButton(Form)
        self.pb_reiniciar.setGeometry(QtCore.QRect(10, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_reiniciar.setFont(font)
        self.pb_reiniciar.setObjectName("pb_reiniciar")
        self.pb_sair = QtWidgets.QPushButton(Form)
        self.pb_sair.setGeometry(QtCore.QRect(210, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_sair.setFont(font)
        self.pb_sair.setObjectName("pb_sair")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Fim de Jogo"))
        self.Mensagem.setText(_translate("Form", "Perdeu!!"))
        self.pb_reiniciar.setText(_translate("Form", "Reiniciar"))
        self.pb_sair.setText(_translate("Form", "Sair"))
        self.pushButton.setText(_translate("Form", "Categorias"))
