select Email
from Person
group by Email
having count(Email) > 1

SELECT name,population,area
FROM World
WHERE population>25000000
OR area>3000000

SELECT *
FROM cinema
WHERE mod(id, 2) = 1 AND description != 'boring'
ORDER BY rating DESC

UPDATE salary
SET sex = char( ASCII(sex) ^ ASCII('m') ^ ASCII('f') )

SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonId=Address.PersonId