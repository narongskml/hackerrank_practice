SELECT SUM(C.POPULATION)
FROM CITY C
JOIN COUNTRY T ON C.CountryCode=T.Code
WHERE T.CONTINENT='Asia';