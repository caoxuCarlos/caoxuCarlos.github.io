# Process

[toc]

This is a note for [Introduction to Linux](http://www.tldp.org/LDP/intro-linux/html/index.html).

## Processes inside out

### Multi-user and Multi Task

Not every command starts a single process.  Some commands initiate a series of processes, such as **mozilla**; others, like **ls**, are executed as a single command.

Furthermore, Linux is based on UNIX, where it has  been common policy to have **multiple users running multiple commands, at  the same time and on the same system.**  It is obvious that measures have  to be taken to have the CPU manage all these processes, and that  functionality has to be provided so users can switch between processes.  In some cases, processes will have to continue to run even when the  user who started them logs out.  And users need a means to reactivate  interrupted processes. 

### Process Types

* Interactive processes

  Interactive processes are initialized and controlled through a terminal  session.  In other words, there has to be someone connected to the  system to start these processes; they are not started automatically as  part of the system functions.  

  They can run **both foreground and background**.

  The shell offers a feature called **job control** which allows easy handling of multiple processes. 

  In order to free the issuing terminal after entering the command, a trailing ampersand(`&`) is added. 

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/001.png)

  The full job control features are explained in detail in the **bash** Info pages, so only the frequently used job control applications are listed [here](http://www.tldp.org/LDP/intro-linux/html/sect_04_01.html#AEN4685):

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/002.png)

  And we use `screen` to make a long time task run background or on a remote server. Click [here](https://www.youtube.com/watch?v=3txYaF_IVZQ) to learn this magic tool.
  
* Automatic processes

  Automatic or batch processes are not connected to a terminal.   Rather, these are tasks that can **be queued** into a spooler area, where  they wait to be executed on a FIFO (**first-in, first-out**) basis.  Such  tasks can be executed using one of two criteria:

  - At a certain date and time: done using the **at** command, which we will discuss in the second part of this chapter.
  - At times when the total system load is low enough to accept extra jobs: done using the **`batch`** command.  By default, tasks are put in a queue where they wait to be  executed until the system load is lower than 0.8.  In large  environments, the system administrator may prefer batch processing when  large amounts of data have to be processed or when tasks demanding a lot of system resources have to be executed on an already loaded system.   Batch processing is also used for optimizing system performance. 

* Daemons are server processes that run continuously.  Most of the time,  they are initialized at system startup and then wait in the background  until their service is required.  A typical example is the networking  daemon, *xinetd*, which is started in almost every boot  procedure.  After the system is booted, the network daemon just sits and waits until a client program, such as an FTP client, needs to connect.

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/003.png)

  > <u>*This little fairy help you guard your computer background.*</u>

### Process Attribute

A process has a series of characteristics, which can be viewed with the **ps** command:

- The process ID or PID: a **unique identification number used to refer to the process**.
- The parent process ID or PPID: the number of the **process (PID) that started this process**.
- Nice number: the degree of friendliness of this process toward other  processes (not to be confused with process priority, which is calculated based on this nice number and recent CPU usage of the process).
- Terminal or TTY: terminal to which the process is connected.
- User name of the real and effective user (RUID and EUID): the owner of the  process.  The real owner is the user issuing the command, the effective  user is the one determining access to system resources.  RUID and EUID  are usually the same, and the process has the same access rights the  issuing user would have.

### Displaying process information

The **ps** command is one of the tools for  visualizing processes.  This command has several options which can be  combined to display different process attributes.

With no options specified, **ps** only gives information about the current shell and eventual processes:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/004.png)

Since this does not give enough information - generally, at least a  hundred processes are running on your system - we will usually select  particular processes out of the list of all processes, using the **grep** command in a *pipe*(`|`)

```bash
ps -ef | grep bash
```

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/005.png)

Note that **ps** **only gives a momentary state of the active processes**, it is a one-time recording.  The **top** program displays a more precise view by updating the results given by **ps** (with a bunch of options) once every five seconds, generating a new  list of the processes causing the heaviest load periodically, meanwhile  integrating more information about the swap space in use and the state  of the CPU, from the `proc` file system.

![pass 006](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/006.png)

The first line of **`top`** contains the same information displayed by the **uptime** command:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/007.png)

The relations between processes can be visualized using the **pstree** command:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/008.png)

### LIfe and Death of a Process

* process creation

  A new process is created because an existing process makes an exact copy of itself.  This child process has the same environment as its parent,  only the process ID number is different.  This procedure is called *forking*.

  The *fork-and-exec* mechanism thus switches an old command  with a new, while **the environment in which the new program is executed  remains the same**. 

  This scheme illustrates the fork-and-exec mechanism.  The process ID changes after the fork procedure:

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/009.png)

  There are a couple of cases in which **init** becomes the parent of a process, while the process was not started by **init**. 

   Many programs, for instance, **daemonize** their child processes, so they can keep on running when the parent stops or is being stopped.

  In an exceptional case, a process might finish while the parent does  not wait for the completion of this process.  Such an unburied process  is called a *zombie* process.

* ending process

  When a process ends normally (it is not killed or otherwise unexpectedly interrupted), the program returns its *exit status* to the parent.  This exit status is a number returned by the program providing the results of the program's execution.  

* signals

  Processes end because they receive a signal.  There are multiple signals that you can send to a process.  Use the **kill** command to send a signal to a process.  The command **`kill -l`**shows a list of signals.  Most signals are for internal use by the system, or for programmers when they write code.  

  Common signals():

  ![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/010.png)

### SUID snd SGID

 These modes exist to provide normal users the ability to execute tasks  they would normally not be able to do because of the tight file  permission scheme used on UNIX based systems.

An interesting example [here](http://www.tldp.org/LDP/intro-linux/html/sect_04_01.html#sect_04_01_06).  

In a group, different user have different terminal(s).

## Boot process, Init and shutdown

### Introduction

One of the most powerful aspects of Linux concerns its open method of  starting and stopping the operating system, where it loads specified  programs using their particular configurations, permits you to change  those configurations to **control the boot process, and shuts down in a  graceful and organized way**.

### The boot process

I can't skip a single word, so this is the [link](http://www.tldp.org/LDP/intro-linux/html/sect_04_02.html#NAVHEADER) ,see 4.2.2.

### The GRUB

A boot method without wiping other systems MBR configuration.

### Init

The kernel, once it is loaded, finds **init** in `sbin` and executes it.

When **init** starts, it becomes **the parent or  grandparent of all of the processes that start up automatically on your  Linux system**. 

> 1. **`init` **reads its initialization file, `/etc/inittab`
>
>    Basically, this step takes care of everything that your system needs to  have done at system initialization: setting the clock, initializing  serial ports and so forth.
>
> 2. **`init` **continues to read the `/etc/inittab` file, which describes how the system should be set up in each run level and sets the default **run level**. 
>
> 3.  **`init`** starts all of the **background processes necessary for the system** to run by looking in the appropriate `rc` directory for that run level.

### Init run level

The idea behind operating different services at different run levels  essentially revolves around the fact that different systems can be used  in different ways. Some services only can be used when the system is in a particular state, or *mode*, such as being ready for more than one user or having networking available.

Use `who -r` to check what your current level is :

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/011.png)

Default run level. The run levels are:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/012.png)

Ubuntu 16.04 uses **`systemd`** instead of **`init`** and hence the concept of `runlevels` is replaced by the term `targets`. So there is indeed a mapping between init-based runlevels and systemd-based targets:

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/013.png)

More specific instruction see [here](https://askubuntu.com/a/788465).

### Tools

There are some tool to provide a simple command-line tool for maintaining the `/etc/init.d` directory hierarchy. These relieve system administrators from having to directly manipulate the numerous symbolic links in the directories  under `/etc/rc[x].d`.

### Shutdown

`shutdown -h` 

## Managing Processes

### How long does it take

Bash offers a built-in **time** command that displays how long a command takes to execute.  The timing is highly accurate and can be used on any command. 

![pass 014](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/014.png)

### load

Run `w` or `top` to check the load. 

### Can I do anything as a user?

**A big environment can slow you down.**

* Priority

  The priority or importance of a job is defined by it's *nice*  number.  A program with a high nice number is friendly to other  programs, other users and the system; it is not an important job.  **The  lower the nice number, the more important a job is and the more  resources it will take without sharing them.**

  Making a job nicer by increasing its nice number is only useful for  processes that use a lot of CPU time (compilers, math applications and  the like).  **Processes that always use a lot of I/O time are  automatically rewarded by the system and given a higher priority** (a  lower nice number), for example keyboard input always gets highest  priority on a system.

  Defining the priority of a program is done with the **nice** command. Change the niceness of a running commond by `renice [newvalue] [ProcessID]`.

  > It is NOT a good idea to **nice** or **renice** an interactive program or a job running in the foreground.

* CPU resources

  On every Linux system, many programs want to use the CPU(s) at the same  time, even if you are the only user on the system.  Every program needs a certain amount of cycles on the CPU to run.  There may be times when  there are not enough cycles because the CPU is too busy. There are some actions you can undertake if you think your CPU is to blame for the unresponsiveness of your system:

  - Run heavy programs when the load is low.  This may be the  case on your system during the night.  See next section for scheduling.
  - Prevent the system from doing unnecessary work: stop daemons and programs that you don't use, use **locate** instead of a heavy **find**, ...
  - Run big jobs with a low **priority**

* Memory resources

  When the currently running processes expect more memory than the system  has physically available, a Linux system will not crash; it will start  paging, or *swapping*, meaning the process uses the memory on  disk or in swap space, moving contents of the physical memory (pieces of running programs or entire programs in the case of swapping) to disk,  thus reclaiming the physical memory to handle more processes.  This  slows the system down enormously since access to disk is much slower  than access to memory.  The **top** command can be used to display memory and swap use.

  If you find that a lot of memory and swap space are being used, you can try:

  - Killing, stopping or renicing those programs that use a big chunk of memory
  - Adding more memory (and in some cases more swap space) to the system.
  - Tuning system performance, which is beyond the scope of this document.  See the reading list in [Appendix A](http://www.tldp.org/LDP/intro-linux/html/app1.html) for more.

* I/O resources

  `iotop`

  `iotop -o`

  `iostat`

  `vmstat` : virtual memory statistics

  `netstat`: print network connections, routing tables, interface statistics, masquerade connections,...

  Network I/O problems

  Disk I/O problems.

* Users

  Users can be divided in several classes, depending on their behavior with resource usage:

  - Users who run a (large) number of small jobs: you, the beginning Linux user, for instance.
  - Users who run relatively few but large jobs: users running simulations,  calculations, emulators or other programs that eat a lot of memory, and  usually these users have accompanying large data files.
  - Users who run few jobs but use a lot of CPU time (developers and the like).

  You can see that system requirements may vary for each class of users, and  that it can be hard to satisfy everyone.  If you are on a multi-user  system, it is useful (and fun) to **find out habits of other users and the system**, in order to get the most out of it for your specific purposes.

* Graphical tools

  `htop`

* Interrupting your processes

  As a non-privileged user, you can only influence your own processes.  We already saw how you can display processes and filter out processes  that belong to a particular user, and what possible restrictions can  occur.  When you see that **one of your processes is eating too much of  the system's resources**, there are two things that you can do:

  1. Make the process use less resources without interrupting it;(`renice`,`top`+`r`)

  2. Stop the process altogether.`kill`&`xkill`

     In a graphical environment, the **xkill** program is very easy to use.  Just type the name of the command, followed by an **Enter** and select the window of the application that you want to stop.  It is  rather dangerous because it sends a SIGKILL by default, so only use it  when an application hangs.

## Scheduling processes

### Use that idle time

A Linux system can have a lot to suffer from, but it usually suffers  **only during office hours**.  Whether in an office environment, a server  room or at home, most Linux systems are just idling away during the  morning, the evening, the nights and weekends.  Using this idle time can be a lot cheaper than buying those machines you'd absolutely need if  you want everything done at the same time.

### The `sleep` command

The Info page on sleep is probably one of the shortest there is.  All **sleep** does is wait.  By default the time to wait is expressed in **seconds**.

```bash
sleep <number> [unit];<commond>
(sleep 1800;echo "lunch")&
(sleep 10000; myprogram) &
echo "a";sleep 5;echo "b";sleep 5;echo "c"
(sleep 10;./pythoncharm)&
```

### The `at` command

Typing **Ctrl**+**D** quits the **at** utility and generates the "EOT" message.

For  example,  to  run  a  job `at 4pm + 3 days` from now, you would do at 4pm + 3 days, to run a job at `10:00am on July 31`, you would do at 10am Jul 31 and to run a job at 1am tomorrow, you would  do  at  1am tomorrow.

`atq` to check jobs to be done

`atre`+`任务编号` remove job

It is a good idea to pick strange execution times, because system jobs are often run at "round" hours, as you can see in [Section 4.4.4](http://www.tldp.org/LDP/intro-linux/html/sect_04_04.html#sect_04_04_04) the next section.  For example, jobs are often run at exactly 1 o'clock in the morning (e.g. system indexing to update a standard locate  database), so entering a time of 0100 may easily slow your system down  rather than fire it up.  To prevent jobs from running all at the same  time, you may also use the **batch** command, which  queues processes and feeds the work in the queue to the system in an  evenly balanced way, preventing excessive bursts of system resource  usage.(所以尽量不要安排到正点去做，而且`batch`没那么多逼事儿，直接`batch`然后你就输入命令就行了，在内存低的时候它自己会执行。)

### Cron and crontab

就是每天固定时间执行任务。

At system startup the cron daemon searches `/var/spool/cron/` for crontab entries which are named after accounts in `/etc/passwd`, it searches `/etc/cron.d/` and it searches `/etc/crontab`, then **uses this information every minute** to check if there is something to be done.

![pass015](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/015.png)

**Some variables are set, and after that there's the actual scheduling,  one line per job, starting with 5 time and date fields.  The first field contains the minutes (from 0 to 59), the second defines the hour of  execution (0-23), the third is day of the month (1-31), then the number  of the month (1-12), the last is day of the week (0-7, both 0 and 7 are  Sunday).  An asterisk in these fields represents the total acceptable  range for the field.  Lists are allowed; to execute a job from Monday to Friday enter 1-5 in the last field, to execute a job on Monday,  Wednesday and Friday enter 1,3,5.Then comes the user who should run the processes which are listed in the last column.**

`crontab -l` display crontbas

`crontab -e` edit crontabs

![pass 016](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/linux_note_picture_for_C4/016.png)

> The `backup.sh` script is executed every Thursday and Sunday.

You don't have to specify the user who should run the commands.  They are executed with the user's own permissions by default.