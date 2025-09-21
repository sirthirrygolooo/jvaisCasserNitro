import subprocess

script_path = "flafla.py"

subprocess.Popen(["python", script_path], shell=True)


def menu():
    print("1 - Démarrer le script")
    print("2 - Voir le nombre de liens récupérés")
    print("3 - Supprimer les liens")
    print("4 - Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        subprocess.Popen(["python", script_path], shell=True)
    elif choice == "2":
        print("Nombre de liens récupérés : " + str(counter()))
        menu()
    elif choice == "3":
        os.remove("liens.txt")
        menu()
    elif choice == "4":
        exit()
    else:
        print("Veuillez entrer un choix valide !")
        menu()