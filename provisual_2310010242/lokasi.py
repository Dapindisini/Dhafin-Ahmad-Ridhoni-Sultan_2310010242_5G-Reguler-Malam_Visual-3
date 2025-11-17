# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crudlokasi import crudlokasi


class lokasi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        file_ui = QFile("formLokasi.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formLokasi = loader.load(file_ui, self)
        file_ui.close()

        self.resize(self.formLokasi.width(), self.formLokasi.height())

        # Object CRUD
        self.aksiCrud = crudlokasi()

        # Tombol
        self.formLokasi.pushButton.clicked.connect(self.aksiSimpan)
        self.formLokasi.pushButton_2.clicked.connect(self.aksiUbah)
        self.formLokasi.pushButton_3.clicked.connect(self.aksiHapus)

        # Klik tabel → tampil ke input
        self.formLokasi.tabelWidget.cellClicked.connect(self.tampilKeInput)

        # EVENT PENCARIAN
        self.formLokasi.cariEdit.textChanged.connect(self.aksiCari)

        # Tampil data awal
        self.tampilData()


    # -------------------------
    # TAMPIL DATA
    # -------------------------
    def tampilData(self):
        data = self.aksiCrud.tampilLokasi()
        self.isiTabel(data)


    # -------------------------
    # ISI TABEL (dipakai ulang)
    # -------------------------
    def isiTabel(self, data):
        tabel = self.formLokasi.tabelWidget
        tabel.setRowCount(0)

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for col_number, value in enumerate(row_data):
                tabel.setItem(row_number, col_number, QTableWidgetItem(str(value)))

        tabel.resizeColumnsToContents()


    # -------------------------
    # CARI DATA (OTOMATIS)
    # -------------------------
    def aksiCari(self):
        keyword = self.formLokasi.cariEdit.text()

        if keyword == "":
            self.tampilData()
            return

        data = self.aksiCrud.cariLokasi(keyword)
        self.isiTabel(data)


    # -------------------------
    # SIMPAN
    # -------------------------
    def aksiSimpan(self):
        id = self.formLokasi.idEdit.text()
        nama = self.formLokasi.namaEdit.text()
        koordinat = self.formLokasi.koordinatEdit.text()
        luas = self.formLokasi.luasEdit.text()

        if id == "" or nama == "":
            QMessageBox.warning(self, "Peringatan", "ID dan Nama Lokasi wajib diisi!")
            return

        self.aksiCrud.simpanLokasi(id, nama, koordinat, luas)
        QMessageBox.information(self, "Berhasil", "Data lokasi berhasil disimpan!")

        self.tampilData()
        self.kosongkanInput()


    # -------------------------
    # UBAH
    # -------------------------
    def aksiUbah(self):
        id = self.formLokasi.idEdit.text()
        nama = self.formLokasi.namaEdit.text()
        koordinat = self.formLokasi.koordinatEdit.text()
        luas = self.formLokasi.luasEdit.text()

        if id == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        self.aksiCrud.ubahLokasi(id, nama, koordinat, luas)
        QMessageBox.information(self, "Berhasil", "Data lokasi berhasil diubah!")

        self.tampilData()
        self.kosongkanInput()


    # -------------------------
    # HAPUS
    # -------------------------
    def aksiHapus(self):
        id = self.formLokasi.idEdit.text()

        if id == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus data ID {id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            self.aksiCrud.hapusLokasi(id)
            QMessageBox.information(self, "Berhasil", "Data lokasi berhasil dihapus!")
            self.tampilData()
            self.kosongkanInput()


    # -------------------------
    # TAMPIL KE INPUT
    # -------------------------
    def tampilKeInput(self, row, column):
        tabel = self.formLokasi.tabelWidget

        self.formLokasi.idEdit.setText(tabel.item(row, 0).text())
        self.formLokasi.namaEdit.setText(tabel.item(row, 1).text())
        self.formLokasi.koordinatEdit.setText(tabel.item(row, 2).text())
        self.formLokasi.luasEdit.setText(tabel.item(row, 3).text())


    # -------------------------
    # KOSONGKAN INPUT
    # -------------------------
    def kosongkanInput(self):
        self.formLokasi.idEdit.clear()
        self.formLokasi.namaEdit.clear()
        self.formLokasi.koordinatEdit.clear()
        self.formLokasi.luasEdit.clear()
