import mysql.connector

# se connecter à la base de données
mydb = mysql.connector.connect(
  host="..",
  user="..",
  password="..",
  database=".."
)
#supprimer la table existante
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS customers")

# créer une table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# insérer des données dans la table
i=int(input("Donnez le nombre de personnes qui participent\n"))
x=0
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
nom=str(input("Nom de la personne : "))
adresse=str(input("Adresse de l'utilisateur : "))
val = (nom, adresse)
mycursor.execute(sql, val)
mydb.commit()
while x!=i-1:
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    nom=str(input("Nom de la personne :"))
    adresse=str(input("Adresse de l'utilisateur"))
    val = (nom, adresse)
    mycursor.execute(sql, val)
    mydb.commit()
    x+=1
print(mycursor.rowcount, "record inserted.")

# récupérer les données de la table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for row in myresult:
    print("nom:", row[0])
    print("adresse:", row[1])
