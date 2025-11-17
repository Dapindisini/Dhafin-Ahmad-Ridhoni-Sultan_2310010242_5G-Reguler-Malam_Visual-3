import mysql.connector

class crudalat:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dapintambang'
        )

    # 🔹 SIMPAN
    def simpanAlat(self, id_alat, nama_alat, kapasitas):
        cur = self.koneksi.cursor()
        cur.execute(
            "INSERT INTO alat_berat (id_alat, nama_alat, kapasitas) VALUES (%s, %s, %s)",
            (id_alat, nama_alat, kapasitas)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 UBAH
    def ubahAlat(self, id_alat, nama_alat, kapasitas):
        cur = self.koneksi.cursor()
        cur.execute(
            "UPDATE alat_berat SET nama_alat=%s, kapasitas=%s WHERE id_alat=%s",
            (nama_alat, kapasitas, id_alat)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 HAPUS
    def hapusAlat(self, id_alat):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM alat_berat WHERE id_alat=%s", (id_alat,))
        self.koneksi.commit()
        cur.close()

    # 🔹 TAMPIL
    def tampilAlat(self):
        cur = self.koneksi.cursor()
        cur.execute("""
            SELECT id_alat, nama_alat, kapasitas
            FROM alat_berat
            ORDER BY id_alat ASC
        """)
        hasil = cur.fetchall()
        cur.close()
        return hasil

    # 🔹 CARI
    def cariAlat(self, keyword):
        cur = self.koneksi.cursor()
        sql = """
            SELECT id_alat, nama_alat, kapasitas
            FROM alat_berat
            WHERE id_alat LIKE %s
               OR nama_alat LIKE %s
               OR kapasitas LIKE %s
        """
        param = (
            "%"+keyword+"%",
            "%"+keyword+"%",
            "%"+keyword+"%"
        )
        cur.execute(sql, param)
        hasil = cur.fetchall()
        cur.close()
        return hasil
