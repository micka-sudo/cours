-- Les commentaires sur SQL sont notifiés par deux tirets
-- Elles sont extremement utiles lors d'une ecriture d'une requete SQL, 
-- Et qui dans le temps va permettre d'avoir un suivi fonctionnel de celle ci.
-- donc c'est une (très bonne) partique de commenter son code SQL

SELECT TOP (1000) [Nom] --prends moi les 1000 premieres lignes
      ,[prenom]
  FROM [BDD].[dbo].[Nom]
  where nom ='peter'-- ou le nom ou peter


--on peut aussi le commenter via le petit bouton dans le menu SSMS


-- Concernant les crochets 

-- Prenons le cas ou je cree une colonne dans une table avec un espace 

create table Table_crochet ([colonne avec un espace] varchar(20))

-- Si on fait un select sur la colonne avec un espace que se passe t il ? 

select colonne avec un espace  from table_crochet

-- Ca ne marche pas il faut rajouter un crochet 

select [colonne avec un espace]  from table_crochet

-- on peut l'utiliser aussi pour les termes, reserves par SQL

create table Reservation_SQL (table varchar (20))

-- J'ai une erreur de syntaxe lors de la creation de la table, mais si je mets le crochet 

create table Reservation_SQL ([table] varchar (20))

-- la ca fonctionne, et que donne le select

select table from Reservation_SQL

-- la aussi le crochet est necessaire