DECLARE @param varchar(1000) = '127';

DECLARE @sql nvarchar(max) =
    N'
    SELECT *
    FROM [dbo].[tblTransaction] AS T WHERE T.EmployeeNumber = ' + @param;

EXECUTE (@sql);


DECLARE @param varchar(1000) = '127';

EXECUTE sys.sp_executesql
    @statement = 
        N'
        SELECT *
        FROM [dbo].[tblTransaction] AS T
    WHERE T.EmployeeNumber = @EmployeeNumber;',
    @params = N'@EmployeeNumber varchar(1000)',
    @EmployeeNumber = @param;
