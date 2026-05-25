DBCC CHECKDB ('AdventureWorks2025')

DBCC CHECKDB    ('AdventureWorks2025') with no_infomsgs

alter database AdventureWorks2025 set single_user with rollback immediate
go
dbcc checkdb ('AdventureWorks2025',REPAIR_ALLOW_DATA_LOSS)
GO
alter database AdventureWorks2025 set MULTI_user with rollback immediate
GO
