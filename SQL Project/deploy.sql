-- Check and create the database first
IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = 'ProjectDB1'
)
BEGIN
    CREATE DATABASE ProjectDB1;
END
GO

-- Switch to the database
USE ProjectDB1;
GO
 
-- Create Employees table if it doesn't exist
IF NOT EXISTS (
    SELECT *
    FROM sys.tables
    WHERE name = 'Employees'
)
BEGIN
    CREATE TABLE Employees
    (
        EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Email VARCHAR(100),
        DateCreated DATETIME DEFAULT GETDATE()
    );
END
GO
 
-- Insert sample data if table is empty
IF NOT EXISTS (
    SELECT 1
    FROM Employees
)
BEGIN
    INSERT INTO Employees
    (
        FirstName,
        LastName,
        Email
    )
    VALUES
    ('John', 'Smith', 'john.smith@email.com'),
    ('Sarah', 'Jones', 'sarah.jones@email.com'),
    ('David', 'Brown', 'david.brown@email.com');
END
GO
 
-- Verify deployment
SELECT * FROM Employees;
GO


