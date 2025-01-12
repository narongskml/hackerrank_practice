/*
Write a query to print the respective hacker_id and name of hackers who achieved full scores 
for more than one challenge. 
Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

*/

SELECT hackers.hacker_id, hackers.name 
FROM hackers
JOIN submissions ON submissions.hacker_id = hackers.hacker_id
JOIN challenges ON challenges.challenge_id = submissions.challenge_id
JOIN difficulty ON difficulty.difficulty_level = challenges.difficulty_level
WHERE difficulty.score = submissions.score
GROUP BY hackers.name, hackers.hacker_id
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, hackers.hacker_id;