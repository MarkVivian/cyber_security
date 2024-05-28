#!/bin/bash

# ***********************IF LOOPS **************************************
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

# ----------------COMPARISON OF NUMERICAL VALUES------------------
# Terms
# -eq : equal to
# -ne : Not equal to
# -gt : Greater than
# -lt : Less than
# -ge : Greater than or equal to
# -le : Less than or equal to

# ****************** SINGLE BRACKETS AND DOUBLE BRACKETS.***********************
# For simple checks like file existence or basic string comparisons, single brackets suffice.
# For complex evaluations involving string operators, arithmetic comparisons, or regular expressions, double brackets provide a safer and more powerful approach.

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

# ------------BASIC SYNTAX---------------
# if [ condition ]; then
    # command to execute.
# fi

# comparing intergers .
read -p "enter a number between 1 and 10: " value;

if [[ $value -gt 10 ]]; then
    echo "you can't follow instructions, can you? "
else
    echo "sometimes rebel"
fi


# comparing strings.
# we use the normal == not the -eq
read -p "guess a word: " word;

if [[ $word == "mark" ]]; then   
    echo "basic ass nigga"
else
    echo "you must think your soo unique"
fi

# checking if file exists
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

# when comparing strings.
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

# ************************* FOR LOOP ****************************
for (( i=0; i<5; i++)); do
    echo "iteration : $i"
done

items=("mark" "elephant" "lion");

for item in ${items[@]}; do
    echo "items at ${item}"
done


# **************************WHILE LOOP ************************************
current_value=1
while [[ $current_value -lt 10 ]]; do
    echo "value is at $current_value"
    current_value=$(( current_value + 1 ))
done

current_state=true
 
while [[ $current_state ]]; do
    echo "the state is still true: $current_state"

    read -p "provide authentication: " auth

    if [[ $auth == "farmer" ]]; then
        current_state=false
        echo "you have been locked out"
        break
    else
        echo "stop this already"
    fi
done
