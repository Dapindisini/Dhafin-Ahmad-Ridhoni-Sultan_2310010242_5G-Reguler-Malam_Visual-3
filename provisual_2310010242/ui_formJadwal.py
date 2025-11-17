# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formJadwal.ui'
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
        Form.resize(420, 562)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 401, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDJadwalLabel = QLabel(self.formLayoutWidget)
        self.iDJadwalLabel.setObjectName(u"iDJadwalLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDJadwalLabel)

        self.idEdit = QLineEdit(self.formLayoutWidget)
        self.idEdit.setObjectName(u"idEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idEdit)

        self.iDPekerjaLabel = QLabel(self.formLayoutWidget)
        self.iDPekerjaLabel.setObjectName(u"iDPekerjaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDPekerjaLabel)

        self.pekerjaComboBox = QComboBox(self.formLayoutWidget)
        self.pekerjaComboBox.setObjectName(u"pekerjaComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.pekerjaComboBox)

        self.jamKerjaLabel = QLabel(self.formLayoutWidget)
        self.jamKerjaLabel.setObjectName(u"jamKerjaLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jamKerjaLabel)

        self.jamEdit = QLineEdit(self.formLayoutWidget)
        self.jamEdit.setObjectName(u"jamEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jamEdit)

        self.lokasiLabel = QLabel(self.formLayoutWidget)
        self.lokasiLabel.setObjectName(u"lokasiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lokasiLabel)

        self.lokasiEdit = QLineEdit(self.formLayoutWidget)
        self.lokasiEdit.setObjectName(u"lokasiEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lokasiEdit)

        self.simpanBtn = QPushButton(Form)
        self.simpanBtn.setObjectName(u"simpanBtn")
        self.simpanBtn.setGeometry(QRect(20, 170, 80, 24))
        self.ubahBtn = QPushButton(Form)
        self.ubahBtn.setObjectName(u"ubahBtn")
        self.ubahBtn.setGeometry(QRect(110, 170, 80, 24))
        self.hapusBtn = QPushButton(Form)
        self.hapusBtn.setObjectName(u"hapusBtn")
        self.hapusBtn.setGeometry(QRect(200, 170, 80, 24))
        self.tabelJadwal = QTableWidget(Form)
        if (self.tabelJadwal.columnCount() < 3):
            self.tabelJadwal.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelJadwal.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelJadwal.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelJadwal.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabelJadwal.setObjectName(u"tabelJadwal")
        self.tabelJadwal.setGeometry(QRect(10, 200, 401, 341))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDJadwalLabel.setText(QCoreApplication.translate("Form", u"ID Jadwal", None))
        self.iDPekerjaLabel.setText(QCoreApplication.translate("Form", u"ID Pekerja", None))
        self.jamKerjaLabel.setText(QCoreApplication.translate("Form", u"Jam Kerja", None))
        self.lokasiLabel.setText(QCoreApplication.translate("Form", u"Lokasi", None))
        self.simpanBtn.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.ubahBtn.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.hapusBtn.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tabelJadwal.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Jadwal", None));
        ___qtablewidgetitem1 = self.tabelJadwal.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem2 = self.tabelJadwal.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lokasi", None));
    # retranslateUi

