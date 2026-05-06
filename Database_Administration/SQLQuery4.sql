SELECT * FROM Person.Address

SELECT addressid,city,modifieddate from [Person].[Address]

SELECT city,addressid,modifieddate from [Person].[Address]

SELECT TOP 10 * FROM [Person].[Address]


SELECT * FROM Person.Address WHERE postalcode = '98011'

SELECT * FROM Person.Address WHERE postalcode != '98011'

SELECT * FROM Person.Address WHERE postalcode <> '98011'

SELECT count(*) FROM Person.Address WHERE postalcode <> '98011'

SELECT * FROM Person.Address WHERE ModifiedDate >= '2013-11-08 00:00:00.000'

SELECT * FROM [Person].[Person] WHERE FirstName LIKE 'MAT%'

SELECT * FROM [HumanResources].[EmployeePayHistory]

SELECT max(rate) As PayRate FROM [HumanResources].[EmployeePayHistory]

SELECT min(rate) As [Min Pay Rate] FROM [HumanResources].[EmployeePayHistory]

SELECT * FROM [Production].[ProductCostHistory] WHERE StartDate = '2013-05-30 00:00:00'

SELECT * FROM [Production].[ProductCostHistory] WHERE StartDate = '2013-05-30 00:00:00' AND StandardCost >=200.00

SELECT * FROM [Production].[ProductCostHistory] WHERE (StartDate = '2013-05-30 00:00:00' AND StandardCost >=200.00) OR ProductId>=800

SELECT * FROM [Production].[ProductCostHistory] WHERE ProductId in (802,803,820,900)

SELECT * FROM [Production].[ProductCostHistory] WHERE EndDate is Null

SELECT * FROM [Production].[ProductCostHistory] WHERE EndDate is not Null


SELECT * FROM [HumanResources].[EmployeePayHistory] order by rate 

SELECT * FROM [HumanResources].[EmployeePayHistory] order by rate ASC

SELECT * FROM [HumanResources].[EmployeePayHistory] order by rate DESC

SELECT * FROM [HumanResources].[EmployeePayHistory] WHERE ModifiedDate >= '2010-06-30 00:00:00.000' order by ModifiedDate DESC

SELECT * FROM [HumanResources].[EmployeePayHistory] WHERE Year(ModifiedDate) >= '2014' order by ModifiedDate DESC


SELECT count(*) FROM Person.Address WHERE PostalCode = '98011'

SELECT * FROM Person.Address WHERE PostalCode = '98011'

SELECT count(*) FROM Person.Address WHERE PostalCode = '98225'

SELECT count(*), PostalCode FROM Person.Address group by PostalCode order by postalcode desc

SELECT count(*), City FROM Person.Address group by City order by City desc


SELECT * FROM [Production].[Product]

SELECT count(1) As CountOfProductColor FROM [Production].[Product] WHERE color = 'yellow' group by Color


