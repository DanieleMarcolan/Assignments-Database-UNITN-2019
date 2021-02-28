SELECT DISTINCT L.drinker, S.beer
FROM "Frequents" F, "Likes" L, "Sells" S
WHERE S.beer=L.beer AND L.drinker=F.drinker;