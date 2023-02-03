/*
    Weather Observation Station 3
*/

select distinct city from station where mod(id,2) = 0;