# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# CATEGORIAS: objetos, frutas, marcas, nomes


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QPushButton
import random
from fim import Ui_fim


class Ui_jogo(object):

    def reiniciar(self):
        palavra = self.selecionar_palavra(self.categoria).rstrip()
        print(palavra)
        self.segredo = ""
        self.letras = []
        for i in palavra:
            self.letras.append(i)
            self.segredo = self.segredo + "-"
        self.tentativas = []
        self.letra_selecionada = ""
        self.n_punicao = 0
        print(palavra)

    def cl_q(self):
        self.click("q")
    def cl_w(self):
        self.click("w")
    def cl_e(self):
        self.click("e")
    def cl_r(self):
        self.click("r")
    def cl_t(self):
        self.click("t")
    def cl_y(self):
        self.click("y")
    def cl_u(self):
        self.click("u")
    def cl_i(self):
        self.click("i")
    def cl_o(self):
        self.click("o")
    def cl_p(self):
        self.click("p")
    def cl_a(self):
        self.click("a")
    def cl_s(self):
        self.click("s")
    def cl_d(self):
        self.click("d")
    def cl_f(self):
        self.click("f")
    def cl_g(self):
        self.click("g")
    def cl_h(self):
        self.click("h")
    def cl_j(self):
        self.click("j")
    def cl_k(self):
        self.click("k")
    def cl_l(self):
        self.click("l")
    def cl_cc(self):
        self.click("cc")
    def cl_z(self):
        self.click("z")
    def cl_x(self):
        self.click("x")
    def cl_c(self):
        self.click("c")
    def cl_v(self):
        self.click("v")
    def cl_b(self):
        self.click("b")
    def cl_n(self):
        self.click("n")
    def cl_m(self):
        self.click("m")

    def fim(self, mensagem):
        import sys
        self.Form = QtWidgets.QDialog()
        self.ui = Ui_fim(mensagem, self.window, self.pai, self)
        self.ui.setupUi(self.Form)
        self.Form.setWindowModality(QtCore.Qt.ApplicationModal)
        self.Form.show()

    def formatar(self, lista):
        temp = ""
        for i in lista:
            if i == "cc":
                temp = ((temp + "ç") + " - ")
            else: temp = temp + i + " - "
        return temp

    def punicao(self):
        self.n_punicao = self.n_punicao + 1
        if self.n_punicao >= 1:
            self.cabeca = QPixmap("cabeca.png")
            self.cabeca = self.cabeca.scaled(self.lb_cabeca.frameGeometry().width(),self.lb_cabeca.frameGeometry().height())
            self.lb_cabeca.setPixmap(self.cabeca)
            if self.n_punicao >= 2:
                self.corpo = QPixmap("corpo.png")
                self.corpo = self.corpo.scaled(self.lb_corpo.frameGeometry().width(),self.lb_corpo.frameGeometry().height())
                self.lb_corpo.setPixmap(self.corpo)
                if self.n_punicao >= 3:
                    self.bracoesquerdo = QPixmap("braco esquerdo.png")
                    self.bracoesquerdo = self.bracoesquerdo.scaled(self.lb_bracoesquerdo.frameGeometry().width(),self.lb_bracoesquerdo.frameGeometry().height())
                    self.lb_bracoesquerdo.setPixmap(self.bracoesquerdo)
                    if self.n_punicao >= 4:
                        self.bracodireito = QPixmap("braco direito.png")
                        self.bracodireito = self.bracodireito.scaled(self.lb_bracodireito.frameGeometry().width(),self.lb_bracodireito.frameGeometry().height())
                        self.lb_bracodireito.setPixmap(self.bracodireito)
                        if self.n_punicao >= 5:
                            self.pernaesquerda = QPixmap("perna esquerda.png")
                            self.pernaesquerda = self.pernaesquerda.scaled(self.lb_pernaesquerda.frameGeometry().width(),self.lb_pernaesquerda.frameGeometry().height())
                            self.lb_pernaesquerda.setPixmap(self.pernaesquerda)
                            if self.n_punicao >= 6:
                                self.pernadireita = QPixmap("perna direita.png")
                                self.pernadireita = self.pernadireita.scaled(self.lb_pernadireita.frameGeometry().width(),self.lb_pernadireita.frameGeometry().height())
                                self.lb_pernadireita.setPixmap(self.pernadireita)
                                self.fim("Você perdeu !!")

    def click(self, letra):
        if letra not in self.tentativas:
            self.tentativas.append(letra)
            i = 0
            status = True
            while i < len(self.letras):
                if letra == self.letras[i]:
                    print("letra: ",letra)
                    print("segredo[:i]", self.segredo[:i])
                    print("segredo[i+1:]", self.segredo[i+2:])
                    status = False
                    print("Acertou miseravi")
                    self.segredo =  self.segredo[:i] + letra + self.segredo[i+1:]
                    print(self.segredo)
                i = i + 1
            if status:
                print("Errou")
                self.punicao()
        if "-" not in self.segredo :
            self.fim("Você ganhou !!")
        print("Tentativas: ", self.tentativas)
        self.label_4.setText(self.formatar(self.tentativas))
        self.lb_palavra.setText(self.segredo)
        print("***")

    def selecionar_palavra(self, categoria):
        lista = []
        count = 0

        if categoria == 0:
            with open("objetos.txt") as arquivos:
                for i in arquivos:
                    lista.append(i)
                    count = count + 1
        elif categoria == 1:
            with open("frutas.txt") as arquivos:
                for i in arquivos:
                    lista.append(i)
                    count = count + 1
        elif categoria == 2:
            with open("marcas.txt") as arquivos:
                for i in arquivos:
                    lista.append(i)
                    count = count + 1
        elif categoria == 3:
            with open("nomes.txt") as arquivos:
                for i in arquivos:
                    lista.append(i)
                    count = count + 1
        else: Ui_jogo.close()
        return lista[random.randrange(0, count)]

    def __init__(self, categoria, pai):
        self.pai = pai
        self.categoria = categoria
        palavra = self.selecionar_palavra(categoria).rstrip()
        print(palavra)
        self.segredo = ""
        self.letras = []
        for i in palavra:
            self.letras.append(i)
            self.segredo = self.segredo + "-"
        self.tentativas = []
        self.letra_selecionada = ""
        self.n_punicao = 0
        print(palavra)

    def setupUi(self, Form):
        self.window = Form
        Form.setObjectName("Form")
        Form.resize(702, 624)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.qb_a = QtWidgets.QPushButton(Form)
        self.qb_a.setGeometry(QtCore.QRect(110, 490, 41, 41))
        self.qb_a.setFont(font)
        self.qb_a.setObjectName("qb_a")
        self.qb_a.clicked.connect(self.cl_a)
        self.lb_cabeca = QtWidgets.QLabel(Form)
        self.lb_cabeca.setGeometry(QtCore.QRect(397.5, 100, 54, 70))
        self.lb_cabeca.setText("")
        self.lb_cabeca.setObjectName("lb_cabeca")
        self.qb_w = QtWidgets.QPushButton(Form)
        self.qb_w.setGeometry(QtCore.QRect(150, 440, 41, 41))
        self.qb_w.setFont(font)
        self.qb_w.setObjectName("qb_w")
        self.qb_w.clicked.connect(self.cl_w)
        self.pb_q = QtWidgets.QPushButton(Form)
        self.pb_q.setGeometry(QtCore.QRect(100, 440, 41, 41))
        self.pb_q.setFont(font)
        self.pb_q.setObjectName("pb_q")
        self.pb_q.clicked.connect(self.cl_q)
        self.qb_z = QtWidgets.QPushButton(Form)
        self.qb_z.setGeometry(QtCore.QRect(130, 540, 41, 41))
        self.qb_z.setFont(font)
        self.qb_z.setObjectName("qb_z")
        self.qb_z.clicked.connect(self.cl_z)
        self.qb_s = QtWidgets.QPushButton(Form)
        self.qb_s.setGeometry(QtCore.QRect(160, 490, 41, 41))
        self.qb_s.setFont(font)
        self.qb_s.setObjectName("qb_s")
        self.qb_s.clicked.connect(self.cl_s)
        self.qb_x = QtWidgets.QPushButton(Form)
        self.qb_x.setGeometry(QtCore.QRect(180, 540, 41, 41))
        self.qb_x.setFont(font)
        self.qb_x.setObjectName("qb_x")
        self.qb_x.clicked.connect(self.cl_x)
        self.qb_e = QtWidgets.QPushButton(Form)
        self.qb_e.setGeometry(QtCore.QRect(200, 440, 41, 41))
        self.qb_e.setFont(font)
        self.qb_e.setObjectName("qb_e")
        self.qb_e.clicked.connect(self.cl_e)
        self.qb_r = QtWidgets.QPushButton(Form)
        self.qb_r.setObjectName("qb_r")
        self.qb_r.setGeometry(QtCore.QRect(250, 440, 41, 41))
        self.qb_r.setFont(font)
        self.qb_r.clicked.connect(self.cl_r)
        self.qb_t = QtWidgets.QPushButton(Form)
        self.qb_t.setGeometry(QtCore.QRect(300, 440, 41, 41))
        self.qb_t.setFont(font)
        self.qb_t.setObjectName("qb_t")
        self.qb_t.clicked.connect(self.cl_t)
        self.qb_y = QtWidgets.QPushButton(Form)
        self.qb_y.setGeometry(QtCore.QRect(350, 440, 41, 41))
        self.qb_y.setFont(font)
        self.qb_y.setObjectName("qb_y")
        self.qb_y.clicked.connect(self.cl_y)
        self.qb_u = QtWidgets.QPushButton(Form)
        self.qb_u.setGeometry(QtCore.QRect(400, 440, 41, 41))
        self.qb_u.setFont(font)
        self.qb_u.setObjectName("qb_u")
        self.qb_u.clicked.connect(self.cl_u)
        self.qb_i = QtWidgets.QPushButton(Form)
        self.qb_i.setGeometry(QtCore.QRect(450, 440, 41, 41))
        self.qb_i.setFont(font)
        self.qb_i.setObjectName("qb_i")
        self.qb_i.clicked.connect(self.cl_i)
        self.qb_d = QtWidgets.QPushButton(Form)
        self.qb_d.setGeometry(QtCore.QRect(210, 490, 41, 41))
        self.qb_d.setFont(font)
        self.qb_d.setObjectName("qb_d")
        self.qb_d.clicked.connect(self.cl_d)
        self.qb_o = QtWidgets.QPushButton(Form)
        self.qb_o.setGeometry(QtCore.QRect(500, 440, 41, 41))
        self.qb_o.setFont(font)
        self.qb_o.setObjectName("qb_o")
        self.qb_o.clicked.connect(self.cl_o)
        self.qb_p = QtWidgets.QPushButton(Form)
        self.qb_p.setGeometry(QtCore.QRect(550, 440, 41, 41))
        self.qb_p.setFont(font)
        self.qb_p.setObjectName("qb_p")
        self.qb_p.clicked.connect(self.cl_p)
        self.qb_f = QtWidgets.QPushButton(Form)
        self.qb_f.setGeometry(QtCore.QRect(260, 490, 41, 41))
        self.qb_f.setFont(font)
        self.qb_f.setObjectName("qb_f")
        self.qb_f.clicked.connect(self.cl_f)
        self.qb_g = QtWidgets.QPushButton(Form)
        self.qb_g.setGeometry(QtCore.QRect(310, 490, 41, 41))
        self.qb_g.setFont(font)
        self.qb_g.setObjectName("qb_g")
        self.qb_g.clicked.connect(self.cl_g)
        self.qb_h = QtWidgets.QPushButton(Form)
        self.qb_h.setGeometry(QtCore.QRect(360, 490, 41, 41))
        self.qb_h.setFont(font)
        self.qb_h.setObjectName("qb_h")
        self.qb_h.clicked.connect(self.cl_h)
        self.qb_j = QtWidgets.QPushButton(Form)
        self.qb_j.setGeometry(QtCore.QRect(410, 490, 41, 41))
        self.qb_j.setFont(font)
        self.qb_j.setObjectName("qb_j")
        self.qb_j.clicked.connect(self.cl_j)
        self.qb_k = QtWidgets.QPushButton(Form)
        self.qb_k.setGeometry(QtCore.QRect(460, 490, 41, 41))
        self.qb_k.setFont(font)
        self.qb_k.setObjectName("qb_k")
        self.qb_k.clicked.connect(self.cl_k)
        self.qb_l = QtWidgets.QPushButton(Form)
        self.qb_l.setGeometry(QtCore.QRect(510, 490, 41, 41))
        self.qb_l.setFont(font)
        self.qb_l.setObjectName("qb_l")
        self.qb_l.clicked.connect(self.cl_l)
        self.qb_cc = QtWidgets.QPushButton(Form)
        self.qb_cc.setGeometry(QtCore.QRect(560, 490, 41, 41))
        self.qb_cc.setFont(font)
        self.qb_cc.setObjectName("qb_cc")
        self.qb_cc.clicked.connect(self.cl_cc)
        self.qb_b = QtWidgets.QPushButton(Form)
        self.qb_b.setGeometry(QtCore.QRect(330, 540, 41, 41))
        self.qb_b.setFont(font)
        self.qb_b.setObjectName("qb_b")
        self.qb_b.clicked.connect(self.cl_b)
        self.qb_c = QtWidgets.QPushButton(Form)
        self.qb_c.setGeometry(QtCore.QRect(230, 540, 41, 41))
        self.qb_c.setFont(font)
        self.qb_c.setObjectName("qb_c")
        self.qb_c.clicked.connect(self.cl_c)
        self.qb_v = QtWidgets.QPushButton(Form)
        self.qb_v.setGeometry(QtCore.QRect(280, 540, 41, 41))
        self.qb_v.setFont(font)
        self.qb_v.clicked.connect(self.cl_v)
        self.qb_v.setObjectName("qb_v")
        self.qb_m = QtWidgets.QPushButton(Form)
        self.qb_m.setGeometry(QtCore.QRect(430, 540, 41, 41))
        self.qb_m.setFont(font)
        self.qb_m.setObjectName("qb_m")
        self.qb_m.clicked.connect(self.cl_m)
        self.qb_n = QtWidgets.QPushButton(Form)
        self.qb_n.setGeometry(QtCore.QRect(380, 540, 41, 41))
        self.qb_n.setFont(font)
        self.qb_n.setObjectName("qb_n")
        self.qb_n.clicked.connect(self.cl_n)
        self.lb_corpo = QtWidgets.QLabel(Form)
        self.lb_corpo.setGeometry(QtCore.QRect(424, 170, 2, 55))
        self.lb_corpo.setText("")
        self.lb_corpo.setObjectName("lb_corpo")
        self.lb_forca = QtWidgets.QLabel(Form)
        self.lb_forca.setGeometry(QtCore.QRect(270, 10, 191, 291))
        self.lb_forca.setText("")
        self.lb_forca.setObjectName("lb_forca")
        self.lb_bracoesquerdo = QtWidgets.QLabel(Form)
        self.lb_bracoesquerdo.setGeometry(QtCore.QRect(378, 165, 44, 20))
        self.lb_bracoesquerdo.setText("")
        self.lb_bracoesquerdo.setObjectName("lb_bracoesquerdo")
        self.lb_bracodireito = QtWidgets.QLabel(Form)
        self.lb_bracodireito.setGeometry(QtCore.QRect(427, 165, 44, 20))
        self.lb_bracodireito.setText("")
        self.lb_bracodireito.setObjectName("lb_bracodireito")
        self.lb_pernaesquerda = QtWidgets.QLabel(Form)
        self.lb_pernaesquerda.setGeometry(QtCore.QRect(400, 220, 25, 50))
        self.lb_pernaesquerda.setText("")
        self.lb_pernaesquerda.setObjectName("lb_pernaesquerda")
        self.lb_pernadireita = QtWidgets.QLabel(Form)
        self.lb_pernadireita.setGeometry(QtCore.QRect(425, 220, 25, 50))
        self.lb_pernadireita.setText("")
        self.lb_pernadireita.setObjectName("lb_pernadireita")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 370, 101, 26))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_palavra = QtWidgets.QLabel(Form)
        self.lb_palavra.setGeometry(QtCore.QRect(330, 370, 291, 21))
        self.lb_palavra.setFont(font)
        self.lb_palavra.setText(self.segredo)
        self.lb_palavra.setObjectName("lb_palavra")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 400, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 400, 211, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lb_forca.raise_()
        self.qb_a.raise_()
        self.lb_cabeca.raise_()
        self.qb_w.raise_()
        self.pb_q.raise_()
        self.qb_z.raise_()
        self.qb_s.raise_()
        self.qb_x.raise_()
        self.qb_e.raise_()
        self.qb_r.raise_()
        self.qb_t.raise_()
        self.qb_y.raise_()
        self.qb_u.raise_()
        self.qb_i.raise_()
        self.qb_d.raise_()
        self.qb_o.raise_()
        self.qb_p.raise_()
        self.qb_f.raise_()
        self.qb_g.raise_()
        self.qb_h.raise_()
        self.qb_j.raise_()
        self.qb_k.raise_()
        self.qb_l.raise_()
        self.qb_cc.raise_()
        self.qb_b.raise_()
        self.qb_c.raise_()
        self.qb_v.raise_()
        self.qb_m.raise_()
        self.qb_n.raise_()
        self.lb_corpo.raise_()
        self.lb_bracoesquerdo.raise_()
        self.lb_bracodireito.raise_()
        self.lb_pernaesquerda.raise_()
        self.lb_pernadireita.raise_()
        self.label.raise_()
        self.lb_palavra.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.forca = QPixmap("forca.png")
        self.forca = self.forca.scaled(self.lb_forca.frameGeometry().width(),self.lb_forca.frameGeometry().height())
        self.lb_forca.setPixmap(self.forca)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Jogo da Forca"))
        self.qb_a.setText(_translate("Form", "A"))
        self.qb_w.setText(_translate("Form", "W"))
        self.pb_q.setText(_translate("Form", "Q"))
        self.qb_z.setText(_translate("Form", "Z"))
        self.qb_s.setText(_translate("Form", "S"))
        self.qb_x.setText(_translate("Form", "X"))
        self.qb_e.setText(_translate("Form", "E"))
        self.qb_r.setText(_translate("Form", "R"))
        self.qb_t.setText(_translate("Form", "T"))
        self.qb_y.setText(_translate("Form", "Y"))
        self.qb_u.setText(_translate("Form", "U"))
        self.qb_i.setText(_translate("Form", "I"))
        self.qb_d.setText(_translate("Form", "D"))
        self.qb_o.setText(_translate("Form", "O"))
        self.qb_p.setText(_translate("Form", "P"))
        self.qb_f.setText(_translate("Form", "F"))
        self.qb_g.setText(_translate("Form", "G"))
        self.qb_h.setText(_translate("Form", "H"))
        self.qb_j.setText(_translate("Form", "J"))
        self.qb_k.setText(_translate("Form", "K"))
        self.qb_l.setText(_translate("Form", "L"))
        self.qb_cc.setText(_translate("Form", "Ç"))
        self.qb_b.setText(_translate("Form", "B"))
        self.qb_c.setText(_translate("Form", "C"))
        self.qb_v.setText(_translate("Form", "V"))
        self.qb_m.setText(_translate("Form", "M"))
        self.qb_n.setText(_translate("Form", "N"))
        self.label.setText(_translate("Form", "Palavra: "))
        self.label_3.setText(_translate("Form", "Tentativas:"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_jogo(1)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
