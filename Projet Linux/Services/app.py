import hashlib
import logging
import os
import subprocess as sb
import zipfile

from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import random
import string
import getpass

from flask_login import login_user

app = Flask(__name__)
app.secret_key = "1234"

def generate_key(login):
    return hashlib.md5(str(login).encode('utf-8')).hexdigest()

logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("L\'opération a été effectuée avec succès.")

@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/login', methods=['POST'])
def login():
    logging.info('L\'utilisateur s\'est connecté.')
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Vérification des informations d'utilisateur ici
    if username == 'username' and password == 'password':
        login_user()
        logging.info(f"L'utilisateur {username} s'est connecté.")
        return "Connecté avec succès"
    else:
        return "Identifiants invalides"
def create_User():
    username = request.form['username']
    existing_usernames = subprocess.check_output("cut -d: -f1 /etc/passwd", shell=True).decode().split("\n")
    if username in existing_usernames:
        response = {'message': 'Le nom d\'utilisateur existe déjà'}
        status_code = 400
    else:
        password = create_password()
        cmd = "sudo adduser --gecos '' --disabled-password " + username
        subprocess.call(cmd, shell=True)
        cmd = "echo '{0}\n{1}\n{1}' | sudo passwd {0}".format(username, password)
        subprocess.call(cmd, shell=True)

        response = {'message': 'Compte utilisateur créé avec succès', 'username': username, 'password': password}
        status_code = 201

    return jsonify(response), status_code
@app.route('/logout')
def logOut():
    return render_template("logOut.html")

def create_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

@app.route('/download')
def DownloadHomeDirectory(user):
    logging.info(f'L\'utilisateur {user} a téléchargé le fichier {filename}.')
    user = request.args.get('user')
    filename = request.args.get('filename')
    logging.info(f"L'utilisateur {user} a téléchargé le fichier {filename}.")
    directory = ""
    return send_from_directory(directory, filename, as_attachment=True)
@app.route('/find')
def FindHomeDirectory():
    user = request.args.get('user')
    directory = ""
    home_dir = os.path.join(directory, user)
    
    if not os.path.exists(home_dir):
        return f"Le répertoire home de l'utilisateur {user} n'existe pas."
    
    return f"Le répertoire home de l'utilisateur {user} est : {home_dir}"    
@app.route('/DownloadZip')
def DownloadFormatZip():
    user = request.args.get('user')
    filename = request.args.get('filename')
    directory = ""
    file_path = os.path.join(directory, user, filename)
    
    if not os.path.exists(file_path):
        return f"Le fichier {filename} pour l'utilisateur {user} n'existe pas."
    
    zip_filename = f"{filename}.zip"
    zip_path = os.path.join(directory, user, zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        zip_file.write(file_path, filename)
    
    return send_from_directory(directory, zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

# Optionnel
def EntrerDonneees():
    username = "????"
    password = "?????"
    input_username = input("Entrez votre nom d'utilisateur: ")
    input_password = getpass.getpass("Entrez votre mot de passe: ")
    if input_username == username and input_password == password:
        print("Vous êtes connecté avec succès !")
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")





