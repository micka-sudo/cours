-- Que donne le select ? 
select * from Nom
-- Partons d'un UPDATE simple 
update  Nom set prenom ='Richard' where nom ='Peter'
-- que donne le SELECT ? 
select * from nom
-- La valeur a été changé a Richard
-- Mais comment faire si je veux faire un UPDATE sur deux colonnes en meme temps ? 
-- si je veux changer par exemple le nom de richard par coeur de lion
-- Soit faire deux UPDATE 
update  Nom set prenom ='Richard' where nom ='Peter'
update  Nom set nom ='Coeur de lion' where nom ='Peter'
-- On peut le faire aussi en mettant une virgule apres la valeur
update  Nom set nom ='Coeur de lion', prenom='richard' where nom ='Peter'
-- Que donne le select ? 
select * from Nom