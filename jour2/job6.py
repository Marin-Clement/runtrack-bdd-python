import mysql.connector

# connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Minecraft01@",
    database="LaPlateforme"
)

# create a cursor
cursor = cnx.cursor()

# execute a query
query = "SELECT SUM(capacite) as capacite_totale FROM salles"
cursor.execute(query)


# get the results
result = cursor.fetchone()
capacite_totale = result[0]
print("La somme des capacités des salles est de {}".format(capacite_totale))

# close the cursor
cursor.close()
cnx.close()