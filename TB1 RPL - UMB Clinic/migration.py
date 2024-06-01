import mysql.connector

# Konfigurasi koneksi ke database MySQL
db_config = {
    "host": "localhost",
    "user": "root",  # Ganti dengan username Anda
    "password": "",  # Ganti dengan password Anda
}

# Membuat koneksi ke database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    

    # Membaca file SQL migrasi
    with open("migration.sql", "r") as sql_file:
        sql_script = sql_file.read()

    # Menjalankan perintah SQL
    cursor.execute(sql_script, multi=True)


    print("Migrasi berhasil dijalankan.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Menutup koneksi
    if conn.is_connected():
        cursor.close()
        conn.close()