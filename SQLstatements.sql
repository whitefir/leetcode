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

SELECT a.Name AS 'Employee'
FROM Employee AS a,
     Employee AS b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary

SELECT Name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.Id=Orders.CustomerId
WHERE Orders.CustomerId IS null

DELETE p1
FROM Person as p1, Person as p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id

select w1.Id
from Weather w1, Weather w2
where DATEDIFF(w1.RecordDate,w2.RecordDate)=1 and w1.Temperature>w2.Temperature

SELECT class 
FROM courses 
GROUP BY class
HAVING COUNT(distinct student)>=5

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
