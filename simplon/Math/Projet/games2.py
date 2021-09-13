import json
import mysql.connector

# Connection python et Mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE games")
mycursor.execute("""use games""")
# creation ma table saison 1.

mycursor.execute("""
CREATE TABLE IF NOT EXISTS saison1 (
    id int(5) NOT NULL AUTO_INCREMENT,
    name varchar(50) DEFAULT NULL,
    age INTEGER DEFAULT NULL,
    PRIMARY KEY(id)
);
""")

"""mycursor.execute("SHOW DATABASE")
for x in mycursor:
  print(x)"""

with open("C:/Users/Shadow/Desktop/thron/season1.json") as json_data:
    data_dict = json.load(json_data)
    print(data_dict)