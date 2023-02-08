/*
    Weather Observation Station 6
*/

select Distinct city from station where left(city, 1) in ('A','E','I','O','U');