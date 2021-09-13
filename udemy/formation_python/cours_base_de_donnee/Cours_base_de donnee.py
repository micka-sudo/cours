import sqlite3

# creation base de donnée
conn = sqlite3.connect("database.db")

# Creation tableau
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")
# insertion de donnée


# envoi les info a la base de donnée
conn.commit()

#ferme le fichier
conn.close()
