SELECT S1.bar
FROM "Sells" S1
WHERE S1.beer='Miller' AND ROUND (S1.price::numeric, 2) = (SELECT ROUND (S2.price::numeric, 2)
						           FROM "Sells" S2
		 	        		           WHERE S2.beer='Bud' AND S1.bar=S2.bar);