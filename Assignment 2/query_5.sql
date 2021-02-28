SELECT DISTINCT S1.beer
FROM "Sells" S1
WHERE ROUND (S1.price::numeric, 2) = (SELECT ROUND (MAX(S2.price::numeric), 2)
	                              FROM "Sells" S2);  