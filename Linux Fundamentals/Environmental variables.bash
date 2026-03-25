[root@Sambe2025001 ~]$printenv
SHELL=/bin/bash
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
TERM=xterm-256color
USER=root
SHLVL=1
PS1=[\u@\h \W]$
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
MAIL=/var/mail/root
_=/usr/bin/printenv
[root@Sambe2025001 ~]$printenv | less
[root@Sambe2025001 ~]$printenv USER
root
[root@Sambe2025001 ~]$echo $USER
root
[root@Sambe2025001 ~]$date
Wed Mar 25 18:34:37 SAST 2026
[root@Sambe2025001 ~]$export TZ="US/Pacific"
[root@Sambe2025001 ~]$date
Wed Mar 25 16:35:54  2026
[root@Sambe2025001 ~]$unset TZ
[root@Sambe2025001 ~]$date
Wed Mar 25 18:36:14 SAST 2026
[root@Sambe2025001 ~]$man date
[root@Sambe2025001 ~]$
