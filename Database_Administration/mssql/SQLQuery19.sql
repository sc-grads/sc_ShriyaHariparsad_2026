create database dbtest;

alter database dbtest set MIXED_PAGE_ALLOCATION on

create table heaptable1(c1 int, c2 varchar(8000))

insert heaptable1 values(1,REPLICATE('a',1000))

select ht1.c1,ht1.c2, p.file_id,p.page_id, is_mixed_page_allocation

From heaptable1 as ht1 CROSS APPLY sys.fn_PhysLocCracker(%%physloc%%) as p inner join sys.dm_db_database_page_allocations(db_id(),object_id('dbo.heaptable1'),null,null,'detailed') as dddpa

on p.file_id=dddpa.allocated_page_file_id and

p.page_id=dddpa.allocated_page_page_id

dbcc traceon(3604,-1)

dbcc page(dbtest,1,1,3)