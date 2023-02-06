/*
    Weather Observation Station 12
*/

select distinct city from station where left(city, 1) not in ('a','e','i','o','u') and right(lower(city), 1) not in ('a','e','i','o','u');