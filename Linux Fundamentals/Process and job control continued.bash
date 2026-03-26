[root@Sambe2025001 ~]$ pstree
systemd─┬─2*[agetty]
        ├─cron
        ├─dbus-daemon
        ├─init-systemd(Ub─┬─SessionLeader───Relay(288)───bash─+++
        │                 ├─init───{init}
        │                 ├─login───bash
        │                 └─{init-systemd(Ub}
        ├─rsyslogd───3*[{rsyslogd}]
        ├─systemd───(sd-pam)
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-resolve
        ├─systemd-timesyn───{systemd-timesyn}
        ├─systemd-udevd
        └─unattended-upgr───{unattended-upgr}
[root@Sambe2025001 ~]$ top
top - 05:46:14 up 13 min,  1 user,  load average: 0.08, 0.10,
Tasks:  22 total,   1 running,  21 sleeping,   0 stopped,   0
%Cpu(s):  0.1 us,  0.2 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,
MiB Mem :   7606.2 total,   7057.5 free,    529.9 used,    169
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   7076

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM























[root@Sambe2025001 ~]$ htop
Command 'htop' not found, but can be installed with:
snap install htop  # version 3.4.1, or
apt  install htop  # version 3.2.2-2
See 'snap info htop' for additional versions.
[root@Sambe2025001 ~]$
