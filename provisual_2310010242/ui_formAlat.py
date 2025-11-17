# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formAlat.ui'
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
        Form.resize(585, 267)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 571, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDAlatLabel = QLabel(self.formLayoutWidget)
        self.iDAlatLabel.setObjectName(u"iDAlatLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDAlatLabel)

        self.alatEdit = QLineEdit(self.formLayoutWidget)
        self.alatEdit.setObjectName(u"alatEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.alatEdit)

        self.namaAlatLabel = QLabel(self.formLayoutWidget)
        self.namaAlatLabel.setObjectName(u"namaAlatLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaAlatLabel)

        self.namaEdit = QLineEdit(self.formLayoutWidget)
        self.namaEdit.setObjectName(u"namaEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.namaEdit)

        self.kapasitasMuatanLabel = QLabel(self.formLayoutWidget)
        self.kapasitasMuatanLabel.setObjectName(u"kapasitasMuatanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.kapasitasMuatanLabel)

        self.kapasitasEdit = QLineEdit(self.formLayoutWidget)
        self.kapasitasEdit.setObjectName(u"kapasitasEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.kapasitasEdit)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 100, 341, 161))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 110, 80, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 150, 80, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 190, 80, 24))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(360, 230, 221, 21))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cariLabel = QLabel(self.formLayoutWidget_2)
        self.cariLabel.setObjectName(u"cariLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.cariLabel)

        self.cariEdit = QLineEdit(self.formLayoutWidget_2)
        self.cariEdit.setObjectName(u"cariEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cariEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDAlatLabel.setText(QCoreApplication.translate("Form", u"ID Alat", None))
        self.namaAlatLabel.setText(QCoreApplication.translate("Form", u"Nama Alat", None))
        self.kapasitasMuatanLabel.setText(QCoreApplication.translate("Form", u"Kapasitas Muatan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Alat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Alat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Kapasitas Muatan", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.cariLabel.setText(QCoreApplication.translate("Form", u"Cari", None))
    # retranslateUi

