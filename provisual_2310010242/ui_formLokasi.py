# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formLokasi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(825, 232)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 371, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLokasiLabel = QLabel(self.formLayoutWidget)
        self.iDLokasiLabel.setObjectName(u"iDLokasiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLokasiLabel)

        self.idEdit = QLineEdit(self.formLayoutWidget)
        self.idEdit.setObjectName(u"idEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idEdit)

        self.namaLokasiLabel = QLabel(self.formLayoutWidget)
        self.namaLokasiLabel.setObjectName(u"namaLokasiLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaLokasiLabel)

        self.namaEdit = QLineEdit(self.formLayoutWidget)
        self.namaEdit.setObjectName(u"namaEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.namaEdit)

        self.koordinatLabel = QLabel(self.formLayoutWidget)
        self.koordinatLabel.setObjectName(u"koordinatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.koordinatLabel)

        self.koordinatEdit = QLineEdit(self.formLayoutWidget)
        self.koordinatEdit.setObjectName(u"koordinatEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.koordinatEdit)

        self.luasAreaLabel = QLabel(self.formLayoutWidget)
        self.luasAreaLabel.setObjectName(u"luasAreaLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.luasAreaLabel)

        self.luasEdit = QLineEdit(self.formLayoutWidget)
        self.luasEdit.setObjectName(u"luasEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.luasEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 140, 80, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 140, 80, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 140, 80, 24))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 170, 361, 31))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cariDataLokasiLabel = QLabel(self.formLayoutWidget_2)
        self.cariDataLokasiLabel.setObjectName(u"cariDataLokasiLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.cariDataLokasiLabel)

        self.cariEdit = QLineEdit(self.formLayoutWidget_2)
        self.cariEdit.setObjectName(u"cariEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cariEdit)

        self.tabelWidget = QTableWidget(Form)
        if (self.tabelWidget.columnCount() < 4):
            self.tabelWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelWidget.setObjectName(u"tabelWidget")
        self.tabelWidget.setGeometry(QRect(390, 10, 431, 211))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDLokasiLabel.setText(QCoreApplication.translate("Form", u"ID Lokasi", None))
        self.namaLokasiLabel.setText(QCoreApplication.translate("Form", u"Nama Lokasi", None))
        self.koordinatLabel.setText(QCoreApplication.translate("Form", u"Koordinat ", None))
        self.luasAreaLabel.setText(QCoreApplication.translate("Form", u"Luas Area ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.cariDataLokasiLabel.setText(QCoreApplication.translate("Form", u"Cari Data Lokasi", None))
        ___qtablewidgetitem = self.tabelWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Lokasi", None));
        ___qtablewidgetitem1 = self.tabelWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Lokasi", None));
        ___qtablewidgetitem2 = self.tabelWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Koordinat", None));
        ___qtablewidgetitem3 = self.tabelWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Luas Area", None));
    # retranslateUi

