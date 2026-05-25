SELECT TOP 10
   sys.fn_PhysLocFormatter(%%physloc%%) PageId,
   *
FROM [CorruptionTest].[dbo].[mssqltips_corrupt]
GO

DBCC TRACEON (3604) ;
GO
DBCC PAGE ('CorruptionTest', 1, 354, 3);
GO

USE master;
GO  
ALTER DATABASE [CorruptionTest] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO
DBCC WRITEPAGE ('CorruptionTest', 1, 354, 2151, 4, 0xCFD5B605, 1)
GO
ALTER DATABASE [CorruptionTest] SET MULTI_USER;
GO


