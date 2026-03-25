root@Sambe2025001:~/Linux-Fundamentals# ls -l
total 4
-rw-r--r-- 1 root root 46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -lr
total 4
-rw-r--r-- 1 root root 46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -lat
total 12
-rw-r--r-- 1 root root   46 Mar 25 09:04 file.txt
drwxr-xr-x 2 root root 4096 Mar 25 09:01 .
drwx------ 6 root root 4096 Mar 25 09:01 ..
root@Sambe2025001:~/Linux-Fundamentals# ls -latr
total 12
drwx------ 6 root root 4096 Mar 25 09:01 ..
drwxr-xr-x 2 root root 4096 Mar 25 09:01 .
-rw-r--r-- 1 root root   46 Mar 25 09:04 file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -R
.:
file.txt
root@Sambe2025001:~/Linux-Fundamentals# tree -d
Command 'tree' not found, but can be installed with:
snap install tree
root@Sambe2025001:~/Linux-Fundamentals# ls -d
.
root@Sambe2025001:~/Linux-Fundamentals#
root@Sambe2025001:~/Linux-Fundamentals# ls --color
file.txt
root@Sambe2025001:~/Linux-Fundamentals# ls -R
.:
file.txt
root@Sambe2025001:~/Linux-Fundamentals# tree
Command 'tree' not found, but can be installed with:
snap install tree
root@Sambe2025001:~/Linux-Fundamentals#
