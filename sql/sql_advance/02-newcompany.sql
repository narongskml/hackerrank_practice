SELECT DISTINCT
C.company_code, C.founder
, (SELECT COUNT(DISTINCT lead_manager_code ) FROM Lead_Manager as L WHERE L.company_code =C.company_code  ) as lm
, (SELECT COUNT(DISTINCT senior_manager_code ) FROM Senior_Manager  as S WHERE S.company_code =C.company_code  ) as sm
, (SELECT COUNT(DISTINCT manager_code ) FROM Manager  M WHERE M.company_code =C.company_code  ) as  mg
, (SELECT COUNT(DISTINCT employee_code ) FROM Employee as E WHERE E.company_code =C.company_code  ) as em
FROM COMPANY as C
GROUP BY C.company_code, C.founder
ORDER BY C.company_code;