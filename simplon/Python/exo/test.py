
montant_dommage = ()
while montant_dommage != "o":

    montant_dommage = str(input("veuillez rentrez le montant des dommages (taper o pour sortir) : \n"))

    if montant_dommage != "o":
        if not montant_dommage.isnumeric():
            print("S.V.P saisissez un nombre compris en 150 et 5000 euro \n")
            continue
        franchise = (int(montant_dommage) * 10 // 100)
        if franchise >= 15 and franchise <= 50:
            
            print(f" la franchise sera de : {franchise} euro ")
        else:
            print(f"Le montant de la dommage doit être compris entre 150 et 5000 euro, votre dommage est de : {franchise} euro " )
    else:
        print("bye bye")
        break

  

