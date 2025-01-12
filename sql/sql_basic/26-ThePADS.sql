
SELECT CONCAT(Name,'(', LEFT(Occupation,1) ,')' )
FROM OCCUPATIONS
ORDER BY Name;

SELECT  CONCAT('There are a total of ', CONVERT(varchar(10),COUNT(*)), ' ', LOWER(Occupation),'s.')
FROM OCCUPATIONS
GROUP BY LOWER(Occupation)
ORDER BY COUNT(*);