from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt
from database import get_connection

class JadwalProduksiWindow(QWidget):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.setWindowTitle("CRUD Jadwal Produksi Pertambangan")
        self.setGeometry(300, 150, 900, 500)

        # === Input Fields ===
        self.bulan = QLineEdit()
        self.tahun = QLineEdit()
        self.volume_ob = QLineEdit()
        self.volume_coal = QLineEdit()
        self.excavator = QLineEdit()
        self.dumptruck = QLineEdit()

        form1 = QHBoxLayout()
        form1.addWidget(QLabel("Bulan:"))
        form1.addWidget(self.bulan)
        form1.addWidget(QLabel("Tahun:"))
        form1.addWidget(self.tahun)

        form2 = QHBoxLayout()
        form2.addWidget(QLabel("Volume OB:"))
        form2.addWidget(self.volume_ob)
        form2.addWidget(QLabel("Volume Coal:"))
        form2.addWidget(self.volume_coal)

        form3 = QHBoxLayout()
        form3.addWidget(QLabel("Excavator:"))
        form3.addWidget(self.excavator)
        form3.addWidget(QLabel("Dumptruck:"))
        form3.addWidget(self.dumptruck)

        # === Tombol CRUD ===
        self.btn_tambah = QPushButton("Tambah")
        self.btn_edit = QPushButton("Edit")
        self.btn_hapus = QPushButton("Hapus")
        self.btn_kembali = QPushButton("Kembali")

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_hapus)
        btn_layout.addWidget(self.btn_kembali)
        btn_layout.addStretch()

        # === Tabel ===
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Bulan", "Tahun", "Volume OB", "Volume Coal", "Excavator", "Dumptruck"]
        )
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.cellClicked.connect(self.on_table_click)

        # === Layout utama ===
        left_layout = QVBoxLayout()
        left_layout.addLayout(form1)
        left_layout.addLayout(form2)
        left_layout.addLayout(form3)
        left_layout.addWidget(self.table)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 4)
        main_layout.addLayout(btn_layout, 1)
        self.setLayout(main_layout)

        # === Event handler ===
        self.btn_tambah.clicked.connect(self.add_record)
        self.btn_edit.clicked.connect(self.edit_record)
        self.btn_hapus.clicked.connect(self.delete_record)
        self.btn_kembali.clicked.connect(self.go_back)

        self.load_data()

    # === Load table data ===
    def load_data(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM jadwal_produksi")
        rows = c.fetchall()
        conn.close()

        self.table.setRowCount(0)
        for row in rows:
            row_index = self.table.rowCount()
            self.table.insertRow(row_index)
            for col_index, data in enumerate(row):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(data)))

    # === Click table → show to form ===
    def on_table_click(self, row, column):
        self.bulan.setText(self.table.item(row, 1).text())
        self.tahun.setText(self.table.item(row, 2).text())
        self.volume_ob.setText(self.table.item(row, 3).text())
        self.volume_coal.setText(self.table.item(row, 4).text())
        self.excavator.setText(self.table.item(row, 5).text())
        self.dumptruck.setText(self.table.item(row, 6).text())

    # === CRUD ===
    def add_record(self):
        data = (
            self.bulan.text(),
            self.tahun.text(),
            self.volume_ob.text(),
            self.volume_coal.text(),
            self.excavator.text(),
            self.dumptruck.text()
        )
        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            INSERT INTO jadwal_produksi (bulan, tahun, volume_overburden, volume_coal, alat_excavator, alat_dumptruck)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, data)
        conn.commit()
        conn.close()
        self.load_data()
        QMessageBox.information(self, "Sukses", "Data berhasil ditambahkan!")

    def edit_record(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Error", "Pilih data yang ingin diedit!")
            return
        id_ = int(self.table.item(row, 0).text())

        data = (
            self.bulan.text(),
            self.tahun.text(),
            self.volume_ob.text(),
            self.volume_coal.text(),
            self.excavator.text(),
            self.dumptruck.text(),
            id_
        )

        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            UPDATE jadwal_produksi
            SET bulan=%s, tahun=%s, volume_overburden=%s, volume_coal=%s, alat_excavator=%s, alat_dumptruck=%s
            WHERE id=%s
        """, data)
        conn.commit()
        conn.close()
        self.load_data()
        QMessageBox.information(self, "Sukses", "Data berhasil diubah!")

    def delete_record(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Error", "Pilih data yang ingin dihapus!")
            return
        id_ = int(self.table.item(row, 0).text())

        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM jadwal_produksi WHERE id=%s", (id_,))
        conn.commit()
        conn.close()
        self.load_data()
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")

    def go_back(self):
        self.close()
        if self.mainwindow:
            self.mainwindow.show()
