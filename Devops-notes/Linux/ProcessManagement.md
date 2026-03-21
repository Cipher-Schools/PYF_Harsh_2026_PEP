List Running process ​:

Listing running processes in Linux helps you monitor and manage all active programs and system tasks.​

Linux provides commands to view active processes and their details like PID, CPU, and memory usage.​

The most common command is ps, which shows currently running processes.​

top displays real-time updates of system processes and resource usage.​

htop offers an interactive, color-coded view for easier process management.​

These tools help in diagnosing system performance issues or terminating unresponsive processes.​

List Running Processes in Linux​

We can use multiple commands to list the running processes in Linux like ps, top, htop,and atop commands in Linux. We can also have a combination of commands to list the running processes in Linux.​

1. The `ps` Command to List Running Processes in Linux​

The ps command in Linux is used to display information about the currently running processes on the system.​

ps stands for process status.​

It shows details like PID, user, CPU, memory usage, and the command that started the process.​

By default, it displays processes running in the current shell.​

Use options to view more detailed or system-wide process information.​

Common formats include standard (ps), user-based (ps -u), and full system (ps -ef or ps aux).​

Often combined with grep to find specific processes.​

Useful for monitoring and troubleshooting running applications and services.​

Example:​

Simple process selection : Shows the processes for the current shell - ​

 ps​



 Result contains four columns of information. Where, ​

PID - the unique process ID ​

TTY - terminal type that the user is logged into ​

TIME - amount of CPU in minutes and seconds that the process has been running ​

CMD - name of the command that launched the process. ​

Syntax of `ps` Command in Linux​

The ps command provides a snapshot of the current processes on your system. The basic syntax is as follows:​

ps [options]​



1) View All Running Processes in Linux.​

To view all running processes, use either of the following options with the `ps`command:​

ps –A​

​

2) List Processes Not associated with a Terminal in Linux​

View all processes except both session leaders and processes not associated with a terminal. ​

ps –a​

​

​

3) List All The Processes Except Session Leaders in Linux​

A session leader is a process that initiates other processes. View processes except session leaders:​

ps -d​
​

​

​

displays a detailed snapshot of all running processes in the system including system, background, and user processes.​

ps aux​




6) List All Processes Associated with this Terminal in Linux​

ps –T​

​

​

7) View All Processes Owned By You​

Processes i.e same EUID as ps which means runner of the ps command, root in this case - ​

ps -x​





Top command​:

In Linux, the `top` command is a dynamic and interactive tool that provides real-time information about system processes. It offers a comprehensive view of running processes, system resource
utilization, and other critical system metrics. This article explores how to effectively use the top command to monitor and manage processes.​

Launching top​

To launch the top command, open a terminal and simply type:​

Top​

​

​

Process-related information including:​

PID: Process ID​

USER: Owner of the process​

PR: Priority​

NI: Nice value​

VIRT: Virtual memory usage​

RES: Resident set size (non-swapped physical memory used)​

SHR: Shared memory​

S: Process status (S: Sleeping, R: Running, I: Idle)​

%CPU: Percentage of CPU usage​

%MEM: Percentage of memory usage​

TIME+: Total CPU time​

COMMAND: Command or process name​

​

kill Command in Linux​:

The kill command in Linux is used to send signals to processes in order to control their execution. It is commonly used to terminate processes, but it can also pause, resume, or perform other actions depending on the signal sent. The kill command sends signals to processes using their Process ID (PID).​

Located in /bin/kill , it’s a built-in Linux command.​

Sends specific signals to processes using their Process ID (PID).​

By default, it sends the SIGTERM (15) signal to terminate a process.​

Can use other signals like SIGKILL (9) or SIG STOP (19) for different actions.​

Example: Killing Mozilla Firefox Process​

Terminate the Mozilla Firefox browser process when it becomes unresponsive or needs to be closed from the terminal.​

​

Step 1: Identify the Firefox PID​

Check the running Firefox processes and their PIDs.​

Command:​

ps aux | grep firefox​

ps aux: Lists all running processes with details.​

grep firefox: Filters processes related to Firefox.​

​

​

Step 2: Gracefully Terminate Firefox​

Send the SIGTERM (15) signal to allow Firefox to close properly.​

Command:​

kill 22673​

Explanation:​

22673 is the PID of the main Firefox process.​

The default SIGTERM signal requests a graceful shutdown.​

Child processes typically terminate automatically along with the parent process.​




Step 3: Force Kill Firefox (if it doesn’t close)​

If Firefox is unresponsive, use SIGKILL (9) to terminate it immediately.​

Command:​

kill -9 22673​

-9: Sends the SIGKILL signal. Forces the process to stop immediately without cleanup.​

​

​

Step 4: Verify Firefox Termination​

Check that no Firefox processes remain:​

Command:​

ps aux | grep firefox​