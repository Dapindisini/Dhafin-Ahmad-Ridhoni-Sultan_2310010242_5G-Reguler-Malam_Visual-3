import mysql.connector

class crudpekerja:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dapintambang'
        )

    def simpanPekerja(self, id, nm, jbt, sts):
        cur = self.koneksi.cursor()
        cur.execute(
            "INSERT INTO pekerja (id_pekerja, nama, jabatan, status) VALUES (%s, %s, %s, %s)",
            (id, nm, jbt, sts)
        )
        self.koneksi.commit()
        cur.close()

    def ubahPekerja(self, id, nm, jbt, sts):
        cur = self.koneksi.cursor()
        cur.execute(
            "UPDATE pekerja SET nama=%s, jabatan=%s, status=%s WHERE id_pekerja=%s",
            (nm, jbt, sts, id)
        )
        self.koneksi.commit()
        cur.close()

    def hapusPekerja(self, id):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM pekerja WHERE id_pekerja=%s", (id,))
        self.koneksi.commit()
        cur.close()

    def tampilPekerja(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("SELECT * FROM pekerja")
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil
