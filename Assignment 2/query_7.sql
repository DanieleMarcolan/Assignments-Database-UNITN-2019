SELECT DISTINCT ROUND (S1.price::numeric, 2)
FROM "Sells" S1
WHERE S1.price IN (SELECT S2.price
	           FROM "Sells" S2
		   WHERE S2.price=S1.price);