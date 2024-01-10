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