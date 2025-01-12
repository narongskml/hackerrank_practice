/*Write a query to print the 
contest_id, hacker_id, name, 
 sums of total_submissions,
  total_accepted_submissions, 
  total_views, 
   total_unique_views for each contest 
   
   sorted by contest_id. 
   
   Exclude the contest from the result if all four sums are 0
*/
SELECT
    C.contest_id, C.hacker_id, C.name
    ,SUM(S.total_submissions) as total_submissions
    ,SUM(S.total_accepted_submissions) as total_accepted_submissions
    ,SUM(V.total_views) as total_view
    ,SUM(V.total_unique_views) as total_unique_view
FROM Contests as C
    JOIN Colleges as l on C.contest_id=l.contest_id
    JOIN Challenges as cl on l.college_id=cl.college_id
    LEFT JOIN (
       SELECT SS.challenge_id
        , SUM(SS.total_submissions)as total_submissions
         , SUM(SS.total_accepted_submissions)as total_accepted_submissions
        FROM Submission_Stats as SS
        GROUP BY SS.challenge_id
    ) as S ON cl.challenge_id=S.challenge_id
    LEFT JOIN (
         SELECT VV.challenge_id
        , SUM(VV.total_views)as total_views
         , SUM(VV.total_unique_views)as total_unique_views
        FROM View_Stats  as VV
        GROUP BY VV.challenge_id
    ) as V on cl.challenge_id=V.challenge_id
GROUP BY C.contest_id, C.hacker_id, C.name
HAVING SUM(S.total_submissions)+
    SUM(S.total_accepted_submissions) +
    SUM(V.total_views)+
    SUM(V.total_unique_views) >0
ORDER BY C.contest_id;