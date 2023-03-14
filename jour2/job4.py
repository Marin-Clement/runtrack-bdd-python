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
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)

# get the results
for (name, capacity) in cursor:
    print("Salle: {}, Capacité: {}".format(name, capacity))

# close the cursor
cursor.close()
cnx.close()
