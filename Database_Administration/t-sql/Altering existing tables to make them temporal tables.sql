alter table [dbo].[tblEmployee]
add
ValidFrom datetime2(2) GENERATED ALWAYS AS ROW START CONSTRAINT def_ValidFrom DEFAULT SYSUTCDATETIME()
	, ValidTo datetime2(2) GENERATED ALWAYS AS ROW END CONSTRAINT def_ValidTo DEFAULT
																  CONVERT(datetime2(2), '9999-12-31 23:59:59')
    , PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
alter table dbo.tblEmployee
--set (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.tblEmployeeHistory2))