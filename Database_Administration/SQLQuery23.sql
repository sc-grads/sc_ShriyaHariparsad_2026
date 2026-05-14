BACKUP DATABASE [FileGroupsDemoDatabase] FILEGROUP = N'FG_2020',  FILEGROUP = N'FG_2019' TO  DISK = N'C:\SQL_BACKUPS\FileGroupsDemoDatabase.bak' WITH NOFORMAT, NOINIT,  NAME = N'FileGroupsDemoDatabase-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO
