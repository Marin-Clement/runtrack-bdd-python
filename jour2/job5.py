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
query = "SELECT SUM(superficie) as superficie_totale FROM etage"
cursor.execute(query)


# get the results
result = cursor.fetchone()
superficie_totale = result[0]
print("La superficie de La Plateforme est de {} m2".format(superficie_totale))

# close the cursor
cursor.close()
cnx.close()