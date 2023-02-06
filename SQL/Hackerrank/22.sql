/*
    Type of Triangle
*/

select (
    case 
        when (A+B)<=C then 'Not A Triangle' 
        when (A=B AND A=C)then 'Equilateral' 
        when (A!=B AND A!=C)then 'Scalene' 
        else 'Isosceles' 
    end ) 
from triangles;