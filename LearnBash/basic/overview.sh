#!/bin/bash

#               IF STATEMENTS
age=10
if [[ age -eq 10 ]];  # the -eq means equal to .
then
    echo "your age $age is correct."
else    
    echo "your age is too low $age"
fi


#               FOR LOOP
for i in {1..10};do
    echo "for loop iterate $i"
done


#               WHILE LOOP
count=1

while [ $count -le 5 ]; do
  echo "while loop Iteration $count"
  ((count++))
done
