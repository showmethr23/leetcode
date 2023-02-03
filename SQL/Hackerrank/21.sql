/*
    Contest Leaderboard
*/


select t.hacker_id, h.name, sum(t.score) total
from hackers h
join(select hacker_id, max(score) score
    from submissions
    group by hacker_id, challenge_id) t on h.hacker_id = t.hacker_id
group by t.hacker_id, h.name
having total != 0
order by total desc, t.hacker_id asc;