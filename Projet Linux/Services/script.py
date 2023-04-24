import os
import pathlib
import subprocess

directory = 'D:/S6/Administration Sous Linux/Projet Linux'

def lister_files(directory):
    directory = 'D:/S6/Administration Sous Linux/Projet Linux'
    for filename in os.listdir(directory):
        f = os.path.join(filename)
        for entry in os.scandir(directory):
            if os.path.isfile(f):
                print(f)
                if entry.is_file() :
                    print(entry.path)
# def fonction():
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.txt'):
#                 print(os.path.join(root, file))


def authentification(username,password):
    if username == "mon_nom_utilisateur" and password == "mon_mot_de_passe":
        print("Authentification réussie!")
    else:
        print("Informations d'identification incorrectes.")

