#!/bin/bash

# basic function.
function hello(){
    echo "this is a function"
}

another(){
    echo "another type of function"
}

hello
another

# function with a parameter.
parameter(){
    name="$1"
    echo "the parameter passed is $name"
}

read -p "enter a parameter " content
parameter "$content"

# function that returns value
sum(){
    local value1="$1"
    local value2="$2"

    local sums=$((value1 + value2))
    echo $sums
}

results=$(sum 1 2)

echo "the results are $results"