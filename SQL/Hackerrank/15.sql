/*
    Weather Observation Station 10
*/

select distinct city from station where right(lower(city), 1) not in ('a','e','i','o','u');