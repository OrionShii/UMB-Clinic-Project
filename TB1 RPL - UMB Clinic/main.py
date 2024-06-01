from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with your own secret key
# Konfigurasi koneksi ke database MySQL
db_config = {
    "host": "localhost",
    "user": "root",  # Ganti dengan username Anda
    "password": "",  # Ganti dengan password Anda
    "database": "webrpl"
}

users = {'user1': 'password1', 'user2': 'password2'}

class Dokter:
    def __init__(self, name, spesialis, jenis_kelamin, images=''):
        self.name = name
        self.spesialis = spesialis
        self.jenis_kelamin = jenis_kelamin
        self.available = 'avail'
        self.pasien = ''
        self.image = images
    
dokters = [
        Dokter('Erza Scarlet ', 'Kulit', 'Wanita', 'images/cewe1.jpg'),
        Dokter('Asuna Hariyati', 'Kelamin', 'wanita', 'images/cewe2.jpg'),
        Dokter('Rin Okumura', 'Rambut', 'Pria', 'images/cowo1.jpg'),
        Dokter('Amar Saputra', 'Umum', 'Pria', 'images/cowo2.jpg'),
        Dokter('Mio Fidela', 'THT', 'Wanita', 'images/cewe3.jpg'),
    ]


@app.route('/')
def hello_world():
    return login()

@app.route('/dashboard')
def dashboard():
    if isLogin():
        return render_template('dashboard.html', dokters=dokters)
    else:
        return redirect(url_for('login'))

# Fungsi untuk melakukan autentikasi pengguna
def authenticate_user(username, password):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Cek apakah pengguna dengan username dan password tertentu ada dalam database
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session['logged_in'] = True
            session['username'] = username
            return True
        else:
            return False
    except mysql.connector.Error as error:
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            return redirect(url_for('dashboard'))
        else:
            return "Invalid login credentials. Please try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def isLogin():
    return 'logged_in' in session and session['logged_in']

# Fungsi untuk menambahkan pengguna ke database
def register_user(username, password):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Cek apakah username sudah ada dalam database
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return "Username already exists. Please choose a different username."

        # Insert pengguna baru ke dalam tabel "user"
        insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password))
        connection.commit()

        return "Registration successful! You can now <a href='/login'>log in</a>."
    except mysql.connector.Error as error:
        return "Error: {}".format(error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users:
        return "Username already exists. Please choose a different username."

    users[username] = password
    result_message = register_user(username, password)

    return render_template("prompt.html", value=result_message)



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    pesan = request.form.get('pesan')
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO contact (fname, lname, email, mobile, pesan) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (fname, lname, email, mobile, pesan))
        connection.commit()
        
        value="Terima Kasih Telah Menghubungi, Kami Akan Segera Membalas Anda"
        return render_template("prompt.html", value=value)

    except mysql.connector.Error as error:
        return "Error: {}".format(error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return render_template('contact.html')

@app.route('/booking',methods=['POST','GET'])
def booking():
    if request.method == 'GET':
        return render_template('booking.html', dokters=dokters)
    d = request.form.get('dokter')
    p = request.form.get('user')
    for dokter in dokters:
        if d == dokter.name:
            dokter.available="sibuk"
            dokter.pasien = p
    return redirect(url_for('dashboard'))


@app.route('/booking_selesai',methods=['POST'])
def booking_selesai():
    d = request.form.get('dokter')
    for dokter in dokters:
        if d == dokter.name:
            dokter.available="avail"
            dokter.pasien = ""
    return redirect(url_for('dashboard'))
