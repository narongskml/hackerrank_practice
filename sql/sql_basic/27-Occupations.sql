SELECT 
MIN(CASE WHEN R.Occupation='Doctor'    THEN R.Name ELSE NULL END),
MIN(CASE WHEN R.Occupation='Professor' THEN R.Name ELSE NULL END),
MIN(CASE WHEN R.Occupation='Singer'    THEN R.Name ELSE NULL END),
MIN(CASE WHEN R.Occupation='Actor'     THEN R.Name ELSE NULL END)
FROM
(
    SELECT ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Name) AS row_num, Name,  Occupation
    FROM OCCUPATIONS
) as R
GROUP BY R.row_num