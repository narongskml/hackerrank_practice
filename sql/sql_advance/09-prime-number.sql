/*
Write a query to print all prime numbers less than or equal to .
 Print your result on a single line, and use the ampersand () 
 character as your separator (instead of a space).

For example, the output for all prime numbers  would be:
*/


    DECLARE @i INT = 1
    DECLARE @j INT = 2
    DECLARE @COUNT INT
    DECLARE @PRIME1000 AS VARCHAR(1000)
    BEGIN
    WHILE @j <= 1000
        BEGIN
            SET @COUNT = 0
            WHILE @i <= @j
                BEGIN
                    BEGIN
                        IF((@j % @i) = 0)
                            SET @COUNT += 1
                    END
                    SET @i += 1
                END
            BEGIN
                IF (@COUNT = 2)
                    SET @PRIME1000 = CONCAT_WS('&',@PRIME1000,@j)
            END
            SET @i = 1
            SET @j += 1
        END
    END;
    PRINT @PRIME1000