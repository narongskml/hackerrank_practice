SELECT  CEILING(AVG(
                    CONVERT(decimal(12,2),Salary)
                    -CONVERT(decimal(12,2), REPLACE(CONVERT(varchar(20), Salary),'0','')))
               ) as v

FROM EMPLOYEES;