import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python"
)

mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1. Lihat User")
    print("2. Tambah User")
    print("3. Ubah User")
    print("4. Hapus User")
    print("5. Keluar")
    print("")

    p = int(input("Pilih Menu: "))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresults = mycursor.fetchall()
        print("=====================================")
        print("(id, nama, email. no hp)")
        for x in myresults:
            print(x)
    elif(p == 2):
        nama = input("Nama: ")
        email = input("Email: ")
        nohp = input("No HP: ")
        sql = "INSERT INTO user (nama, email, nohp) VALUES (%s, %s, %s)"
        val = (nama, email, nohp)
        mycursor.execute(sql, val)
        koneksi.commit()
        print("Berhasil Menambahkan User")
    elif(p == 3):
        id = input("ID USER: ")
        mycursor.execute("SELECT * FROM user where id = "+id+" LIMIT 1")
        myresults = mycursor.fetchall()
        user = None
        for x in myresults:
            user = x
        if(user != None):
            nama = input("Nama ("+user[1]+") :")or user[1]
            email = input("Email ("+user[2]+") :")or user[2]
            nohp = input("No HP ("+user[3]+") :")or user[3]
            sql = "UPDATE user SET nama = %s, email = %s, nohp = %s WHERE id = %s"
            val = (nama, email, nohp, id)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount,"Berhasil Mengubah User")
        else:
            print("User Tidak Ditemukan")
    elif(p == 4):
        id = input("ID USER: ")
        mycursor.execute("SELECT * FROM user where id = "+id+" LIMIT 1")
        myresults = mycursor.fetchall()
        user = None
        for x in myresults:
            user = x
        if(user != None):
            print("MENGHAPUS DATA : ", user)
            sql = "DELETE FROM user WHERE id ="+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount,"Berhasil Menghapus User")
        else:
            print("User Tidak Ditemukan")
    elif(p == 5):
        lanjut = False