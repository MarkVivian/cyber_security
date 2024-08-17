#!/bin/bash

# there are two methods of getting user input

#           METHOD 1
echo "what is your name? " 
# you can add -n if you want the user input to be on the same line as the text provided.
# echo -n "what is your name? "
read name
echo "your name is $name"


#             METHOD 2

read -p "what is your name  " name1

echo "your name is $name1"


#           METHOD 3
# we can also pass a value while calling the script
value="$1" # the 1 takes the 1 value passed to the script so if you wanted the second passed we use $2 so on.
echo "the value is $value"
# EG.  
#       ./scripts.sh value


#               PASSING INPUT FROM SCRIPT CALL.
# If your script uses read to get user input, you can use a here document.
#  EG.
#      ./gitPush.sh <<EOF
#      pushing something random
#      EOF


#             GETTING INPUT FROM SCRIPT CALL.
# $#: The number of positional parameters passed to the script.
# $0: The name of the script.
# $1, $2, ...: The first, second, etc., positional parameters.
# $@: All positional parameters as separate words.
# $*: All positional parameters as a single word.
# $?: The exit status of the most recent command.
    # Exit status values.
        # 0: Successful execution.
        # 1- 255: The command failed. The exact value can vary depending on the command.
        # Example 1: Successful command
        ls
        echo $?  # Outputs 0 if `ls` was successful

        # Example 2: Failed command
        ls nonexistentfile
        echo $?  # Outputs a non-zero value (e.g., 2) because `ls` failed



# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 num1 [num2 ...]"
    exit 1
fi

# Iterate over all arguments
echo "You provided $# arguments:"
for arg in "$@"; 
do
    echo "$arg"
done
