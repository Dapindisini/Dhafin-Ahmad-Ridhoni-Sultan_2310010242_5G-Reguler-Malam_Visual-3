# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPekerja.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(431, 385)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 411, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPekerjaLabel = QLabel(self.formLayoutWidget)
        self.iDPekerjaLabel.setObjectName(u"iDPekerjaLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPekerjaLabel)

        self.pekerjaEdit = QLineEdit(self.formLayoutWidget)
        self.pekerjaEdit.setObjectName(u"pekerjaEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pekerjaEdit)

        self.namaLabel = QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName(u"namaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaLabel)

        self.namaEdit = QLineEdit(self.formLayoutWidget)
        self.namaEdit.setObjectName(u"namaEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.namaEdit)

        self.jabatanLabel = QLabel(self.formLayoutWidget)
        self.jabatanLabel.setObjectName(u"jabatanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jabatanLabel)

        self.jabatanEdit = QLineEdit(self.formLayoutWidget)
        self.jabatanEdit.setObjectName(u"jabatanEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jabatanEdit)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.statusComboBox = QComboBox(self.formLayoutWidget)
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.setObjectName(u"statusComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.statusComboBox)

        self.tabelPekerja = QTableWidget(Form)
        if (self.tabelPekerja.columnCount() < 4):
            self.tabelPekerja.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPekerja.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPekerja.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPekerja.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPekerja.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelPekerja.setObjectName(u"tabelPekerja")
        self.tabelPekerja.setGeometry(QRect(10, 190, 411, 192))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 150, 80, 24))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(100, 150, 80, 24))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(189, 150, 81, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPekerjaLabel.setText(QCoreApplication.translate("Form", u"ID Pekerja", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.jabatanLabel.setText(QCoreApplication.translate("Form", u"Jabatan", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.statusComboBox.setItemText(0, QCoreApplication.translate("Form", u"Aktif", None))
        self.statusComboBox.setItemText(1, QCoreApplication.translate("Form", u"Cuti", None))
        self.statusComboBox.setItemText(2, QCoreApplication.translate("Form", u"Nonaktif", None))

        ___qtablewidgetitem = self.tabelPekerja.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pekerja", None));
        ___qtablewidgetitem1 = self.tabelPekerja.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelPekerja.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Jabatan", None));
        ___qtablewidgetitem3 = self.tabelPekerja.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Status", None));
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
    # retranslateUi

