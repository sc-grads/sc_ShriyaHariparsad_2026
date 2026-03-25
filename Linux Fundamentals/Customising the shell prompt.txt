[persist root@Sambe2025001 /]$echo $PS1
[persist \u@\h \w]$
[persist root@Sambe2025001 /]$PS1="\u@\h \$ "
root@Sambe2025001 $ PS1="<\t \u@\h \w>\$"
<17:37:15 root@Sambe2025001 />$ cd /var/log
<17:37:51 root@Sambe2025001 /var/log>$ PS1="\d \t \h \W>\$ "
Wed Mar 25 17:38:30 Sambe2025001 log>$ cd
Wed Mar 25 17:38:57 Sambe2025001 ~>$ vi .bash_profile
Wed Mar 25 17:39:37 Sambe2025001 ~>$
