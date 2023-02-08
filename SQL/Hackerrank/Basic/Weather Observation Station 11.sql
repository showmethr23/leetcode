/*
    Weather Observation Station 11
*/

select distinct city from station where left(city, 1) not in ('a','e','i','o','u') or right(lower(city), 1) not in ('a','e','i','o','u');