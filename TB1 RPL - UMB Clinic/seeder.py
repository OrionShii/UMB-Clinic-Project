import mysql.connector
from faker import Faker
import random

# Konfigurasi koneksi ke basis data MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'webrpl',
}

# Fungsi untuk mengisi data fake ke tabel "user"
def seed_users(num_users):
    fake = Faker()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        for _ in range(num_users):
            username = fake.user_name()
            password = fake.password()
            insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))

        connection.commit()
        print("{} data user berhasil di-generate dan di-insert.".format(num_users))
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Fungsi untuk mengisi data fake ke tabel "dokter"
def seed_dokters(num_dokters):
    fake = Faker()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        for _ in range(num_dokters):
            name = fake.name()
            spesialis = random.choice(["Umum", "Bedah", "Gigi", "Mata", "THT", "Anak", "Jantung", "Kulit", "Psikiater", "Ortopedi", "Obgyn", "Gizi", "Saraf", "Rehabilitasi", "Urologi", "Pulmonologi", "Kejiwaan", "RadiologiCT"])
            jenis_kelamin = random.choice(['Laki-laki', 'Perempuan'])
            status = random.choice(['available', 'unavailable'])
            pasien_id = random.randint(1, num_users)  # Gunakan num_users dari seeding user

            insert_query = "INSERT INTO dokter (name, spesialis, jenis_kelamin, status, pasien_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (name, spesialis, jenis_kelamin, status, pasien_id))

        connection.commit()
        print("{} data dokter berhasil di-generate dan di-insert.".format(num_dokters))
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    num_users = 10  # Jumlah data user yang ingin di-generate
    num_dokters = 5  # Jumlah data dokter yang ingin di-generate

    seed_users(num_users)
    seed_dokters(num_dokters)