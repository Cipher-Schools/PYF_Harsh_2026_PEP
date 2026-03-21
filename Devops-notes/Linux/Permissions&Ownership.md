Linux Permissions​



Linux file permissions form the foundation of the system’s security model. They define who can read, write, or execute files and
directories, ensuring only authorized users or processes can access sensitive data. You can modify these permissions using the
chmod command.​

chmod +rwx filename – Adds read, write, and execute permissions.​

chmod -rwx directoryname – Removes all permissions.​

chmod +x filename – Grants executable permission.​

chmod -wx filename – Removes write and execute rights

 
Letters​

Definition​

'r'​

"read" the file's contents. ​

 'w'​

"write", or modify, the file's contents. ​

'x' ​

"execute" the file. This permission is given only if the file is a program.​






 How to Check the Permission of Files in Linux​

Let's dive in to understand the possible methods to check all the desired details of a file including "File Permission"​

1. The "Trusty Command"​

Here's the command to execute it within the terminal. Let's show you with an example:​

Input:​

We're taking 'NarX' as a default file name:​

ls -l NarX.txt​

​

Output:​

-rw-r--r-- 1 user group 46 Apr 14 16:37 NarX.txt​

The above command represents these following information:​

The first character = '-', which means it's a file 'd', which means it's a directory.​

The next nine characters = (rw-r--r--) show the security​

The next column shows the owner of the file.​

The next column shows the group owner of the file. (which has special access to these files)​

The next column shows the size of the file in bytes.​

The next column shows the date and time the file was last modified.​

​






2. The 'namei' Command​

The 'namei' command is used to check the file path through layer of folder's path. Here's the command to execute it within Terminal:​

Here, we've taken 'path' as " root@anonymous-VirtualBox:~# " and file name as "hoops"​

namei -l /path/to/your/file​

​

3. The 'stat' Command​

Unlike 'ls -l' command, the "stat" command is used to pin point the file location. Here's how you can do it:​

We're taking file name as "hoops"​

stat hoops​

Output:​

 File: example.txt​
  Size: 2210       Blocks: 8          IO Block: 4096  regular file​
Device: 802h/2050d    Inode: 1288496     Links: 1​
Access: 2024-11-18 10:50:56.000000000 +0000​
Modify: 2024-11-18 10:50:56.000000000 +0000​
Change: 2024-11-18 10:50:56.000000000 +0000​
 Birth: -










 How to Change Permissions in Linux​

​The command you use to change the security permissions on files is called "chmod", which stands for "change mode" because the nine security characters are collectively called the security "mode" of the file. You can modify permissions using symbolic notation or octal notation.​

1. Symbolic Notation​

Symbolic notation allows you to add, remove, or set permissions for specific users. Let's understand this using different example below:​

Example 1: To Change File Permission in Linux​

If you want to give "execute" permission to the world ("other") for file "xyz.txt", you will start by typing. ​

chmod o​

Now you would type a '+' to say that you are "adding" permission. ​

chmod o+​

Then you would type an 'x' to say that you are adding "execute" permission. ​

chmod o+x​

Finally, specify which file you are changing.  ​

chmod o+x xyz.txt​

​

You can also change multiple permissions at once. For example, if you want to take all permissions away from everyone, you would type. ​

chmod ugo-rwx xyz.txt​

















2. Octal Notations Permissions in Linux​

The octal notation is used to represent file permission in Linux by using three user group by denoting 3 digits i.e.​

user​

group​

other users​

Here's how to permissions are mapped:​

Read (r) = 4​

Write (w) = 2​

Execute (x) = 1​

Permissions for owner, group, and others are represented by a three-digit octal value. The sum of permissions for each group gives the corresponding number.​

Reference:​

chmod o​

Now you would type a '+' to say that you are "adding" permission.  ​

chmod o+​

Then you would type an 'x' to say that you are adding "execute" permission. ​

chmod o+x​

Finally, specify which file you are changing.  ​

chmod o+x xyz.txt​









How to Set File Permissions for a
Specific User​

1. By using chown​

Use chown to change file ownsership:​

chown user:group file.txt​

2. By using chmod​

Use chmod to modify permissions:​

chmod 755 file.txt​







chmod Command in Linux​:

The chmod (change mode) command in Linux/UNIX is used to modify file and directory permissions. It controls who can read, write, or execute a file by setting access rights for the owner, group, and others.​

Used to change permissions of files and directories​

Manages access for owner, group, and others​

Controls read (r), write (w), and execute (x) permissions​

Helps maintain system security and proper access control​

Let’s use the chmod command to set the permission to 745.​

Command:​

chmod 745 newfile.txt​

​

​

​

Syntax:​

chmod [options] [mode] [File_name] ​

Here,​

Options: Optional flags that modify the behavior of the chmod command.​

Mode: The permissions to be set, represented by a three-digit octal number or symbolic notation (e.g., u=rw,go=rx).​

File_name: The name of the file or directory for which the permissions are to be changed.​






3. Example of Reverting Changes Made by "chmod" Command​

To undo or revert changes made by the chmod command in Linux, you simply need to run the chmod command again and
specify the correct permissions you want.​

Steps to revert permission changes:​

Decide the correct permission you want to restore.​

Use the chmod command again with the appropriate octal value.​

Example:​

If you want to revert the permissions to rw-r--r--​

Owner: read + write​

Group: read-only​

Others: read-only​

The corresponding octal value is 644. (read = 4, write = 2).​

Command:​

chmod 644 file_or_directory_name​










chown Command in Linux​:

The chown command in Linux allows modifying the ownership of files or directories. It can assign a new user, group, or both,
either individually or simultaneously. Only the root user or the file owner with permissions can perform ownership changes.​

Changes the owner and/or group of files or directories.​

Supports recursive changes with the -R option for directories.​

Can change ownership of single or multiple files at once.​

Offers verbose reporting and conditional ownership change using options.​

Works with symbolic links using dedicated options (-h, -H, -L, -P).​

Example:​

chown vboxuser sample.txt​

chown: modifies file ownership​

vboxuser: becomes the new owner of the file​

sample.txt: is the target file whose ownership is updated​






Syntax​

chown [options] new_owner[:new_group] file(s)​

Here's a breakdown of the components:​

chown: The base command.​

[options]: Optional flags that control the behavior of the command.​

new_owner: Specifies the user who will become the new owner of the file.​

[:new_group]: Specifies the group to be assigned. This part is optional and must be preceded by a colon (:).​

file(s): One or more files or directories whose ownership will be modified.​

​



Examples to Change File Ownership in Linux​:

1. Change the Owner of a File​

To Change the owner of a file in Linux. Update file ownership when responsibility or access needs to be transferred to another user, such
as after file creation by root or file migration between users.​

Syntax:​

chown owner_name file_name​

Command:​

chown master file1.txt​

This designates the user "master" as the new owner of file1.txt.​

​

2. Change the Group of a File​

Modify the group associated with a file so that users belonging to a specific group can access or manage it according to group
permission rules, without altering the file owner.​

Command:​

chown :group1 file1.txt​

':' specifies that only the group ownership is updated​

group1: becomes the new group owner​

​






3. Change Owner and Group of a File​

Perform a simultaneous change of both the file owner and the group to ensure correct ownership and group association in a single operation.​

Command:​

chown master:group1 file1.txt​

master: becomes the new file owner​

group1: is assigned as the new group​

Both ownership attributes are updated together​

​

Change Owner and Group of a File​

Assign both a new user and a new group to a file at the same time, ensuring correct ownership and group assignment in a single command.​

Command:​

chown master:group1 greek1​

master: becomes the new file owner​

group1: is assigned as the new group​

greek1: is the target file​

Both ownership attributes are updated simultaneously​

​