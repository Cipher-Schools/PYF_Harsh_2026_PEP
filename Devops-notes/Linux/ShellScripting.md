Shell Script Structure, Syntax​

A shell script is essentially a sequence of commands stored in a text file, which the shell executes in order. Understanding the structure and syntax of shell scripts is essential to write efficient and error-free scripts.​

Shebang (#!):​

The first line in a shell script typically starts with #!/bin/bash​

Specifies which shell should interpret the script​

Comments:​

Lines starting with # are comments and are ignored during execution​

Useful for documenting the script​

Commands:​

Shell commands like ls, cd, echo, pwd are executed sequentially​

Variables:​

Used to store values or user input for reuse in commands​

Example: MYDIR="/home/user/projects"​

​


Control Structures:​

Conditional statements: if...then...else, case​

Loops: for, while, until​

Functions:​

Reusable blocks of code that can be called multiple times within a script​

Example: A simple shell script to displays the current directory and lists all files​

#!/bin/bash​
# This script displays the current directory and lists all files​
​
echo "Current Directory:"​
pwd​
​
echo "Files in Directory:"​
ls -l​

#!/bin/bash: Uses Bash shell to run the script​

echo: Prints text to the terminal​

pwd: Prints the current working directory​

ls -l: Lists files in long format, showing permissions, size, and modification date







# !/bin/bash​
​
# A simple bash script to move up to desired directory level directly​
​
function jump()​
{​
    # original value of Internal Field Separator​
    OLDIFS=$IFS​
​
    # setting field separator to "/"​
    IFS=/​
​
    # converting working path into array of directories in path​
    # eg. /my/path/is/like/this​
    # into [, my, path, is, like, this]​
    path_arr=($PWD)​
​
    # setting IFS to original value​
    IFS=$OLDIFS​
​
    local pos=-1​
​
    # ${path_arr[@]} gives all the values in path_arr​
    for dir in "${path_arr[@]}"​
    do​
        # find the number of directories to move up to​
        # reach at target directory​
        pos=$[$pos+1]​
        if [ "$1" = "$dir" ];then​
​
            # length of the path_arr​
            dir_in_path=${#path_arr[@]}​
​
            #current working directory​
            cwd=$PWD​
            limit=$[$dir_in_path-$pos-1]​
            for ((i=0; i<limit; i++))​
            do​
                cwd=$cwd/..​
            done​
            cd $cwd​
            break​
        fi​
    done​
























Making the Script Executable​

By default, scripts do not have execution permissions. To make it executable:​

Command:​

chmod +x path/to/our/file/jump.sh​

Integrating with .bashrc for Persistent Availability​

To make the jump function available in every terminal session:​

Command:​

echo "source ~/path/to/jump.sh" >> ~/.bashrc​

After restarting the terminal, you can use the script​

Command:​

jump directory_name​