SELECT * FROM [HumanResources].[EmployeePayHistory]
WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM [HumanResources].[EmployeePayHistory] WHERE Rate > 60)

SELECT * FROM [Employee]

SELECT * FROM [HumanResources].[EmployeePayHistory]
WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM [HumanResources].[EmployeePayHistory] WHERE Rate = 39.06)

SELECT * FROM [Production].[Product]
WHERE ProductID in (SELECT ProductID FROM [Production].[ProductInventory] WHERE Quantity > 300)
