USE master
GO
DROP DATABASE IF EXISTS [CorruptionTest]
GO
CREATE DATABASE [CorruptionTest]
GO
ALTER DATABASE [CorruptionTest] SET RECOVERY FULL;
GO
ALTER DATABASE [CorruptionTest] SET PAGE_VERIFY CHECKSUM  
GO
CREATE TABLE [CorruptionTest].[dbo].[mssqltips_online]
(increment INT, randomGUID uniqueidentifier, randomValue INT, BigCol CHAR(2000) DEFAULT 'a',
INDEX CIX_MSSQLTips_increment1 UNIQUE CLUSTERED (increment))
GO
CREATE TABLE [CorruptionTest].[dbo].[mssqltips_corrupt]
(increment INT, randomGUID uniqueidentifier, randomValue INT, BigCol CHAR(2000) DEFAULT 'a',
INDEX CIX_MSSQLTips_increment1 UNIQUE CLUSTERED (increment))
GO

SET NOCOUNT ON;
DECLARE @counter INT = 1;
BEGIN TRAN
   WHILE @counter <= 250000
   BEGIN
      INSERT INTO CorruptionTest.dbo.mssqltips_online (increment, randomGUID, randomValue) 
      VALUES (@counter, NEWID(), ABS(CHECKSUM(NewId())) % 140000000)

      INSERT INTO CorruptionTest.dbo.mssqltips_corrupt (increment, randomGUID, randomValue)
      VALUES (@counter, NEWID(), ABS(CHECKSUM(NewId())) % 140000000)

      SET @counter += 1
   END;
COMMIT TRAN;
GO
DBCC CHECKDB('CorruptionTest') WITH NO_INFOMSGS
GO
BACKUP DATABASE [CorruptionTest] TO DISK = 'C:\SQL_BACKUPS\CorruptionTest_Full.BAK' WITH COMPRESSION
GO	

select count(1) from [dbo].[mssqltips_corrupt]
select count(1) from [dbo].[mssqltips_online]