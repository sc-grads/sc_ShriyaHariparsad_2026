root@Sambe2025001:~/Linux-Fundamentals# ls
file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -a
.  ..  file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -l
total 4
-rw-r--r-- 1 root root 46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -l -a
total 12
drwxr-xr-x 2 root root 4096 Mar 25 09:01 .
drwx------ 6 root root 4096 Mar 25 09:01 ..
-rw-r--r-- 1 root root   46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -a -l
total 12
drwxr-xr-x 2 root root 4096 Mar 25 09:01 .
drwx------ 6 root root 4096 Mar 25 09:01 ..
-rw-r--r-- 1 root root   46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals#
