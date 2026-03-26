[root@Sambe2025001 ~]$ crontab -l
no crontab for root
[root@Sambe2025001 ~]$ vi my-cron
[root@Sambe2025001 ~]$ cat my-cron
#Run every Monday at 07:00
0 7 * * 1 /opt/sales/bin/weekly-report


[root@Sambe2025001 ~]$ crontab my-cron
[root@Sambe2025001 ~]$ crontab -l
#Run every Monday at 07:00
0 7 * * 1 /opt/sales/bin/weekly-report


[root@Sambe2025001 ~]$ echo $EDITOR

[root@Sambe2025001 ~]$ EDITOR=vi
[root@Sambe2025001 ~]$ crontab -e

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 1
No modification made
[root@Sambe2025001 ~]$ crontab -r
[root@Sambe2025001 ~]$ crontab -l
no crontab for root
[root@Sambe2025001 ~]$
