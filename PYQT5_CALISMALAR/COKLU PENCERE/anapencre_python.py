# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anapencre_python.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 20, 281, 261))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 51, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 81, 17))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(80, 100, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(80, 130, 111, 51))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 18))
        self.menubar.setObjectName("menubar")
        self.menudosya = QtWidgets.QMenu(self.menubar)
        self.menudosya.setObjectName("menudosya")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.urunlistele = QtWidgets.QAction(MainWindow)
        self.urunlistele.setObjectName("urunlistele")
        self.kategoriEkle = QtWidgets.QAction(MainWindow)
        self.kategoriEkle.setObjectName("kategoriEkle")
        self.menudosya.addAction(self.urunlistele)
        self.menudosya.addAction(self.kategoriEkle)
        self.menubar.addAction(self.menudosya.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Ürün Ekle"))
        self.label.setText(_translate("MainWindow", "Ürün Adı"))
        self.label_2.setText(_translate("MainWindow", "Miktarı"))
        self.label_3.setText(_translate("MainWindow", "Kategorisi"))
        self.label_4.setText(_translate("MainWindow", "Açıklama "))
        self.pushButton.setText(_translate("MainWindow", "Ekle"))
        self.menudosya.setTitle(_translate("MainWindow", "Ürünler"))
        self.urunlistele.setText(_translate("MainWindow", "Ürün Listele"))
        self.kategoriEkle.setText(_translate("MainWindow", "Ürün Kategori Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
