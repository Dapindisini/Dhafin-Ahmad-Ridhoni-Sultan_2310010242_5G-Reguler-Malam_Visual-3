# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crudalat import crudalat


class alat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        file_ui = QFile("formAlat.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formAlat = loader.load(file_ui, self)
        file_ui.close()

        self.resize(self.formAlat.width(), self.formAlat.height())

        # CRUD Object
        self.aksiCrud = crudalat()

        # Tombol
        self.formAlat.pushButton.clicked.connect(self.aksiSimpan)       # Simpan
        self.formAlat.pushButton_2.clicked.connect(self.aksiUbah)       # Ubah
        self.formAlat.pushButton_3.clicked.connect(self.aksiHapus)      # Hapus

        # Klik tabel
        self.formAlat.tableWidget.cellClicked.connect(self.tampilKeInput)

        # Pencarian
        self.formAlat.cariEdit.textChanged.connect(self.aksiCari)

        # Tampil data awal
        self.tampilData()


    # -------------------------
    # TAMPIL DATA
    # -------------------------
    def tampilData(self):
        data = self.aksiCrud.tampilAlat()
        self.isiTabel(data)


    # -------------------------
    # ISI TABEL
    # -------------------------
    def isiTabel(self, data):
        tabel = self.formAlat.tableWidget
        tabel.setRowCount(0)

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for col_number, value in enumerate(row_data):
                tabel.setItem(row_number, col_number, QTableWidgetItem(str(value)))

        tabel.resizeColumnsToContents()


    # -------------------------
    # CARI DATA
    # -------------------------
    def aksiCari(self):
        keyword = self.formAlat.cariEdit.text()

        if keyword == "":
            self.tampilData()
            return

        data = self.aksiCrud.cariAlat(keyword)
        self.isiTabel(data)


    # -------------------------
    # SIMPAN
    # -------------------------
    def aksiSimpan(self):
        id_alat = self.formAlat.alatEdit.text()
        nama_alat = self.formAlat.namaEdit.text()
        kapasitas = self.formAlat.kapasitasEdit.text()

        if id_alat == "" or nama_alat == "":
            QMessageBox.warning(self, "Peringatan", "ID Alat dan Nama Alat wajib diisi!")
            return

        self.aksiCrud.simpanAlat(id_alat, nama_alat, kapasitas)
        QMessageBox.information(self, "Berhasil", "Data alat berhasil disimpan!")

        self.tampilData()
        self.kosongkanInput()


    # -------------------------
    # UBAH
    # -------------------------
    def aksiUbah(self):
        id_alat = self.formAlat.alatEdit.text()
        nama_alat = self.formAlat.namaEdit.text()
        kapasitas = self.formAlat.kapasitasEdit.text()

        if id_alat == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        self.aksiCrud.ubahAlat(id_alat, nama_alat, kapasitas)
        QMessageBox.information(self, "Berhasil", "Data alat berhasil diubah!")

        self.tampilData()
        self.kosongkanInput()


    # -------------------------
    # HAPUS
    # -------------------------
    def aksiHapus(self):
        id_alat = self.formAlat.alatEdit.text()

        if id_alat == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus data alat dengan ID {id_alat}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            self.aksiCrud.hapusAlat(id_alat)
            QMessageBox.information(self, "Berhasil", "Data alat berhasil dihapus!")
            self.tampilData()
            self.kosongkanInput()


    # -------------------------
    # TAMPIL KE INPUT
    # -------------------------
    def tampilKeInput(self, row, column):
        tabel = self.formAlat.tableWidget

        self.formAlat.alatEdit.setText(tabel.item(row, 0).text())
        self.formAlat.namaEdit.setText(tabel.item(row, 1).text())
        self.formAlat.kapasitasEdit.setText(tabel.item(row, 2).text())


    # -------------------------
    # KOSONGKAN INPUT
    # -------------------------
    def kosongkanInput(self):
        self.formAlat.alatEdit.clear()
        self.formAlat.namaEdit.clear()
        self.formAlat.kapasitasEdit.clear()
