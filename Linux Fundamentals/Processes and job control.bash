[root@Sambe2025001 ~]$ ps
    PID TTY          TIME CMD
    517 pts/0    00:00:00 bash
    536 pts/0    00:00:00 ps
[root@Sambe2025001 ~]$ ps -p 517
    PID TTY          TIME CMD
    517 pts/0    00:00:00 bash
[root@Sambe2025001 ~]$ ps -f
UID          PID    PPID  C STIME TTY          TIME CMD
root         517     511  0 05:33 pts/0    00:00:00 -bash
root         546     517 99 05:35 pts/0    00:00:00 ps -f
[root@Sambe2025001 ~]$ ps -e
    PID TTY          TIME CMD
      1 ?        00:00:01 systemd
      2 ?        00:00:00 init-systemd(Ub
      6 ?        00:00:00 init
     55 ?        00:00:00 systemd-journal
    101 ?        00:00:00 systemd-udevd
    112 ?        00:00:00 systemd-resolve
    119 ?        00:00:00 systemd-timesyn
    190 ?        00:00:00 cron
    191 ?        00:00:00 dbus-daemon
    204 ?        00:00:00 systemd-logind
    206 ?        00:00:00 wsl-pro-service
    223 ?        00:00:00 rsyslogd
    228 hvc0     00:00:00 agetty
    231 tty1     00:00:00 agetty
    237 ?        00:00:00 unattended-upgr
    333 pts/1    00:00:00 login
    378 ?        00:00:00 systemd
    381 ?        00:00:00 (sd-pam)
    405 pts/1    00:00:00 bash
    510 ?        00:00:00 SessionLeader
    511 ?        00:00:00 Relay(517)
    517 pts/0    00:00:00 bash
    547 pts/0    00:00:00 ps
[root@Sambe2025001 ~]$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 05:32 ?        00:00:01 /sbin/init
root           2       1  0 05:32 ?        00:00:00 /init
root           6       2  0 05:32 ?        00:00:00 plan9 --control-socket 7 --log-level 4 --server-fd 8
root          55       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-journald
root         101       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-udevd
systemd+     112       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-resolved
systemd+     119       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-timesyncd
root         190       1  0 05:32 ?        00:00:00 /usr/sbin/cron -f -P
message+     191       1  0 05:32 ?        00:00:00 @dbus-daemon --system --address=systemd: --nofork --
root         204       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-logind
root         206       1  0 05:32 ?        00:00:00 /usr/libexec/wsl-pro-service -vv
syslog       223       1  0 05:32 ?        00:00:00 /usr/sbin/rsyslogd -n -iNONE
root         228       1  0 05:32 hvc0     00:00:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115
root         231       1  0 05:32 tty1     00:00:00 /sbin/agetty -o -p -- \u --noclear - linux
root         237       1  0 05:32 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/unat
root         333       2  0 05:32 pts/1    00:00:00 /bin/login -f
root         378       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd --user
root         381     378  0 05:32 ?        00:00:00 (sd-pam)
root         405     333  0 05:32 pts/1    00:00:00 -bash
root         510       2  0 05:33 ?        00:00:00 /init
root         511     510  0 05:33 ?        00:00:00 /init
root         517     511  0 05:33 pts/0    00:00:00 -bash
root         548     517  0 05:35 pts/0    00:00:00 ps -ef
[root@Sambe2025001 ~]$ les
Command 'les' not found, did you mean:
  command 'less' from deb less (590-2ubuntu2.1)
  command 'lvs' from deb lvm2 (2.03.16-3ubuntu3.1)
  command 'yes' from deb coreutils (9.4-2ubuntu2)
  command 'ls' from deb coreutils (9.4-2ubuntu2)
  command 'lex' from deb flex (2.6.4-8.2)
Try: apt install <deb name>
[root@Sambe2025001 ~]$ less
Missing filename ("less --help" for help)
[root@Sambe2025001 ~]$ ps -ef |less
[root@Sambe2025001 ~]$ ps -fu root
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 05:32 ?        00:00:01 /sbin/init
root           2       1  0 05:32 ?        00:00:00 /init
root           6       2  0 05:32 ?        00:00:00 plan9 --control-socket 7 --log-level 4 --server-fd 8
root          55       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-journald
root         101       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-udevd
root         190       1  0 05:32 ?        00:00:00 /usr/sbin/cron -f -P
root         204       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-logind
root         206       1  0 05:32 ?        00:00:00 /usr/libexec/wsl-pro-service -vv
root         228       1  0 05:32 hvc0     00:00:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115
root         231       1  0 05:32 tty1     00:00:00 /sbin/agetty -o -p -- \u --noclear - linux
root         237       1  0 05:32 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/unat
root         333       2  0 05:32 pts/1    00:00:00 /bin/login -f
root         378       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd --user
root         381     378  0 05:32 ?        00:00:00 (sd-pam)
root         405     333  0 05:32 pts/1    00:00:00 -bash
root         510       2  0 05:33 ?        00:00:00 /init
root         511     510  0 05:33 ?        00:00:00 /init
root         517     511  0 05:33 pts/0    00:00:00 -bash
root         577     517  0 05:38 pts/0    00:00:00 ps -fu root
[root@Sambe2025001 ~]$ ps --forest
    PID TTY          TIME CMD
    517 pts/0    00:00:00 bash
    580 pts/0    00:00:00  \_ ps
[root@Sambe2025001 ~]$ ps -ef --forest
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 05:32 ?        00:00:01 /sbin/init
root           2       1  0 05:32 ?        00:00:00 /init
root           6       2  0 05:32 ?        00:00:00  \_ plan9 --control-socket 7 --log-level 4 --server-
root         333       2  0 05:32 pts/1    00:00:00  \_ /bin/login -f
root         405     333  0 05:32 pts/1    00:00:00  |   \_ -bash
root         510       2  0 05:33 ?        00:00:00  \_ /init
root         511     510  0 05:33 ?        00:00:00      \_ /init
root         517     511  0 05:33 pts/0    00:00:00          \_ -bash
root         585     517  0 05:39 pts/0    00:00:00              \_ ps -ef --forest
root          55       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-journald
root         101       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-udevd
systemd+     112       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-resolved
systemd+     119       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-timesyncd
root         190       1  0 05:32 ?        00:00:00 /usr/sbin/cron -f -P
message+     191       1  0 05:32 ?        00:00:00 @dbus-daemon --system --address=systemd: --nofork --
root         204       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd-logind
root         206       1  0 05:32 ?        00:00:00 /usr/libexec/wsl-pro-service -vv
syslog       223       1  0 05:32 ?        00:00:00 /usr/sbin/rsyslogd -n -iNONE
root         228       1  0 05:32 hvc0     00:00:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115
root         231       1  0 05:32 tty1     00:00:00 /sbin/agetty -o -p -- \u --noclear - linux
root         237       1  0 05:32 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/unat
root         378       1  0 05:32 ?        00:00:00 /usr/lib/systemd/systemd --user
root         381     378  0 05:32 ?        00:00:00  \_ (sd-pam)
[root@Sambe2025001 ~]$
