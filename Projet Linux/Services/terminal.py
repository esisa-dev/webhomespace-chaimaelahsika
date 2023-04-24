import subprocess as sb

def create_passwdInTerminal(username,mdp):
    
    # Exécuter la commande passwd avec le nom d'utilisateur fourni
    cmd = "echo '{0}\n{1}\n{1}' | sudo passwd {0}".format(username, mdp)
    sb.call(cmd, shell=True)
    print("Mot de passe défini avec succès")

def create_userInTerminal(username):
    try :
        # Vérifier si le nom d'utilisateur est unique
        existing_usernames = sb.check_output("cut -d: -f1 /etc/passwd", shell=True).decode().split("\n")
        if username in existing_usernames:
            print("Le nom d'utilisateur existe déjà")
            return False
        else:
            # Exécuter la commande adduser avec le nom d'utilisateur fourni
            cmd = "sudo adduser " + username
            sb.call(cmd, shell=True)
            print("Compte utilisateur créé avec succès")
            return True
    except ValueError as err:
        print("On peut pas creer cet Utilisateur ",err)

