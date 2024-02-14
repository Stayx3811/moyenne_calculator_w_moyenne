def calcul_moyenne_generale(moyennes):
    if len(moyennes) == 0:
        return 0
    return sum(moyennes) / len(moyennes)

def main():
    moyennes = []
    while True:
        try:
            moyenne = float(input("Entrez la moyenne du cours (ou entrez '0' pour terminer) : "))
            if moyenne == 0:
                break
            moyennes.append(moyenne)
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    moyenne_generale = calcul_moyenne_generale(moyennes)
    print("La moyenne générale est :", moyenne_generale)

if __name__ == "__main__":
    main()
