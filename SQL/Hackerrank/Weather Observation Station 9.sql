/*
    Weather Observation Station 9
*/

select distinct city from station where left(city, 1) not in ('a','e','i','o','u');