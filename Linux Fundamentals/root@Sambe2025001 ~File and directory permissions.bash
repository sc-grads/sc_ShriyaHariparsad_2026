root@Sambe2025001:~/Linux-Fundamentals# cd ..
root@Sambe2025001:~# mkdir testumask
root@Sambe2025001:~# cd testumask
root@Sambe2025001:~/testumask# umask -S
u=rwx,g=rx,o=rx
root@Sambe2025001:~/testumask# mkdir a-dir
root@Sambe2025001:~/testumask# touch a-file
root@Sambe2025001:~/testumask# ls -l
total 4
drwxr-xr-x 2 root root 4096 Mar 25 10:34 a-dir
-rw-r--r-- 1 root root    0 Mar 25 10:35 a-file
root@Sambe2025001:~/testumask# rmdir a-dir
root@Sambe2025001:~/testumask# rm a-file
root@Sambe2025001:~/testumask# umask 007
root@Sambe2025001:~/testumask# umask 0007
root@Sambe2025001:~/testumask# umask -S
u=rwx,g=rwx,o=
root@Sambe2025001:~/testumask# mkdir a-dir
root@Sambe2025001:~/testumask# touch a-file
root@Sambe2025001:~/testumask# ls -l
total 4
drwxrwx--- 2 root root 4096 Mar 25 10:37 a-dir
-rw-rw---- 1 root root    0 Mar 25 10:37 a-file
root@Sambe2025001:~/testumask#
