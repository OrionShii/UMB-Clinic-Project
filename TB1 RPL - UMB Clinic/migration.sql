-- Membuat basis data "webrpl" jika belum ada
CREATE DATABASE IF NOT EXISTS webrpl;

-- Menggunakan basis data "webrpl"
USE webrpl;

-- Membuat tabel "user"
CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Membuat tabel "dokter"
CREATE TABLE IF NOT EXISTS dokter (
    dokter_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    spesialis VARCHAR(255) NOT NULL,
    jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
    status ENUM('available', 'sibuk') DEFAULT 'available',
    pasien_id INT,
    FOREIGN KEY (pasien_id) REFERENCES user(user_id)
);

-- Membuat tabel "resep_dokter"
CREATE TABLE IF NOT EXISTS resep_dokter (
    resep_id INT AUTO_INCREMENT PRIMARY KEY,
    dokter_id INT NOT NULL,
    FOREIGN KEY (dokter_id) REFERENCES dokter(dokter_id),
    resep_text TEXT NOT NULL
);

-- Membuat tabel "invoice"
CREATE TABLE IF NOT EXISTS invoice (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    total_harga DECIMAL(10, 2) NOT NULL
);

-- Membuat tabel "contact"
CREATE TABLE IF NOT EXISTS contact (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    mobile VARCHAR(20) NOT NULL,
    pesan TEXT NOT NULL
);