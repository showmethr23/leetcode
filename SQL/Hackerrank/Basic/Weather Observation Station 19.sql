/*
    Weather Observation Station 19
*/

set @p1 = (select round(min(lat_n), 4) from station);
set @p2 = (select round(max(lat_n), 4) from station);
set @p3 = (select round(min(long_w), 4) from station);
set @p4 = (select round(max(long_w), 4) from station);

select round(sqrt(power((@p2-@p1), 2) + power((@p4-@p3), 2)),4);