SELECT DISTINCT S.bar
FROM "Sells" S
WHERE S.beer IN (SELECT L.beer
		 FROM "Likes" L
		 WHERE L.drinker='Joe'); 