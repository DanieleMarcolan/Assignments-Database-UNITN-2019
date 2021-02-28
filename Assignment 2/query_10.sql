SELECT DISTINCT F1.drinker
FROM "Frequents" F1
EXCEPT
SELECT TT.drinker
FROM (SELECT*
      FROM "Frequents" F2
      EXCEPT
      SELECT L.drinker, S.bar
      FROM "Likes" L NATURAL JOIN "Sells" S) as TT;