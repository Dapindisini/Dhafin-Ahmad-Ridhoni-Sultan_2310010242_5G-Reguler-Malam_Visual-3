# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import mysql.connector
from crudjadwal import crudjadwal


class jadwal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === Load UI ===
        file_ui = QFile("formJadwal.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formJadwal = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formJadwal.width(), self.formJadwal.height())

        # === Koneksi CRUD ===
        self.aksiCrud = crudjadwal()

        # === Isi combobox pekerja dari database ===
        self.isiComboPekerja()

        # === Hubungkan tombol ===
        self.formJadwal.simpanBtn.clicked.connect(self.aksiSimpanJadwal)
        self.formJadwal.ubahBtn.clicked.connect(self.aksiUbahJadwal)
        self.formJadwal.hapusBtn.clicked.connect(self.aksiHapusJadwal)
        self.formJadwal.tabelJadwal.cellClicked.connect(self.tampilKeInput)

        # === Tampilkan data awal ===
        self.tampilDataJadwal()

    # -------------------------
    # 🔹 Isi ComboBox dari tabel pekerja
    # -------------------------
    def isiComboPekerja(self):
        try:
            koneksi = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='dapintambang'
            )
            cur = koneksi.cursor()
            cur.execute("SELECT id_pekerja, nama FROM pekerja ORDER BY nama ASC")
            hasil = cur.fetchall()
            cur.close()
            koneksi.close()

            combo = self.formJadwal.pekerjaComboBox
            combo.clear()
            for id_pekerja, nama in hasil:
                combo.addItem(f"{nama} (ID: {id_pekerja})", id_pekerja)

        except Exception as e:
            QMessageBox.critical(self, "Kesalahan DB", f"Gagal memuat data pekerja:\n{e}")

    # -------------------------
    # 🔹 Tampilkan Data Jadwal
    # -------------------------
    def tampilDataJadwal(self):
        data = self.aksiCrud.tampilJadwal()
        tabel = self.formJadwal.tabelJadwal
        tabel.setColumnCount(5)
        tabel.setHorizontalHeaderLabels([
            "ID Jadwal", "ID Pekerja", "Nama Pekerja", "Jam Kerja", "Lokasi"
        ])
        tabel.setRowCount(0)

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for col_number, value in enumerate(row_data):
                tabel.setItem(row_number, col_number, QTableWidgetItem(str(value)))

        tabel.resizeColumnsToContents()

    # -------------------------
    # 🔹 Simpan
    # -------------------------
    def aksiSimpanJadwal(self):
        id_jadwal = self.formJadwal.idEdit.text()
        id_pekerja = self.formJadwal.pekerjaComboBox.currentData()
        jam = self.formJadwal.jamEdit.text()
        lokasi = self.formJadwal.lokasiEdit.text()

        if id_jadwal == "" or id_pekerja is None:
            QMessageBox.warning(self, "Peringatan", "ID Jadwal dan Pekerja wajib diisi!")
            return

        self.aksiCrud.simpanJadwal(id_jadwal, id_pekerja, jam, lokasi)
        QMessageBox.information(self, "Berhasil", "Data jadwal berhasil disimpan!")
        self.tampilDataJadwal()
        self.kosongkanInput()

    # -------------------------
    # 🔹 Ubah
    # -------------------------
    def aksiUbahJadwal(self):
        id_jadwal = self.formJadwal.idEdit.text()
        id_pekerja = self.formJadwal.pekerjaComboBox.currentData()
        jam = self.formJadwal.jamEdit.text()
        lokasi = self.formJadwal.lokasiEdit.text()

        if id_jadwal == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah!")
            return

        self.aksiCrud.ubahJadwal(id_jadwal, id_pekerja, jam, lokasi)
        QMessageBox.information(self, "Berhasil", "Data jadwal berhasil diubah!")
        self.tampilDataJadwal()
        self.kosongkanInput()

    # -------------------------
    # 🔹 Hapus
    # -------------------------
    def aksiHapusJadwal(self):
        id_jadwal = self.formJadwal.idEdit.text()

        if id_jadwal == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus data jadwal dengan ID {id_jadwal}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            self.aksiCrud.hapusJadwal(id_jadwal)
            QMessageBox.information(self, "Berhasil", "Data jadwal berhasil dihapus!")
            self.tampilDataJadwal()
            self.kosongkanInput()

    # -------------------------
    # 🔹 Klik tabel → tampil ke input
    # -------------------------
    def tampilKeInput(self, row, column):
        tabel = self.formJadwal.tabelJadwal
        id_jadwal = tabel.item(row, 0).text()
        id_pekerja = int(tabel.item(row, 1).text())
        jam = tabel.item(row, 3).text()
        lokasi = tabel.item(row, 4).text()

        self.formJadwal.idEdit.setText(id_jadwal)
        self.formJadwal.jamEdit.setText(jam)
        self.formJadwal.lokasiEdit.setText(lokasi)

        combo = self.formJadwal.pekerjaComboBox
        index = combo.findData(id_pekerja)
        if index >= 0:
            combo.setCurrentIndex(index)

    # -------------------------
    # 🔹 Bersihkan input
    # -------------------------
    def kosongkanInput(self):
        self.formJadwal.idEdit.clear()
        self.formJadwal.jamEdit.clear()
        self.formJadwal.lokasiEdit.clear()
        self.formJadwal.pekerjaComboBox.setCurrentIndex(-1)
