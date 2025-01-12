/*
Consider P1(a,c) and P2(b,d)  to be two points on a 2D plane 
where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) 
and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) 
in STATION.
    a = min LAT_N
    b = max LAT_N
    c = min LONG_W
    d = max LONG_W

    P1(min LAT_N, min LONG_W)
    P2(max LAT_N, max LONG_W)
    d(P1,P2) = SQRT( POW(minLAT_N-maxLAT_N, 2) + POW( max LONGW-minLONGW, 2))
Query the Euclidean Distance between points P1 and P2 and format your answer to display  decimal digits.
*/


SELECT 
    CONVERT(numeric(12,4),ROUND(SQRT( POWER(MIN(LAT_N)-MAX(LAT_N),2)+ POWER(MAX(LONG_W)-MIN(LONG_W),2)),4))
FROM STATION;