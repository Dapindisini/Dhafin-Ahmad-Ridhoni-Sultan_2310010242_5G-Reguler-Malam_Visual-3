# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from pekerja import pekerja
from jadwal import jadwal
from lokasi import lokasi
from alat import alat   # ⬅️ TAMBAHKAN INI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === Load file UI utama ===
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)
        muatFile = QUiLoader()
        self.FormMenu = muatFile.load(filenya, self)
        filenya.close()

        # Atur ukuran & tampilkan menu bar
        self.resize(self.FormMenu.size())
        self.setMenuBar(self.FormMenu.menuBar())

        # === Hubungkan menu dengan form ===
        self.FormMenu.actionData_Pekerja.triggered.connect(self.bukaFormPekerja)
        self.FormMenu.actionData_Jadwal.triggered.connect(self.bukaFormJadwal)
        self.FormMenu.actionData_Lokasi.triggered.connect(self.bukaFormLokasi)
        self.FormMenu.actionAlat_Berat.triggered.connect(self.bukaFormAlat)   # ⬅️ Tambah MENU ALAT

    # === Fungsi untuk buka form pekerja ===
    def bukaFormPekerja(self):
        self.tampilPekerja = pekerja()
        self.tampilPekerja.show()

    # === Fungsi untuk buka form jadwal ===
    def bukaFormJadwal(self):
        self.tampilJadwal = jadwal()
        self.tampilJadwal.show()

    # === Fungsi untuk buka form lokasi ===
    def bukaFormLokasi(self):
        self.tampilLokasi = lokasi()
        self.tampilLokasi.show()

    # === Fungsi untuk buka form alat ===
    def bukaFormAlat(self):      # ⬅️ FUNGSI BARU
        self.tampilAlat = alat()
        self.tampilAlat.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
