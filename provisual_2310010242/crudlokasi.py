import mysql.connector

class crudlokasi:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dapintambang'
        )

    # 🔹 SIMPAN
    def simpanLokasi(self, id_lokasi, nama_lokasi, koordinat, luas_area):
        cur = self.koneksi.cursor()
        cur.execute(
            "INSERT INTO lokasi_tambang (id_lokasi, nama_lokasi, koordinat, luas_area) VALUES (%s, %s, %s, %s)",
            (id_lokasi, nama_lokasi, koordinat, luas_area)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 UBAH
    def ubahLokasi(self, id_lokasi, nama_lokasi, koordinat, luas_area):
        cur = self.koneksi.cursor()
        cur.execute(
            "UPDATE lokasi_tambang SET nama_lokasi=%s, koordinat=%s, luas_area=%s WHERE id_lokasi=%s",
            (nama_lokasi, koordinat, luas_area, id_lokasi)
        )
        self.koneksi.commit()
        cur.close()

    # 🔹 HAPUS
    def hapusLokasi(self, id_lokasi):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM lokasi_tambang WHERE id_lokasi=%s", (id_lokasi,))
        self.koneksi.commit()
        cur.close()

    # 🔹 TAMPIL
    def tampilLokasi(self):
        cur = self.koneksi.cursor()
        cur.execute("""
            SELECT id_lokasi, nama_lokasi, koordinat, luas_area
            FROM lokasi_tambang
            ORDER BY id_lokasi ASC
        """)
        hasil = cur.fetchall()
        cur.close()
        return hasil

    def cariLokasi(self, keyword):
        cur = self.koneksi.cursor()
        sql = """
            SELECT id_lokasi, nama_lokasi, koordinat, luas_area
            FROM lokasi_tambang
            WHERE id_lokasi LIKE %s
            OR nama_lokasi LIKE %s
            OR koordinat LIKE %s
            OR luas_area LIKE %s
        """
        param = ("%"+keyword+"%", "%"+keyword+"%", "%"+keyword+"%", "%"+keyword+"%")
        cur.execute(sql, param)
        hasil = cur.fetchall()
        cur.close()
        return hasil


