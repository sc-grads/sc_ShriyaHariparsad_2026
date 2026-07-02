IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'TimesheetDB')
BEGIN
    CREATE DATABASE TimesheetDB;
END;
GO

USE TimesheetDB;
GO

-- 1. STAGING TABLE 
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Staging_Table') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Staging_Table (
        StagingID INT IDENTITY(1,1) NOT NULL,
        [Date] NVARCHAR(50),
        [D_of_Week] NVARCHAR(50),
        [Client] NVARCHAR(250),
        [Description] NVARCHAR(MAX),
        [Billable_or_NonBillable] NVARCHAR(50),
        [Comments] NVARCHAR(MAX),
        [Total_Hours] NVARCHAR(50),
        [Start_Time] NVARCHAR(50),
        [End_Time] NVARCHAR(50),
        [SourceFileName] NVARCHAR(500), 
        [LoadTimestamp] DATETIME DEFAULT GETDATE(),
        CONSTRAINT PK_Staging_Table PRIMARY KEY NONCLUSTERED (StagingID)
    );
    
    CREATE CLUSTERED INDEX IX_Staging_Chronological 
    ON dbo.Staging_Table (SourceFileName ASC, [Date] ASC, [Start_Time] ASC);
END;

-- 2. AUDIT LOG TABLE
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Audit_Log') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Audit_Log (
        AuditID INT IDENTITY(1,1) PRIMARY KEY,
        SourceFile NVARCHAR(250) NOT NULL, 
        LoadDate DATETIME DEFAULT GETDATE(),
        UserAccount NVARCHAR(100) NULL,
        RowsProcessed INT,
        InsertsProcessed INT NULL,
        UpdatesProcessed INT NULL,
        DeletesProcessed INT NULL,
        SkippedRows INT NULL,
        Status NVARCHAR(50),
        ErrorMessage NVARCHAR(MAX) NULL
    );
END;

-- 3. EMPLOYEE TABLE 
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Employee') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Employee (
        EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
        EmployeeFirstName NVARCHAR(250) NOT NULL,
        EmployeeLastName NVARCHAR(250) NOT NULL,
        CONSTRAINT UC_Employee_FullName UNIQUE (EmployeeFirstName, EmployeeLastName)
    );
END;

-- 4. CLIENT TABLE
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Client') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Client (
        ClientID INT IDENTITY(1,1) PRIMARY KEY,
        ClientName NVARCHAR(250) UNIQUE NOT NULL
    );
END;

-- 5. FINAL TIMESHEET TABLE
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Timesheet') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Timesheet (
        TimesheetID INT IDENTITY(1,1) NOT NULL,
        EmployeeID INT NOT NULL FOREIGN KEY REFERENCES dbo.Employee(EmployeeID),
        ClientID INT NOT NULL FOREIGN KEY REFERENCES dbo.Client(ClientID), 
        WorkDate DATE NOT NULL,
        DayOfWeek NVARCHAR(50),
        [Description] NVARCHAR(MAX), 
        BillableOrNonBillable NVARCHAR(50) NOT NULL, 
        Comments NVARCHAR(MAX),
        HoursWorked TIME(0),
        StartTime TIME(0),
        EndTime TIME(0),
        CONSTRAINT PK_Timesheet PRIMARY KEY NONCLUSTERED (TimesheetID)
    );
    
    CREATE CLUSTERED INDEX IX_Timesheet_Chronological 
    ON dbo.Timesheet (EmployeeID ASC, WorkDate ASC, StartTime ASC);
END;

-- 6. LEAVE TRACKING TABLE (Updated: BatchID & TotalHours removed)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Leave') AND type in (N'U'))
BEGIN
    CREATE TABLE dbo.Leave (
        LeaveID INT IDENTITY(1,1) PRIMARY KEY,
        EmployeeID INT NOT NULL FOREIGN KEY REFERENCES dbo.Employee(EmployeeID),
        LeaveDate DATE NOT NULL,
        LeaveType NVARCHAR(150) NOT NULL                  
    );
END;
