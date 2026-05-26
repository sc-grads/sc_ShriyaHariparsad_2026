INSERT INTO tblEmployee
VALUES (1, 'Dylan', 'A', 'Word', 'HN513777D', '19920914', 'Customer Relations'),
(2,'Jossef', 'H', 'Wright', 'TX593671R', '19711224', 'Litigation')

select * from tblEmployee
where [EmployeeLastName] >= 'Word'

select * from tblEmployee
where [EmployeeLastName] like '%W%'

select * from tblEmployee
where [EmployeeLastName] like '_W%' --_means one character 

Select * from tblEmployee
where [EmployeeLastName] like '[r-t]%'

Select * from tblEmployee
where [EmployeeLastName] like '[^rst]%'

-- % = 0-infinity characters
-- _ = 1 character
-- [A-G] = In the range A-G.
-- [AGQ] = A, G or Q.
-- [^AGQ] = NOT A, G or Q.

select * from tblEmployee
where EmployeeLastName like '[%]%'





