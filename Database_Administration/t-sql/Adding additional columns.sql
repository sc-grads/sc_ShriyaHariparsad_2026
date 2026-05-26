ALTER TABLE tblEmployee
ADD Department VARCHAR(10);

SELECT * FROM tblEmployee

INSERT INTO tblEmployee
VALUES (132,	'Dylan',	'A',	'Word',	'HN513777D',	'19920914',	'Customer Relations')

ALTER TABLE tblEmployee
DROP COLUMN Department 

Alter TABLE tblEmployee
Add Department VARCHAR(15)

Alter TABLE tblEmployee
Alter COLUMN Department VARCHAR(20)

Alter TABLE tblEmployee
Alter COLUMN Department VARCHAR(19)

SELECT LEN('Customer Relations')

INSERT INTO tblEmployee([EmployeeFirstName],[EmployeeMiddleName],
[EmployeeLastName],[EmployeeGovernmentID],[DateOfBirth],[Department],[EmployeeNumber])
VALUES ('Jossef', 'H', 'Wright', 'TX593671R', '19711224', 'Litigation',131)


