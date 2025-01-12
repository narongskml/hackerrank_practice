/* median  is value on center  

    if row number is odd 
        have 2 center
        median = avg (2 value in center)
    else
        median = value in center

    find row on center order by  value
*/

 SELECT LAT_N
    FROM 
    (
       SELECT COUNT(*) as Cnt, 
        ROW_NUMBER() OVER(ORDER BY LAT_N) as RowN
       FROM STATION
    )

/*** ORACLE */

SELECT ROUND(MEDIAN(LAT_N), 4)
FROM STATION;