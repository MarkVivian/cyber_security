#!/bin/bash

# ****************** SINGLE BRACKETS ***********************
# its a traditional way of writing tests and conditional expressions.
# It requires proper quoting of variables to handle spaces and special characters correctly.


# ------------BASIC SYNTAX---------------
# if [ condition ]; then
    # command to execute.
# fi


# ----------------COMPARISON OF NUMERICAL VALUES------------------
# Terms
# -eq : equal to
# -ne : Not equal to
# -gt : Greater than
# -lt : Less than
# -ge : Greater than or equal to
# -le : Less than or equal to

read -p "enter a value: " value;

if [ $value -eq 8 ]; then
    echo "the values match good guess."
else    
    echo "wrong value"

    if [ $value -lt 8 ]; then
        echo "the value was too low"
    else
        if [ $value -gt 8 ]; then
            echo "the value was too large"
        fi
    fi
fi


# -------------CHECK IF FILE --------------
# -e, -a : checks if file exists.
# -r : checks if file is readable
# -w : checks if file is writable.
# -x : checks if file is executable.
# -d : checks if a file is a directory.
# -f : check if a file is not a directory.
# -s : check if file is not empty.
# -L, -h : check if file is a symbolic link.
# ! : negates a command.
# -b : true if file exists and is a block special file (mostly files found in /dev and  used by storage devices like hard disks.).
# -c : true if file exists and is a character special file (mostly files found in /dev and include device files for ports )
# -g : True if the file exists and is set-group-id. set-group-id (sgid): If set on a file, it means that when the file is executed, it will run with the privileges of the group that owns the file instead of the user who executed it.
# -G : True if the file exists and is owned by the effective group id. Effective Group ID: This refers to the group ownership of the file. This check determines whether the file is owned by the same group as the user executing the script.
# -k : True if the file exists and has the sticky bit set. Sticky Bit: When the sticky bit is set on a directory, it restricts who can delete or rename files within that directory. On files, the sticky bit has no effect in modern systems.
# -ef : True if the two files refer to the same device and inode numbers. This checks if two files are hard links to each other, meaning they refer to the same inode on the filesystem.
# -ot : true if file exists and is older than other files.This checks if one file is older than another file, based on modification timestamps. 
# -nt : true if file exists and is newer than other files.This checks if one file is newer than another file, based on modification timestamps.
# -u : true if a file exists and its set-user-id bit is set.If set on a file, it means that when the file is executed, it will run with the privileges of the user who owns the file instead of the user who executed it.
# -t : True if the file descriptor number n is open and associated with a terminal. This checks if a particular file descriptor is associated with a terminal.
# -S : true if file exists and is a socket. files used for inter processs communication within a newtork,
# -s : true if file exists and has a size greater than zero.
# -p : true if file exists and is a named pipe (FIFO). this are files used for communication between processes.
# -O : true if file exists and is owned by the effective user id. checks if the file is owned by the same user who is executing a script.
# -N : true if file exists and has been modified since it was last read.

file_path="./overview.sh"
if [ -e $file_path ]; then
    echo "the file exists."
    if [ -r $file_path ]; then
        echo "the file is readable"
        if [ -s $file_path ]; then
            echo "the file is not empty"
        fi
    fi
else
    if [ ! -e $file_path ]; then
        echo "the file doesn't exist."
    fi
fi


# ****************DOUBLE QUOTES ************************
# This is a newer extension to Bash and provides more features and flexibility compared to single square brackets.
# It supports advanced pattern matching, regular expressions, and additional logical operators (&&, ||, ==, !=, etc.).

# ------------ COMPARISON OF STRING ----------------
# == : checks if strings are equal.
# != : check if strings are not equal.
# -z : check if a string is empty.
# =~ : matches string on the left side against the regular expression on the right side. 
# -n : check if string is not empty.
# "word"* : check if string starts with word
# *"word" : check if string ends with word.
# *"word"* : check if strings contains word.
# > : lexicographical order greather than  
# < : lexicographical order less than

string1="hello"
if [[ -z $string1 ]]; then
    echo "the string is empty"
else   
    if [[ -n $string1 ]]; then
        echo "the string is not empty"
    fi
fi

if [[ $string1 == "world" ]]; then
    echo "the strings match"
else
    echo "the strings do not match"
    if [[ $string1 == *"l"* ]]; then
        echo "the word contains a l"
        if [[ $string1 == *"o" ]]; then
            echo "the word ends with o"
            if [[ $string1 == "h"* ]]; then
                echo "the word starts with h"
            fi
        fi
    fi
fi


# ******************** DOUBLE PARENTHESIS *****************
# used when conducting arithmetic operations.
