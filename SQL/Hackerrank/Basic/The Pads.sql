/*
    The Pads
*/

select concat(name, "(", left(occupation, 1), ")") from occupations order by name;
select concat("There are a total of ", count(occupation), " ", lower(occupation)) from occupations group by occupation order by count(occupation), occupation;