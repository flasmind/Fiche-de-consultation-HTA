

print("FICHE DE CONSULTATION PATIENT\n")
def info_patient(nom,prenom,age,tension_s,tension_d):
    print(f"-----VOS INFORMATIONS-----")
    print(f"NOM:{nom}")
    print(f"PRENOM:{prenom}")
    print(f"AGE:{age}")
    print(f"TENSION ARTERIELLE:{tension_s}/{tension_d}")
    print(f"-----------BY BOGUI--------------")  
nom=input("Entrer le nom du patient:")
prenom=input("Entrer le prénom du patient:")
age=int(input("Entrer l'âge du patient:"))
tension_s=int(input("Entrer la tension systolique du patient:"))
tension_d=int(input("Entrer tension diastolique du patient:"))
info_patient(nom,prenom,age,tension_s,tension_d)
if tension_s==12 and tension_d==8:
    print(f"\nObservation:Votre tension artérielle est normale:RAS")
elif tension_s > 12 and tension_s < 20 and tension_d > 8 and tension_d < 13 :
    print(f"\nObservation:Votre tension artérielle est élevée.\nConduite:Vous devez consulter un Cardiologue.")
elif tension_s >=20 and tension_s <=26 and tension_d >=10 and tension_d <=15:
    print(f"\nObservation:Votre tension artérielle est trop élevée.\nConduite:Transfert d'urgence en Cardiologie.")    
elif tension_s < 12 and tension_d <= 8:
    print(f"\nObservation:Votre tension artérielle est basse.\nConduite:Veuillez consulter un Diététicien.")
else:
    print(f"\nObservation:Votre tension artérielle est trop élevée.\nConduite:Transfert d'urgence en Cardiologie.")      