# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:08:43 2020

@author: Shadow
"""

import json
import mysql.connector

# Connection python et Mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123Camel"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE games")




"""mycursor.execute("SHOW DATABASE games")
for x in mycursor:
  print(x)"""

"""with open("C:/Users/Shadow/Desktop/thron/season1.json") as json_data:
    data_dict = json.load(json_data)
    print(data_dict)"""



