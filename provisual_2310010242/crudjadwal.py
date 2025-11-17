import mysql.connector

class crudjadwal:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dapintambang'
        )

    # 🔹 SIMPAN
    def simpanJadwal(self, id_jadwal, id_pekerja, jam_kerja, lokasi):
        cur = self.koneksi.cursor()
        cur.execute(
            "INSERT INTO jadwal_piket (id_jadwal, id_pekerja, jam_kerja, lokasi) VALUES (%s, %s, %s, %s)",
            (id_jadwal, id_pekerja, jam_kerja, lokasi)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 UBAH
    def ubahJadwal(self, id_jadwal, id_pekerja, jam_kerja, lokasi):
        cur = self.koneksi.cursor()
        cur.execute(
            "UPDATE jadwal_piket SET id_pekerja=%s, jam_kerja=%s, lokasi=%s WHERE id_jadwal=%s",
            (id_pekerja, jam_kerja, lokasi, id_jadwal)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 HAPUS
    def hapusJadwal(self, id_jadwal):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM jadwal_piket WHERE id_jadwal=%s", (id_jadwal,))
        self.koneksi.commit()
        cur.close()

    # 🔹 TAMPIL
    def tampilJadwal(self):
        cur = self.koneksi.cursor()
        # Join ke tabel pekerja agar bisa tampilkan nama pekerja juga
        cur.execute("""
            SELECT j.id_jadwal, p.id_pekerja, p.nama AS nama_pekerja, j.jam_kerja, j.lokasi
            FROM jadwal_piket j
            JOIN pekerja p ON j.id_pekerja = p.id_pekerja
            ORDER BY j.id_jadwal ASC
        """)
        hasil = cur.fetchall()
        cur.close()
        return hasil
