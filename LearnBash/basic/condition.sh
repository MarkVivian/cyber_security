#!/bin/bash

# ***********************IF LOOPS **************************************
# -------------CHECK IF FILE --------------
# -b filename - Block special file
# -c filename - Special character file
# -d directoryname - Check for directory Existence
# -e filename - Check for file existence, regardless of type (node, directory, socket, symlink, etc.)
# -f filename - Check for regular file existence not a directory
# -G filename - Check if file exists and is owned by effective group ID
# -G filename set-group-id - True if file exists and is set-group-id
# -k filename - Sticky bit
# -L filename - Symbolic link
# -O filename - True if file exists and is owned by the effective user id
# -r filename - Check if file is a readable
# -S filename - Check if file is socket
# -s filename - Check if file is nonzero size
# -u filename - Check if file set-user-id bit is set
# -w filename - Check if file is writable
# -x filename - Check if file is executable
# -e, -f : checks if file exists.
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
# ^[0-9]+$ : check if a value is a digit

# Check if both are integers
after=10
wantedBy="hello world"
if ! [[ "$after" =~ ^[0-9]+$ ]] || ! [[ "$wantedBy" =~ ^[0-9]+$ ]]; then
    echo "Error: Both after and wantedBy must be integers."
    exit 1
else
    echo "both are numbers"
fi

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

if [[ $value -gt 10 ]] || [[ $value -lt 0 ]]; then
    echo "you can't follow instructions, can you? "
else
    echo "sometimes rebel"
fi

if [[ $value -gt 10 ]] && [[ $value -lt 0 ]]; then
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

# check if the current user is root.
#   - The root user has an EUID of 0. You can use $EUID to check if a script is being run as root.
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi
    # "$EUID" -ne 0 checks if the EUID is not equal to 0 (not root).
    # If the user is not root, it prints a message and exits.


# Feature	            [ ] (test)	            [[ ]] (Bash built-in)
# Portability	    POSIX-compliant	           Not POSIX-compliant
# Variable Quoting	Required for safety	        Not required
# Logical Operators	    Use -a, -o	                Use &&, `
# Pattern Matching	        No	                      Yes
# Globbing	        Yes (filename expansion)	No (pattern matching instead)

# ************************* FOR LOOP ****************************
for (( i=0; i<5; i++)); do
    echo "iteration : $i"
done

items=("mark" "elephant" "lion");

for item in ${items[@]}; do
    echo "items at ${item}"
done

# iterating through a range of numbers.
for i in {0..5}; do
    echo "number $i"
done

for i in $(seq 1 5); do
    echo "seq number $i"
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


#*********************SWITCH STATEMENTS.**************

#   BASIC STRUCTURE

# case "$variable" in
#     pattern1) statements1 ;;
#     pattern2) statements2 ;;
#     *) statements3 ;; # default case
# esac

day="Tuesday"

case "$day" in
    "Monday")
        echo "Today is Monday"
        ;;
    "Tuesday")
        echo "Today is Tuesday"
        ;;
    "Wednesday")
        echo "Today is Wednesday" 
        ;;
    *)  
        echo "Today is another day"
        ;;
esac

input="B"

case $input in
    "A")
        echo "Value is A"
        ;;
    "B")
        echo "Value is B"
        ;;
    "C")
        echo "Value is C"
        ;;
    *)
        echo "Value is not A, B, or C"
        ;;
esac
