# C'est un fichier de configuration de etc/shadow 
# avec les permissions 640 et un nom d'utilisateur root 
# Puisque on est sous Windows il va afficher le message d'erreurde else
import os

# Définir les permissions recommandées et le propriétaire
droits = "640"
user = "root"

# Vérifier que le fichier existe
if os.path.exists("/etc/shadow"):
    # Définir les permissions et le propriétaire
    os.chmod("/etc/shadow", int(droits, 8))
    os.chown("/etc/shadow", -1, os.getgrnam(user).gr_gid)
    print("Les droits ont bien été configurés dans /etc/shadow ")
    print("Le USER de a bien été configuré dans /etc/shadow ")
else:
    print("Le fichier /etc/shadow n'existe pas.")
