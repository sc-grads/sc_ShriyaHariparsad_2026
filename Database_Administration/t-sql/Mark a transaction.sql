begin transaction MyTransaction WITH MARK

select * 
from [dbo].[tblEmployee]

commit transaction MyTransaction