CREATE DATABASE BDD
--- Comment renommer la BDD ??
ALTER DATABASE BDD  Modify Name = Peterpan ;  
--- Comment Supprimer la BDD ? 
DROP DATABASE BDD
-- Revenir a l'etat initial
CREATE DATABASE BDD

Use [BDD]  
-- Utilisation de ma BDD les crochets sont facultatifs

--- Pour mettre des commentaires sur SQL il faut mettre deux tirets 

-- Si je veux utiliser la BDD Master ?
use [master]
-- On repart sur la BDD actuelle 
Use [BDD]
-- Creation d'une table simple avec deux colonnes
create table ma_table4 (nom varchar(200),prenom varchar(200))
--- je veux renommer ma table :
-- en TSQL : 
sp_rename 'ma_table2','ma_table8'
-- Je veux supprimer ma table : 
-- en TSQL : 
drop table ma_table4