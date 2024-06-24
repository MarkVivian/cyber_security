#!/bin/bash

# variables are created without spaces.
variable="this is a variable"

echo "$variable"

# if you want to store a command output into a variable we use $()
command=$(history | grep dir)

echo "$command $(history)"

# local variables that can't be used outside a function
name="mary wachira"
local_variables(){
    local name="mark vivian"
    echo "$name"
}
local_variables
echo "$name"


# storing calculations in variables
addition=$((1 + 2))
echo $addition

# getting the length of a string and array. we use the #.
# length of string
random_string="this is just some nonesense"
echo ${#random_string}

# length of array
random_array=("mark" "day" "red")
echo ${#random_array[@]}

# accessing the first and the last element.
random_word="Mark"
first_character_in_word="${random_word:0:1}"
last_character_in_word="${random_word: -1}"


#                           SPECIAL VARIABLES.

# $?
#   - This variable holds the exit status of the last command executed. 
#   - An exit status of 0 usually means the command was successful, while a non-zero value indicates an error.
#       EG.
#           some_command
#           echo $?     # prints the exit status of some_command.


# $1, $2
#   - These variables represent the positional parameters passed to the script or function. 
#   - $1 is the first argument, $2 is the second argument, and so on.
#       EG.
#           echo "first argument: $1"


# $#
#   - This variable holds the number of positional parameters passed to the script or function.
#       EG.
#           echo "Number of arguments: $#"


# $@
#   - This variable holds all the positional parameters passed to the script as seperate words.
#       EG.
#           echo "All arguments: $@"


# $*
#   - Similar to $@, but all the arguments are concatenated into a single word.
#       EG.
#           echo "all arguments : $*"


