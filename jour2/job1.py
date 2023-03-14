import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Minecraft01@",
    database="LaPlateforme"
)


# Create a cursor
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM etudiants"
cursor.execute(query)

# Get the results
etudiants = cursor.fetchall()

# Print the results
for etudiant in etudiants:
    print(etudiant)

# Close the cursor
cursor.close()
cnx.close()
