import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Minecraft01@",
    database="zoo"
)
# function to show all animals
def afficher_animaux():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM animal")
  myresult = mycursor.fetchall()
  for animal in myresult:
    print(animal)

# function to show all cages
def afficher_animaux_cages():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT animal.nom, cage.id FROM animal LEFT JOIN cage ON animal.cage_id = cage.id")
  myresult = mycursor.fetchall()
  for animal in myresult:
    print(animal[0] + " se trouve dans la cage " + str(animal[1]))

# function to add an animal
def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
  mycursor = mydb.cursor()
  sql = "INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
  val = (nom, race, cage_id, date_naissance, pays_origine)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "animal ajouté avec succès")

# function to delete an animal
def supprimer_animal(id):
  mycursor = mydb.cursor()
  sql = "DELETE FROM animal WHERE id = %s"
  val = (id,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "animal supprimé avec succès")

# modify animal
def modifier_animal(id, nom, race, cage_id, date_naissance, pays_origine):
  mycursor = mydb.cursor()
  sql = "UPDATE animal SET nom = %s, race = %s, cage_id = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
  val = (nom, race, cage_id, date_naissance, pays_origine, id)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "animal modifié avec succès")

# add cage
def ajouter_cage(superficie, capacite_max):
  mycursor = mydb.cursor()
  sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
  val = (superficie, capacite_max)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "cage ajoutée avec succès")

# delete cage
def supprimer_cage(id):
  mycursor = mydb.cursor()
  sql = "DELETE FROM cage WHERE id = %s"
  val = (id,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "cage supprimée avec succès")

# modify cage
def modifier_cage(id, superficie, capacite_max):
  mycursor = mydb.cursor()
  sql = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
  val = (superficie, capacite_max, id)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "cage modifiée avec succès")

while True:
  print("Que souhaitez-vous faire ?")
  print("1. Afficher les animaux présents dans le zoo")
  print("2. Afficher les animaux présents dans les cages")
  print("3. Ajouter un animal")
  print("4. Supprimer un animal")
  print("5. Modifier un animal")
  print("6. Ajouter une cage")
  print("7. Supprimer une cage")
  print("8. Modifier une cage")
  print("9. Quitter")

  choix = int(input())

  if choix == 1:
    afficher_animaux()
  elif choix == 2:
    afficher_animaux_cages()
  elif choix == 3:
    nom = input("Nom de l'animal : ")
    race = input("Race de l'animal : ")
    cage_id = int(input("Identifiant de la cage : "))
    date_naissance = input("Date de naissance de l'animal : ")
    pays_origine = input("Pays d'origine de l'animal : ")
    ajouter_animal(nom, race, cage_id, date_naissance, pays_origine)
  elif choix == 4:
    id = int(input("Identifiant de l'animal à supprimer : "))
    supprimer_animal(id)
  elif choix == 5:
    id = int(input("Identifiant de l'animal à modifier : "))
    nom = input("Nouveau nom de l'animal : ")
    race = input("Nouvelle race de l'animal : ")
    cage_id = int(input("Nouvel identifiant de la cage : "))
    date_naissance = input("Nouvelle date de naissance de l'animal : ")
    pays_origine = input("Nouveau pays d'origine de l'animal : ")
    modifier_animal(id, nom, race, cage_id, date_naissance, pays_origine)
  elif choix == 6:
    superficie = float(input("Superficie de la cage : "))
    capacite_max = int(input("Capacité maximale de la cage : "))
    ajouter_cage(superficie, capacite_max)
  elif choix == 7:
    id = int(input("Identifiant de la cage à supprimer : "))
    supprimer_cage(id)
  elif choix == 8:
    id = int(input("Identifiant de la cage à modifier : "))
    superficie = float(input("Nouvelle superficie de la cage : "))
    capacite_max = int(input("Nouvelle capacité maximale de la cage : "))
    modifier_cage(id, superficie, capacite_max)
  elif choix == 9:
    break
  else:
    print("Choix invalide")
