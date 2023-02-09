/*
    Weather Observation Station 14
*/

select truncate(max(lat_n),4) from station where lat_n < 137.2345;