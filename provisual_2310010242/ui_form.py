# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 380)
        self.actionData_Pekerja = QAction(MainWindow)
        self.actionData_Pekerja.setObjectName(u"actionData_Pekerja")
        self.actionData_Jadwal = QAction(MainWindow)
        self.actionData_Jadwal.setObjectName(u"actionData_Jadwal")
        self.actionData_Lokasi = QAction(MainWindow)
        self.actionData_Lokasi.setObjectName(u"actionData_Lokasi")
        self.actionAlat_Berat = QAction(MainWindow)
        self.actionAlat_Berat.setObjectName(u"actionAlat_Berat")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuHalaman_Utama = QMenu(self.menubar)
        self.menuHalaman_Utama.setObjectName(u"menuHalaman_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Utama.menuAction())
        self.menuHalaman_Utama.addSeparator()
        self.menuHalaman_Utama.addSeparator()
        self.menuHalaman_Utama.addAction(self.actionData_Pekerja)
        self.menuHalaman_Utama.addAction(self.actionData_Jadwal)
        self.menuHalaman_Utama.addAction(self.actionData_Lokasi)
        self.menuHalaman_Utama.addAction(self.actionAlat_Berat)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Pekerja.setText(QCoreApplication.translate("MainWindow", u"Pekerja", None))
        self.actionData_Jadwal.setText(QCoreApplication.translate("MainWindow", u"Jadwal Piket", None))
        self.actionData_Lokasi.setText(QCoreApplication.translate("MainWindow", u"Lokasi Tambang", None))
        self.actionAlat_Berat.setText(QCoreApplication.translate("MainWindow", u"Alat Berat", None))
        self.menuHalaman_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Halaman Utama", None))
    # retranslateUi

