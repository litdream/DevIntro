<!-- vscode-markdown-toc -->
	* 1. [pwd](#pwd)
	* 2. [ls](#ls)
	* 3. [cd](#cd)
	* 4. [mkdir](#mkdir)
	* 5. [rmdir](#rmdir)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc --># Basic Linux Commands


After logged in, get used to following commands.

###  1. <a name='pwd'></a>pwd
Print Working Directory.  This will tell where you are located in directory tree.

```
% pwd
/Users/rychung/github/DevIntro
```

###  2. <a name='ls'></a>ls
List all files in current directory.
Simply "ls" will show name only.
Adding a switch(-l), "ls -l" will show other information, such as Size.

```
% pwd
/Users/rychung/github/DevIntro

% ls
2019		LICENSE		README.md

% ls -l
total 16
drwxr-xr-x  3 rychung  1896053708   102 Dec 27 19:47 2019
-rw-r--r--  1 rychung  1896053708  1070 Dec 27 19:46 LICENSE
-rw-r--r--  1 rychung  1896053708   313 Dec 27 19:50 README.md

```

###  3. <a name='cd'></a>cd
Change Directory.
Simply "cd" will always come back to your home directory.
If a directory name is given, cd will change the current location to the name given.

```
% pwd
/Users/rychung/github/DevIntro
% cd
% pwd
/Users/rychung
% ls -l
total 16

....(some names)...
drwxr-xr-x@ 11 rychung  1896053708   374 Dec 15 17:40 bitbucket
drwxr-xr-x   9 rychung  1896053708   306 Dec 27 19:46 github
drwxr-xr-x  11 rychung  1896053708   374 Nov 21 08:39 local
....(some names)...

% cd github
% pwd
/Users/rychung/github
% ls -l
total 0
drwxr-xr-x   6 rychung  1896053708  204 Dec 27 19:47 DevIntro
drwxr-xr-x  16 rychung  1896053708  544 Oct  9 21:36 glg4kids
drwxr-xr-x   5 rychung  1896053708  170 Nov 30 03:40 inf-ruby
% cd DevIntro
% ls -l
total 16
drwxr-xr-x  3 rychung  1896053708   102 Dec 27 19:47 2019
-rw-r--r--  1 rychung  1896053708  1070 Dec 27 19:46 LICENSE
-rw-r--r--  1 rychung  1896053708   313 Dec 27 19:50 README.md
% pwd
/Users/rychung/github/DevIntro
```

###  4. <a name='mkdir'></a>mkdir

Create a new directory.  Name is required.

```
% cd
% cd prj
% ls -l
total 0
drwxr-xr-x  3 rychung  1896053708  102 Oct  9 21:43 game-sample
drwxr-xr-x  9 rychung  1896053708  306 Dec  4 10:24 node.js
drwxr-xr-x  7 rychung  1896053708  238 Oct  9 21:33 pygame
drwxr-xr-x  3 rychung  1896053708  102 Dec 27 19:21 vscode
% mkdir hello
% cd hello
% pwd
/Users/rychung/prj/hello
% ls -l
%
```


###  5. <a name='rmdir'></a>rmdir

Remove a directory.  Only empty directory can be removed.
We will talk about removing files and directories seperately.

```
% cd
% cd prj
% ls -l
total 0
drwxr-xr-x  3 rychung  1896053708  102 Oct  9 21:43 game-sample
drwxr-xr-x  2 rychung  1896053708   68 Dec 27 20:01 hello
drwxr-xr-x  9 rychung  1896053708  306 Dec  4 10:24 node.js
drwxr-xr-x  7 rychung  1896053708  238 Oct  9 21:33 pygame
drwxr-xr-x  3 rychung  1896053708  102 Dec 27 19:21 vscode
% rmdir hello
% ls -l
total 0
drwxr-xr-x  3 rychung  1896053708  102 Oct  9 21:43 game-sample
drwxr-xr-x  9 rychung  1896053708  306 Dec  4 10:24 node.js
drwxr-xr-x  7 rychung  1896053708  238 Oct  9 21:33 pygame
drwxr-xr-x  3 rychung  1896053708  102 Dec 27 19:21 vscode
```
