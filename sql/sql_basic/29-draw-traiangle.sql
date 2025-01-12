DECLARE @i int
SET @i=20;

WHILE (@i>0)
    BEGIN
        SELECT RTRIM(REPLICATE('* ', @i));
        SET @i=@i-1;
    END



/*
* 
* * 
* * * 
* * * * 
* * * * *

*/
DECLARE @i int
SET @i=1;

WHILE (@i<=20)
    BEGIN
        SELECT RTRIM(REPLICATE('* ', @i));
        SET @i=@i+1;
    END