from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Painting(object):
    def setupUi(self, Painting):
        Painting.setObjectName("Painting")
        Painting.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(Painting)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(250, 550, 100, 30))
        self.btn.setObjectName("btn")
        Painting.setCentralWidget(self.centralwidget)

        self.retranslateUi(Painting)
        QtCore.QMetaObject.connectSlotsByName(Painting)

    def retranslateUi(self, Painting):
        _translate = QtCore.QCoreApplication.translate
        Painting.setWindowTitle(_translate("Painting", "MainWindow"))
        self.btn.setText(_translate("Painting", "Create cirle"))
