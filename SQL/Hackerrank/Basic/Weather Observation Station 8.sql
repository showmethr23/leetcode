/*
    Weather Observation Station 8
*/

select distinct(CITY) from STATION where left(CITY, 1) in ('a', 'e', 'i', 'o', 'u') and right(CITY, 1) in ('a', 'e', 'i', 'o', 'u');