# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700,330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.jisuan = QtWidgets.QPushButton(self.centralwidget)
        self.jisuan.setGeometry(QtCore.QRect(510, 60, 101, 71))
        self.jisuan.setObjectName("jisuan")
        self.jisuan.clicked.connect(self.baofa)
        self.chongzhi = QtWidgets.QPushButton(self.centralwidget)
        self.chongzhi.setGeometry(QtCore.QRect(510, 150, 101, 71))
        self.chongzhi.setObjectName("chongzhi")
        self.chongzhi.clicked.connect(self.chongzhi_)
        self.gongjili = QtWidgets.QLabel(self.centralwidget)
        self.gongjili.setGeometry(QtCore.QRect(40, 90, 85, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.gongjili.setFont(font)
        self.gongjili.setObjectName("gongjili")
        self.gudinghuchuan = QtWidgets.QLabel(self.centralwidget)
        self.gudinghuchuan.setGeometry(QtCore.QRect(40, 130, 85, 21))
        #font = QtGui.QFont()
        #font.setFamily("Arial")
        #font.setPointSize(11)
        self.gudinghuchuan.setFont(font)
        self.gudinghuchuan.setObjectName("gudinghuchuan")
        self.dengji=QtWidgets.QLabel(self.centralwidget)
        self.dengji.setGeometry(QtCore.QRect(40,44,85,31))
        font=QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(11)
        self.dengji.setFont(font)
        self.dengji.setObjectName('dengji')
        self.xianshi=QtWidgets.QLabel(self.centralwidget)
        self.xianshi.setGeometry(QtCore.QRect(10,250,680,40))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(9)
        self.xianshi.setFont(font)
        self.xianshi.setObjectName("xianshi")
        self.baifenbichuan = QtWidgets.QLabel(self.centralwidget)
        self.baifenbichuan.setGeometry(QtCore.QRect(40, 170, 85, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.baifenbichuan.setFont(font)
        self.baifenbichuan.setObjectName("baifenbichuan")
        self.gongjili_e = QtWidgets.QLineEdit(self.centralwidget)
        self.gongjili_e.setGeometry(QtCore.QRect(150, 80, 101, 31))
        self.gongjili_e.setObjectName("gongjili_e")
        self.dengji_e=QtWidgets.QLineEdit(self.centralwidget)
        self.dengji_e.setGeometry(QtCore.QRect(150,40,101,31))
        self.dengji_e.setObjectName('dengji_e')
        self.gudinghuchuan_e = QtWidgets.QLineEdit(self.centralwidget)
        self.gudinghuchuan_e.setGeometry(QtCore.QRect(150, 120, 101, 31))
        self.gudinghuchuan_e.setObjectName("gudinghuchuan_e")
        self.baifenbichuan_e = QtWidgets.QLineEdit(self.centralwidget)
        self.baifenbichuan_e.setGeometry(QtCore.QRect(150, 160, 101, 31))
        self.baifenbichuan_e.setObjectName("baifenbichuan_e")
        self.wulifangyu = QtWidgets.QLabel(self.centralwidget)
        self.wulifangyu.setGeometry(QtCore.QRect(270, 100, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.wulifangyu.setFont(font)
        self.wulifangyu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wulifangyu.setObjectName("wulifangyu")
        self.HPzuidazhi = QtWidgets.QLabel(self.centralwidget)
        self.HPzuidazhi.setGeometry(QtCore.QRect(270, 140, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.HPzuidazhi.setFont(font)
        self.HPzuidazhi.setObjectName("HPzuidazhi")
        self.wulifangyu_e = QtWidgets.QLineEdit(self.centralwidget)
        self.wulifangyu_e.setGeometry(QtCore.QRect(380, 90, 111, 31))
        self.wulifangyu_e.setObjectName("wulifangyu_e")
        self.HPzuidazhi_e = QtWidgets.QLineEdit(self.centralwidget)
        self.HPzuidazhi_e.setGeometry(QtCore.QRect(380, 130, 111, 31))
        self.HPzuidazhi_e.setObjectName("HPzuidazhi_e")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "王者荣耀荆轲爆发计算器"))
        self.jisuan.setText(_translate("MainWindow", "计算"))
        self.chongzhi.setText(_translate("MainWindow", "重置"))
        self.gongjili.setText(_translate("MainWindow", "攻击力"))
        self.dengji.setText(_translate("MainWindow",'等级'))
        self.gudinghuchuan.setText(_translate("MainWindow", "固定护穿"))
        self.baifenbichuan.setText(_translate("MainWindow", "百分比穿"))
        self.gudinghuchuan_e.setText(_translate("MainWindow", "96"))
        self.baifenbichuan_e.setText(_translate("MainWindow", "0.45"))
        self.dengji_e.setText(_translate("MainWindow",''))
        self.wulifangyu.setText(_translate("MainWindow", "物理防御"))
        self.HPzuidazhi.setText(_translate("MainWindow", "HP最大值"))
        self.xianshi.setText(_translate("MainWindow",'结果显示在这'))

    def baofa(self):
        hujia=float(self.wulifangyu_e.text())
        gongjili=float(self.gongjili_e.text())
        gudinghuchuan=float(self.gudinghuchuan_e.text())
        baifenbihuchuan=float(self.baifenbichuan_e.text())
        dengji=int(self.dengji_e.text())
        HPzuidazhi=float(self.HPzuidazhi_e.text())
        shijihujia = hujia * (1 - baifenbihuchuan) - gudinghuchuan
        shanghaijianmian = shijihujia / (602 + shijihujia)
        gongjili_all=self.dengji_(dengji,gongjili)+gongjili
        shijishanghai = int(gongjili_all * (1 - shanghaijianmian))
        restHP=int(HPzuidazhi-shijishanghai)
        shanghaibaifenbi = shijishanghai / HPzuidazhi
        self.xianshi.setText('一套伤害约为{},占总血量的{:.2f}%剩余血量约为{}'.format(shijishanghai,shanghaibaifenbi*100,restHP))

    def dengji_(self,dengji,gongjili):
        a = {1: {1: 0, 2: 1, 3: 0}, 2: {1: 1, 2: 1, 3: 0}, 3: {1: 1, 2: 2, 3: 0}, 4: {1: 1, 2: 2, 3: 1},
             5: {1: 1, 2: 3, 3: 1}, 6: {1: 2, 2: 3, 3: 1}, 7: {1: 1, 2: 4, 3: 1}, 8: {1: 1, 2: 4, 3: 2},
             9: {1: 1, 2: 5, 3: 2}, \
             10: {1: 3, 2: 5, 3: 2}, 11: {1: 3, 2: 6, 3: 2}, 12: {1: 3, 2: 6, 3: 3}, 13: {1: 4, 2: 6, 3: 3},
             14: {1: 5, 2: 6, 3: 3}, 15: {1: 6, 2: 6, 3: 3}}
        b = {1: {1: 200, 2: 240, 3: 280, 4: 320, 5: 360, 6: 400}, 2: {1: 390, 2: 440, 3: 490, 4: 540, 5: 590, 6: 640},
             3: {1: 450, 2: 640, 3: 830}}
        sum_of_jineng=b[1][a[dengji][1]]+b[2][a[dengji][2]]+b[3][a[dengji][3]]+3.65*gongjili
        return sum_of_jineng
    def chongzhi_(self):
        self.dengji_e.setText('')
        self.gongjili_e.setText('')
        self.wulifangyu_e.setText('')
        self.HPzuidazhi_e.setText('')
        self.xianshi.setText('结果显示在这')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
