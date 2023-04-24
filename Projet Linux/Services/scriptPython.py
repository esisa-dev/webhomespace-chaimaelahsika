import os
import pandas as pd
import zipfile
def ListerHome():
# Récupérer le chemin du répertoire home de l'utilisateur
    home_path = os.path.expanduser("~")
    files_and_dirs = os.listdir(home_path)
    df = pd.DataFrame(columns=["Nom", "Type"])
    for item in files_and_dirs:
        item_path = os.path.join(home_path, item)
        if os.path.isfile(item_path):
            df = df.append({"Nom": item, "Type": "Fichier"}, ignore_index=True)
        elif os.path.isdir(item_path):
            df = df.append({"Nom": item, "Type": "Répertoire"}, ignore_index=True)
    print(df)

def search_files(home_path, keyword):
    """
    Recherche de fichiers par nom et extension dans le répertoire home de l'utilisateur.
    """
    matching_files = []
    for dirpath, dirnames, filenames in os.walk(home_path):
        for filename in filenames:
            if keyword in filename:
                matching_files.append(os.path.join(dirpath, filename))
    return matching_files

def zip_home_directory(home_path, zip_filename):
    """
    Crée un fichier zip contenant le répertoire home de l'utilisateur.
    """
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for dirpath, dirnames, filenames in os.walk(home_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                arcname = os.path.relpath(file_path, home_path)
                zipf.write(file_path, arcname=arcname)
def PathToUserHome():
    home_path = os.path.expanduser("~")
    keyword = input("Entrez un mot-clé pour rechercher des fichiers dans le répertoire home : ")
    matching_files = search_files(home_path, keyword)
    if matching_files:
        print("Fichiers correspondants trouvés :")
        for file_path in matching_files:
            print(file_path)
    else:
        print("Aucun fichier correspondant trouvé.")
    zip_filename = input("Entrez le nom du fichier zip à créer pour le répertoire home : ")
    zip_home_directory(home_path, zip_filename)
    print(f"Le répertoire home a été compressé dans le fichier zip : {zip_filename}")

def get_directory_stats(path):
    """
    Obtient les statistiques du répertoire, y compris le nombre de fichiers, le nombre de répertoires
    et l'espace occupé en octets.
    """
    total_files = 0
    total_dirs = 0
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            total_files += 1
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

        for dirname in dirnames:
            total_dirs += 1

    return total_files, total_dirs, total_size
home_path = os.path.expanduser("~")
total_files, total_dirs, total_size = get_directory_stats(home_path)
print("Statistiques du répertoire home :")
print(f"Nombre de fichiers : {total_files}")
print(f"Nombre de répertoires : {total_dirs}")
print(f"Taille totale occupée : {total_size} octets")