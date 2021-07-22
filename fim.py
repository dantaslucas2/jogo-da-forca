# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fim.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_fim(object):

    def __init__(self, mensagem, pai=None, avo=None, classe_pai=None):
        self.pai = pai
        self.avo = avo
        self.mensagem = mensagem
        self.classe_pai = classe_pai

    def reiniciar(self):
        self.pai.close()
        self.classe_pai.reiniciar()
        self.Form = QtWidgets.QMainWindow()
        self.ui = self.classe_pai
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.Form_fim.close()


    def sair(self):
        import sys
        sys.exit()

    def categorias(self):
        self.Form_fim.close()
        self.pai.close()
        self.avo.show()


    def setupUi(self, Form):
        self.Form_fim = Form
        Form.setObjectName("Form")
        Form.resize(314, 133)
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        self.Mensagem = QtWidgets.QLabel(Form)
        self.Mensagem.setGeometry(QtCore.QRect(20, 40, 281, 26))
        self.Mensagem.setAlignment(QtCore.Qt.AlignCenter)
        self.Mensagem.setObjectName("Mensagem")
        self.pb_reiniciar = QtWidgets.QPushButton(Form)
        self.pb_reiniciar.setGeometry(QtCore.QRect(10, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_reiniciar.setFont(font)
        self.pb_reiniciar.setObjectName("pb_reiniciar")
        self.pb_reiniciar.clicked.connect(self.reiniciar)
        self.pb_sair = QtWidgets.QPushButton(Form)
        self.pb_sair.setGeometry(QtCore.QRect(210, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pb_sair.setFont(font)
        self.pb_sair.setObjectName("pb_sair")
        self.pb_sair.clicked.connect(self.sair)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.categorias)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Mensagem.setText(self.mensagem)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Fim de Jogo"))
        self.Mensagem.setText(_translate("Form", "Perdeu!!"))
        self.pb_reiniciar.setText(_translate("Form", "Reiniciar"))
        self.pb_sair.setText(_translate("Form", "Sair"))
        self.pushButton.setText(_translate("Form", "Categorias"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = ui_fim()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
