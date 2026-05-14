BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\AdventureWorks2025.BAK'
BACKUP DATABASE AdventureWorks2025 FILE = 'TestBackup' TO DISK = 'C:\TestBackup_TestBackup.FIL'
BACKUP DATABASE AdventureWorks2025 FILEGROUP = 'ReadOnly' TO DISK = 'C:\TestBackup_ReadOnly.FLG'

BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\SQL_BACKUPS\AdventureWorks2025_1.BAK',DISK = 'C:\SQL_BACKUPS\AdventureWorks2025_2.BAK',DISK = 'C:\SQL_BACKUPS\AdventureWorks2025_3.BAK'

BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\AdventureWorks2025.BAK' WITH PASSWORD = 'Q!W@E#R\$'
BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\AdventureWorks2025.BAK' WITH STATS
BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\AdventureWorks2025.BAK' WITH DESCRIPTION = 'Full backup for AdventureWorks2025'
BACKUP DATABASE AdventureWorks2025 TO DISK = 'C:\AdventureWorks2025.BAK' MIRROR TO DISK = 'D:\AdventureWorks2025_mirror.BAK' WITH FORMAT
