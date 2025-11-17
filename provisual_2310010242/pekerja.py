# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crudpekerja import crudpekerja

class pekerja(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        file_ui = QFile("formPekerja.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPekerja = loader.load(file_ui, self)
        file_ui.close()


        self.resize(self.formPekerja.width(), self.formPekerja.height())


        self.aksiCrud = crudpekerja()


        self.formPekerja.btnSimpan.clicked.connect(self.aksiSimpanPekerja)
        self.formPekerja.btnUbah.clicked.connect(self.aksiUbahPekerja)
        self.formPekerja.btnHapus.clicked.connect(self.aksiHapusPekerja)


        self.formPekerja.tabelPekerja.cellClicked.connect(self.tampilKeInput)


        self.tampilDataPekerja()


    def tampilDataPekerja(self):
        data = self.aksiCrud.tampilPekerja()
        tabel = self.formPekerja.tabelPekerja
        tabel.setRowCount(0)

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for col_number, value in enumerate(row_data):
                tabel.setItem(row_number, col_number, QTableWidgetItem(str(value)))

        tabel.resizeColumnsToContents()


    def aksiSimpanPekerja(self):
        id = self.formPekerja.pekerjaEdit.text()
        nama = self.formPekerja.namaEdit.text()
        jabatan = self.formPekerja.jabatanEdit.text()
        status = self.formPekerja.statusComboBox.currentText()

        if id == "" or nama == "":
            QMessageBox.warning(self, "Peringatan", "ID dan Nama wajib diisi!")
            return

        self.aksiCrud.simpanPekerja(id, nama, jabatan, status)
        QMessageBox.information(self, "Berhasil", "Data berhasil disimpan!")

        self.tampilDataPekerja()
        self.kosongkanInput()


    def aksiUbahPekerja(self):
        id = self.formPekerja.pekerjaEdit.text()
        nama = self.formPekerja.namaEdit.text()
        jabatan = self.formPekerja.jabatanEdit.text()
        status = self.formPekerja.statusComboBox.currentText()

        if id == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        self.aksiCrud.ubahPekerja(id, nama, jabatan, status)
        QMessageBox.information(self, "Berhasil", "Data berhasil diubah!")

        self.tampilDataPekerja()
        self.kosongkanInput()


    def aksiHapusPekerja(self):
        id = self.formPekerja.pekerjaEdit.text()

        if id == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin ingin menghapus data dengan ID {id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            self.aksiCrud.hapusPekerja(id)
            QMessageBox.information(self, "Berhasil", "Data berhasil dihapus!")
            self.tampilDataPekerja()
            self.kosongkanInput()


    def tampilKeInput(self, row, column):
        tabel = self.formPekerja.tabelPekerja
        id = tabel.item(row, 0).text()
        nama = tabel.item(row, 1).text()
        jabatan = tabel.item(row, 2).text()
        status = tabel.item(row, 3).text()

        self.formPekerja.pekerjaEdit.setText(id)
        self.formPekerja.namaEdit.setText(nama)
        self.formPekerja.jabatanEdit.setText(jabatan)
        index = self.formPekerja.statusComboBox.findText(status)
        if index != -1:
            self.formPekerja.statusComboBox.setCurrentIndex(index)


    def kosongkanInput(self):
        self.formPekerja.pekerjaEdit.clear()
        self.formPekerja.namaEdit.clear()
        self.formPekerja.jabatanEdit.clear()
        self.formPekerja.statusComboBox.setCurrentIndex(0)
