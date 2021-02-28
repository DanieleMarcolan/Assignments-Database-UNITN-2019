SELECT DISTINCT B.name, B.manf
FROM "Likes" L, "Beers" B
WHERE L.drinker='Fred' AND L.beer=B.name;