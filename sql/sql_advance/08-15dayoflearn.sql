/*
Julia conducted a  days of learning SQL contest. 
The start date of the contest was March 01, 2016 and the end date was March 15, 2016.

Write a query to print total number of unique hackers who made at least  submission each day 
(starting on the first day of the contest), 
and find the hacker_id and name of the hacker who made maximum number of submissions each day. 
If more than one such hacker has a maximum number of submissions,
 print the lowest hacker_id. 
The query should print this information for each day of the contest,
 sorted by the date.

*/

        select b.submission_date,min(b.hacker_id) mn 
         from 
        (
        select a.submission_date, a.hacker_id, a.cnt, 
            rank() over ( partition by a.submission_date order by a.submission_date asc, a.cnt desc)  rn 
            from 
           (
            select s.submission_date,shacker_id,count(distinct s.submission_id) cnt
            from submissions s
              group by s.submission_date,s. hacker_id
            ) as a
        ) as b 
        where b.rn=1 
         group by b.submission_date
         order by b.submission_date



         /*
Working Platform:- MySQL
*/
SELECT SUBMISSION_DATE,
(SELECT COUNT(DISTINCT HACKER_ID)  
 FROM SUBMISSIONS S2  
 WHERE S2.SUBMISSION_DATE = S1.SUBMISSION_DATE AND    
(SELECT COUNT(DISTINCT S3.SUBMISSION_DATE) 
 FROM SUBMISSIONS S3 WHERE S3.HACKER_ID = S2.HACKER_ID AND S3.SUBMISSION_DATE < S1.SUBMISSION_DATE) = DATEDIFF(S1.SUBMISSION_DATE , '2016-03-01')),
(SELECT HACKER_ID FROM SUBMISSIONS S2 WHERE S2.SUBMISSION_DATE = S1.SUBMISSION_DATE 
GROUP BY HACKER_ID ORDER BY COUNT(SUBMISSION_ID) DESC, HACKER_ID LIMIT 1) AS TMP,
(SELECT NAME FROM HACKERS WHERE HACKER_ID = TMP)
FROM
(SELECT DISTINCT SUBMISSION_DATE FROM SUBMISSIONS) S1
GROUP BY SUBMISSION_DATE;




--MySQL
SELECT submission_date,

      (SELECT COUNT(DISTINCT hacker_id)
       FROM Submissions AS s2
       WHERE s2.submission_date = s1.submission_date
       AND (SELECT COUNT(DISTINCT submission_date)
            FROM Submissions AS s3
            WHERE s3.hacker_id = s2.hacker_id 
            AND s3.submission_date < s2.submission_date
            ) = DATEDIFF(s1.submission_date,'2016-03-01')),
                                  
      (SELECT hacker_id
       FROM Submissions AS s4
       WHERE s4.submission_date = s1.submission_date
       GROUP BY hacker_id
       ORDER BY COUNT(submission_id) DESC, hacker_id 
       LIMIT 1) AS h_id,
        
      (SELECT name
       FROM Hackers
       WHERE hacker_id = h_id)
        
FROM (SELECT DISTINCT submission_date FROM Submissions) AS s1;


--MS SQL Server
WITH ConsistentHackers AS (
	SELECT s.submission_date,
               s.hacker_id
	FROM Submissions s
      	WHERE s.submission_date = '2016-03-01'
      	UNION ALL
      	SELECT DATEADD(dd,1,ch.submission_date),
               s.hacker_id
      	FROM Submissions s
      	JOIN ConsistentHackers ch
      	    ON s.hacker_id = ch.hacker_id
      	    AND s.submission_date = DATEADD(dd,1,ch.submission_date))
,
ConsistencyCounts AS (
	SELECT ch.submission_date,
               COUNT(DISTINCT ch.hacker_id) AS ConsistentHackers
	FROM ConsistentHackers ch
      	GROUP BY ch.submission_date)
,
SubmissionsSummary AS (
	SELECT s.submission_date,
               s.hacker_id,
               ROW_NUMBER() OVER (PARTITION BY s.submission_date 
				  ORDER BY COUNT(*) DESC, s.hacker_id
             ) AS ranking
    	FROM Submissions s
    	GROUP BY s.submission_date, s.hacker_id)

SELECT
    ss.submission_date,
    cc.ConsistentHackers,
    h.hacker_id,
    h.name
FROM SubmissionsSummary ss
JOIN ConsistencyCounts cc
    ON ss.submission_date = cc.submission_date
    AND ss.ranking = 1
JOIN Hackers h
    ON ss.hacker_id = h.hacker_id
ORDER BY ss.submission_date;




WITH join_tables_sub_hacker AS (     
      -- Joining both tables : submission and hacker 
    SELECT
        hacker_id,
        hacker_name,
        submission_date,
        submission_id
    FROM
        (
            SELECT
                h.hacker_id       AS hacker_id,
                h.name            AS hacker_name,
                s.submission_date AS submission_date,
                s.submission_id   AS submission_id
            FROM
                     submissions s
                JOIN hackers h ON s.hacker_id = h.hacker_id
            ORDER BY
                s.submission_date,
                h.name
        )
), day_number AS (
   -- daily participated day number 
    SELECT
        hacker_id,
        hacker_name,
        submission_date,
        submission_id,
        DENSE_RANK()
        OVER(
            ORDER BY
                submission_date
        ) AS day_num
    FROM
        join_tables_sub_hacker
), each_day_participated AS (
   -- daily participated day number 
    SELECT
        hacker_id,
        hacker_name,
        submission_date,
        submission_id,
        DENSE_RANK()
        OVER(PARTITION BY hacker_id, hacker_name
             ORDER BY
                 submission_date
        ) AS each_day
    FROM
        join_tables_sub_hacker
), get_cnt_of_hker_each_day AS (
    SELECT
        sdt                 AS submission_date,
        COUNT(DISTINCT hid) AS no_of_count_participated
    FROM
        (
            SELECT
                a.hacker_id       AS hid,
                a.hacker_name     AS hname,
                b.submission_date AS sdt
            FROM
                     day_number a
                JOIN each_day_participated b ON a.hacker_id = b.hacker_id
                                                AND a.hacker_name = b.hacker_name
                                                AND a.submission_date = b.submission_date
                                                AND a.day_num = b.each_day
            ORDER BY
                a.submission_date,
                a.hacker_name
        )
    GROUP BY
        sdt
    ORDER BY
        sdt
), get_submission_count AS (
    SELECT
        submission_date,
        MIN(hacker_id) AS mhcker,
        COUNT(*)       AS each_count
    FROM
        submissions
    GROUP BY
        submission_date,
        hacker_id
    ORDER BY
        submission_date,
        hacker_id
), get_each_date_max_sub_count AS (
    SELECT
        submission_date,
        MAX(each_count) AS mxcnt
    FROM
        get_submission_count
    GROUP BY
        submission_date
    ORDER BY
        submission_date
), final_data_min_hacker AS (
    SELECT
        sdt,
        hk
    FROM
        (
            SELECT
                sdt,
                hk,
                ecnt,
                mcnt,
                ROW_NUMBER()
                OVER(PARTITION BY sdt
                     ORDER BY
                         hk ASC
                ) AS rn
            FROM
                (
                    SELECT
                        a.submission_date AS sdt,
                        a.mhcker          AS hk,
                        a.each_count      AS ecnt,
                        b.mxcnt           AS mcnt
                    FROM
                             get_submission_count a
                        JOIN get_each_date_max_sub_count b ON a.each_count = b.mxcnt
                                                              AND a.submission_date = b.submission_date
                    ORDER BY
                        a.submission_date,
                        a.mhcker ASC
                )
        )
    WHERE
        rn = 1
)
SELECT
    a.submission_date,
    a.no_of_count_participated,
    f.hk,
    h.name
FROM
         get_cnt_of_hker_each_day a
    JOIN final_data_min_hacker f ON a.submission_date = f.sdt
    JOIN hackers               h ON f.hk = h.hacker_id
ORDER BY
    a.submission_date;





    WITH rcte (
    hacker_id,
    submission_date
) AS (
    SELECT
        hacker_id,
        submission_date
    FROM
        submissions
    WHERE
        trunc(submission_date) = (
            SELECT
                MIN(trunc(submission_date))
            FROM
                submissions
        )
    UNION ALL
    SELECT
        r.hacker_id,
        trunc(e.submission_date)
    FROM
             rcte r
        JOIN submissions e ON e.hacker_id = r.hacker_id
                              AND trunc(e.submission_date) = trunc(r.submission_date + 1)
), get_count_participated AS (
    SELECT
        submission_date,
        COUNT(DISTINCT hacker_id) AS no_of_count_participated
    FROM
        rcte
    GROUP BY
        submission_date
    ORDER BY
        submission_date
), get_submission_count AS (
    SELECT
        submission_date,
        MIN(hacker_id) AS mhcker,
        COUNT(*)       AS each_count
    FROM
        submissions
    GROUP BY
        submission_date,
        hacker_id
    ORDER BY
        submission_date,
        hacker_id
), get_each_date_max_sub_count AS (
    SELECT
        submission_date,
        MAX(each_count) AS mxcnt
    FROM
        get_submission_count
    GROUP BY
        submission_date
    ORDER BY
        submission_date
), final_data_min_hacker AS (
    SELECT
        sdt,
        hk
    FROM
        (
            SELECT
                sdt,
                hk,
                ecnt,
                mcnt,
                ROW_NUMBER()
                OVER(PARTITION BY sdt
                     ORDER BY
                         hk ASC
                ) AS rn
            FROM
                (
                    SELECT
                        a.submission_date AS sdt,
                        a.mhcker          AS hk,
                        a.each_count      AS ecnt,
                        b.mxcnt           AS mcnt
                    FROM
                             get_submission_count a
                        JOIN get_each_date_max_sub_count b ON a.each_count = b.mxcnt
                                                              AND a.submission_date = b.submission_date
                    ORDER BY
                        a.submission_date,
                        a.mhcker ASC
                )
        )
    WHERE
        rn = 1
)
SELECT
    a.submission_date,
    a.no_of_count_participated,
    f.hk,
    h.name
FROM
         get_count_participated a
    JOIN final_data_min_hacker f ON a.submission_date = f.sdt
    JOIN hackers               h ON f.hk = h.hacker_id
ORDER BY
    a.submission_date;