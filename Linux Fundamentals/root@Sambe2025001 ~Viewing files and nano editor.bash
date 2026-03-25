root@Sambe2025001:~# mkdir my_file
root@Sambe2025001:~# cd my_file
root@Sambe2025001:~/my_file# touch file.txt
root@Sambe2025001:~/my_file# echo "This is the first line.
This is the second.
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
All my base are belong to you.
Finally, the 12th and last line.
$ head file.txt
This is the first line.
This is the second.
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
$ tail file.txt
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
More filler text." >> file.txt
root@Sambe2025001:~/my_file# cat myfile.txt
cat: myfile.txt: No such file or directory
root@Sambe2025001:~/my_file# cat file.txt
This is the first line.
This is the second.
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
All my base are belong to you.
Finally, the 12th and last line.
$ head file.txt
This is the first line.
This is the second.
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
$ tail file.txt
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
All my base are belong to you.
Finally, the 12th and last line.
$ more file.txt
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
root@Sambe2025001:~/my_file# head file.txt
This is the first line.
This is the second.
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
The quick brown fox jumps over the lazy dog.
The dog was rather impressed.
Roses are red,
Violets are blue,
root@Sambe2025001:~/my_file# head -2 file.txt
This is the first line.
This is the second.
root@Sambe2025001:~/my_file# tail file.txt
The dog was rather impressed.
Roses are red,
Violets are blue,
All my base are belong to you.
Finally, the 12th and last line.
$ more file.txt
Here is some more interesting text.
Knock knock.
Who's there?
More filler text.
root@Sambe2025001:~/my_file# tail -1 file.txt
More filler text.
root@Sambe2025001:~/my_file# nano file.txt
root@Sambe2025001:~/my_file# nano file.txt
root@Sambe2025001:~/my_file# nano file.txt
root@Sambe2025001:~/my_file#
