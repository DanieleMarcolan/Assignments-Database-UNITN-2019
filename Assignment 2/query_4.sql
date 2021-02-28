SELECT B1.name
FROM "Beers" B1
WHERE B1.manf IN (SELECT B2.manf
	          FROM "Beers" B2
		  GROUP BY B2.manf
		  HAVING COUNT(*)=1);