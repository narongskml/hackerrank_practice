/* Manhattan distance In a plane with p1 at (x1, y1) and p2 at (x2, y2),
 it is |x1 - x2| + |y1 - y2|.*/

SELECT CONVERT(numeric(12,4),ROUND(ABS((MIN(LAT_N) - MAX(LAT_N))) 
                + ABS((MIN(LONG_W ) - MAX(LONG_W))),4) )
FROM STATION;