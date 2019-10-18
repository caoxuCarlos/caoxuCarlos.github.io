# About file and file system

[toc]

This is a note for [Introduction to Linux](http://www.tldp.org/LDP/intro-linux/html/index.html).

## General

### Files

On a UNIX system, **everything is a file**; if something is not a file, it is a process. 

> *This a very important idea, because basically everything can be edit use just one group of API.*
>
> <u>*API is short for application programming interface.*</u>
>
> *<u>When you type a command in terminal, your terminal actually translate your command, and execute a **file** .*</u>

A Linux system, just like UNIX, makes no difference between a file and a directory, since a directory is just a file containing names of other files: 

> Directories: files that are **lists of other files**.
>
> Special files: the **mechanism used for input and output**. Most special files are in `/dev`.
>
> Links: a system to make a file or directory visible in multiple parts of the system's file tree.
>
> Named pipes: act more or less like sockets and form a way for processes to communicate with each
> other, without using network socket semantics.

Use **`ls -l`** to check file type:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/001.png)

Different head character represent different file types: 

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/002.png)

Use **`ls -F`** also helps to show different file with different color:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/003.png)

### Partitioning

One of the goals of having different partitions is to achieve **higher data security in case of disaster**.

This principle dates from the days when Linux didn't have journaled file systems and power failures might have lead to disaster. The use of partitions remains for **security and robustness** reasons, so a breach on one part of the system doesn't automatically mean that the whole computer is in danger. This is currently the most important reason for partitioning. 

> A simple example: a user creates a script, a program or a web application that starts filling up the disk. If the disk contains only one big partition, the entire system will stop functioning if the disk is full. If the user stores the data on a separate partition, then only that (data) partition will be
> affected, while the system partitions and possible other data partitions keep functioning.

There are two types of partitions in Linux. 

* data partition: normal Linux system data, including the root partition containing all the data to start up and run the system.
* swap partition: expansion of the computer's physical memory, extra memory on hard disk. (Remember that, CPU is processor, RAM is memory, Hard Drive is Storage. RAM can translate data very fast with CPU. Hard Drive is larger but slower. **The swap partition is to use part of Storage as memory.** To know more about this, click to watch [this video](https://www.youtube.com/watch?v=ExxFxD4OSZ0).)

You can use swap partition and swap file, allocate how much **storage** will be used as **memory**. Watch [this video](https://averagelinuxuser.com/linux-swap/) to check the specific way.

For data partitions, they got their name for a reason:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/004.png)

Use **`dh -h . `**to show which partition the current directory belong.

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/005.png)

### inode

**Inodes** are numbers to mark a file's identity, which looks like `10626490`.

Kind of like the address in C language, and I personally regard it as abbreviation of **information node**.

Each inode describes a data structure on the hard disk, storing the properties of a file, including the physical location of the file data.

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/006.png)

Use **`ls -i` **to check inodes of files in the directory.

> **When a hard disk is initialized to accept data storage, a fixed number of inodes per partition is created**. This number will be the maximum amount of files, of all types (including directories, special files, links etc.) that can exist at the same time on the partition. We typically count on having 1 inode per 2 to 8 kilobytes of storage.

## Orientation in the file system

### the PATH variable

This variable lists those **directories in the system where executable files can be found**, and thus saves the user a lot of typing and memorizing locations of commands. 

When you want the system to execute a command, **you almost never have to give the full path to that command**. For example, we know that the ls command is in the `/bin` directory, yet we don't have to enter the command `/bin/ls` for the computer to list the content of the current directory.

The echo command is used to display the content ("$") of the variable PATH:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/007.png)

> Note the use of the `su` (switch user) facility, which allows you to run a shell in the environment of another user, on the condition that you know the user's password.
>
> `su root `, `su <username>`

We can add file in `PATH` variable to start them directly in terminal. 

### Absolute and relative paths

begin with `/`

In relative paths we also use the . and .. indications for the current and the parent directory.

### The most important file in the system

* The **kernel** is the heart of the system. It manages the communication between the underlying hardware and the peripherals. The kernel also makes sure that processes and daemons (server processes) are started and stopped at the exact right times.

  > <u>*Daemons are server processes that run continuously. Most of the time,  they are initialized at system startup and then wait in the background  until their service is required.*</u> 

* **shell**

  **Shell is file.**

  **A shell manages the interaction between the system and its users.**

  Bash is a kind of shell, so, it's also a shell(**B**ourne **A**gain **SH**ell). 

  The shell, on the other hand, is an advanced way of communicating with the system, because it allows for two-way conversation and taking initiative. Both partners in the communication are equal, so new ideas can be tested. The shell allows the user to handle a system in a very flexible way. An additional asset is that the shell allows for **task automation**.

  There are different shell types, which means you can use different to realize task automation：

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/008.png)

  If you don't know which shell you are using: `echo $SHELL`

* **home**

  The correct path to your home directory is stored in the HOME environment variable, in case some program needs it. With the `echo $HOME` command you can display the content of this variable. 

### The Most Important Configuration

As we mentioned before, most configuration files are stored in the /etc directory. **Content can be viewed using the `cat` command**, which sends text files to the standard output (usually your monitor).

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/009.png)

If you need change some configuration in a specific configuration file, I suggest just google it.

### The Most Common Variable Files

In the `/var` directory we find a set of directories for storing specific **non-constant data** (as opposed to the ls program or the system configuration files, which change relatively infrequently or never at all). All files that change frequently, such as log files, mailboxes, lock files, spoolers etc. are kept in a subdirectory of `/var`.

## Manipulating FIles 

```bash
ls -a # show files start with dot

```

Every directory contains **a file named just dot (.)** and **one with two dots (..)**, which are **used in combination with their inode number to determine the directory's position** in the file system's tree structure. 

A common combination is **`ls -al`**; it shows a long list of files and their properties as well as the destinations that any symbolic links point to. (**Which means options can be combined**.)

Linux marked different file with different. This is the default color scheme: 

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/010.png)

* **`file`**

  To find out more about the kind of data we are dealing with, we use the **file** command. 

  ```bash
  mike:~> file me+tux.jpg
  me+tux.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI),
              "28 Jun 1999", 144 x 144
  ```

  Keep in mind that the results of **file** are **<u>not absolute</u>**, it is only a guess. In other words, **file** can be tricked.

* **`mkdir`**

  ```bash
  mkdir [OPTION]... DIRECTORY...
  ```

  Creating directories and subdirectories in one step is done using the -p option.`mkdir -p /first/second/thrid`

* **`mv`**

  1. rename`mv old_name newname` 
  2. move`mv target_file new_place`

* **`cp`**

  Copying files and directories is done with the **cp** command. A useful option is recursive copy (copy all underlying files and subdirectories), using the `-R` option to **cp**. The general syntax is

  **`cp [-R] fromfile tofile`**

* **`rm`**

  Use the **rm** command to remove single files, **rmdir** to remove empty directories. (Use **`ls -a`** to check whether a directory is empty or not). The **rm** command also has options for removing non-empty directories with all their subdirectories, read the Info pages for these rather dangerous options.

  `rm -rf`to delete directories			r: recursive			f: force

* **`which`**

  A very simple way of looking up files is using the **`which`** command, to look in the directories listed in the user's search path for the required file. Of course, since the search path contains **only paths to directories containing executable** programs, **`which`** <u>doesn't work for ordinary files.</u> 

  ```bash
  which executabel_file_name
  ```

  Which only search in `PATH` variable. 

* **`find`**

  These are the real tools, used when searching other paths beside those listed in the search path. The find tool,
  known from UNIX, is very **powerful**, which may be the cause of **a somewhat more difficult syntax**.(see`man find`)

   This command will call on **rm** as many times as a file answering the requirements is found. In the worst case, this might be thousands or millions of times. This is quite a load on your system. A more realistic way of working would be the use of a pipe (`|` on the `enter` key) and the **xargs** tool with **rm** as an argument. This way, the **rm** command is only called when the command line is full, instead of for every file. 

* **`locate`**

  Later on (in 1999 according to the man pages, after 20 years of **find**), **locate** was developed. This program is easier to use, but more restricted than **find**, since its output is based on a file index database that is updated only once every day. On the other hand, a search in the **locate** database uses less resources than **find** and therefore shows the results nearly instantly.

  Most Linux distributions use **slocate** these days, security enhanced locate, the modern version of **locate** that prevents users from getting output they have no right to read.

* **`grep`**

  A simple but powerful program, **grep** is used for filtering input lines and returning certain patterns to the output. There are literally thousands of applications for the **grep** program. 

### More Way to View File Content

```bash
software file ## use file to find file type
```

* **`cat`**

  其实就是把文件里的东西一口气显示到屏幕上。

  Output was streamed in an uncontrollable way.

* **`more`**

  This command puts text to the output
  one page at the time.

* **`less`**

  less is the GNU version of more and has extra features allowing highlighting of search strings,
  scrolling back etc.

  > ***"`Less` is `more`"***

* **`head`&`tail`**

  These two commands display the n first/last lines of a file respectively. To see the last ten commands entered.

  `head -10 20191014.md`

### Link Types

* Hard link: Associate two or more file names with the same inode. Hard links share the same data blocks on the hard disk, while they continue to behave as independent files.

  There is an immediate disadvantage: hard links can't span partitions, because inode numbers are only unique within a given partition.

* **Soft link or symbolic link** (or for short: symlink): a small file that is a pointer to another file. A symbolic link contains the path to the target file instead of a physical location on the hard disk. Since inodes are not used in this system, soft links can span across partitions.

The command to make links is **ln**. In order to create symlinks, you need to use the `-s` option:

**`ln -s targetfile linkname`**

## File Security

* **`chmod`**

A [simple tutorial](https://www.maketecheasier.com/file-permissions-what-does-chmod-777-means/).

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/011.png)

The way of combination:

```bash
chmod u+rwx,go-rwx hello
```

* owner, group, other

  You should know what your user name is. If you don't, it can be displayed using the **id** command, which also displays the default group you belong to and eventually other groups of which you are a member.

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/012.png)

  our user name is also stored in the environment variable `USER`:

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/013.png)

  However, on many Linux systems you **can only be actively logged in to one group at the time**. By default, this active or *primary group* is the one that you get assigned from the `/etc/passwd` file. The fourth field of this file holds users' primary group ID, which is looked up in the `/etc/group` file. 

  In order to allow more flexibility, most Linux systems follow the so-called **user private group scheme**, that assigns each user primarily to his or her own group. This group is a group that only contains this particular user, hence the name "private group". Usually this group **has the same name as the user login name**, which can be a bit confusing.

  pass

  >  Apart from his own private group, user *asim* can also be in the groups *users* and *web*. Because these are secondary groups to this user, he will need to use the **newgrp** to log into any of these groups (use **gpasswd** for setting the group password first). In the example, *asim* needs to create files that are owned by the group *web*.

  `sudo i-`to get into root.

  `cat /etc/passwd` to show all user

  `passwd username` to set new password for a user

  **<u>User can login though putty.</u>** Which means no matter windows or Linux, we can work as a group! 

  > <u>*Putty is a software.*</u>

  Edit `/etc/passwd` to manage groups.

* file mask

  When a new file is saved somewhere, it is first subjected to the standard security procedure. Files without permissions don't exist on Linux. The standard file permission is determined by the *mask* for new file creation.

  The value of this mask can be displayed using the **umask** command.

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/0014.png)

  In the example above, however, **we see 4 values displayed, yet there are only 3 permission categories**: *user*, *group* and *other*. The first zero is part of the special file attributes settings.

  **Each UNIX-like system has a system function for creating new files**, which is called each time a user uses a program that creates new files, for instance, when downloading a file from the Internet, when saving a new text document and so on. This function creates both new files and new directories. **Full read, write and execute permission is granted to everybody when creating a new directory.** When creating a new file, this function will grant read and write permissions for everybody, but set execute permissions to none for all user categories. This, before the mask is applied, a directory has permissions *777* or *rwxrwxrwx*, a plain file *666* or *rw-rw-rw-*.

  **The *umask* value is subtracted from these default permissions after the function has created the new file or directory.** Thus, a directory will have permissions of *775* by default, a file *664*, if the mask value is *(0)002*. 

  A directory **gets more permissions by default**: it always has the *execute* permission. If it wouldn't have that, it would not be accessible. 

  If you log in to another group using the **newgrp** command, the mask remains unchanged. Thus, if it is set to *002*, files and directories that you create while being in the new group will also be accessible to the other members of that group; you don't have to use **chmod**. 

  These defaults are set system-wide in the shell resource configuration files, for instance `/etc/bashrc` or `/etc/profile`. You can change them in your **own shell configuration file**.

* Changing user and group ownership

  **When a file is owned by the wrong user or group**, the error can be repaired with the **chown** (change owner) and **chgrp** (change group) commands.

  `chown newowner file`

  `chgrp newowner file`

  `ls -l` to show files' owner and group

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note/015.png)

* Special Mode 

  For the system admin to not be bothered solving permission problems all the time, **special access rights can be given to entire directories, or to separate programs**. There are three special modes:

  * Sticky bit mode: After execution of a job, the command is kept in the system memory. Originally this was a feature used a lot to save memory: big jobs are loaded into memory only once.

    The sticky bit is set using the command **`chmod o+t directory`**. The historic origin of the "t" is in UNIX' *save Text access* feature.

  * SUID (set user ID) and SGID (set group ID): represented by the character *s* in the user or group permission field. When this mode is set on an executable file, it will run with the user and group permissions on the file instead of with those of the user issuing the command, thus giving access to system resources.

  * SGID (set group ID) on a directory: in this special case every file created in the directory will have the same group owner as the directory itself (while normal behavior would be that new files are owned by the users who create them). This way, users don't need to worry about file ownership when sharing directories.( Files that are being moved to a SGID directory but were created elsewhere keep their original user and group owner. This may be confusing.)

  These modes also use `chmod` to set permission, they **just offer better control of file permission**. 

