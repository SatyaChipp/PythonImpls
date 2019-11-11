Given a list of oring cities and a list of destination cities
find if there is a route from origin to destination
if origin cities and destination cities have common divisors, then there is a route from origin to destination
sample
origin [1, 2,3] 
dest [4, 5, 6]
Origin  divisors     dest  divisors
1         1            4      1,2 4
2        1, 2          5       1, 5
3       1, 3           6       1, 2, 3, 6
if we have a threshold of 2
then eliminate cities <2 
now city 3 and dest city 6 have common divisors ..hence there is a route from 3 to 6!!
Now get cracking!
