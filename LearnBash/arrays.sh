#!/bin/bash
fruits=("Apple" "Banana" "Orange")

for fruit in "${fruits[@]}"; do
  echo "Fruit: $fruit"
done


# adding and removing files from list.
files=()
while IFS= read -r file; do
  files+=("$file")
done < <(ls | grep c)

echo "all the files" "${files[@]}" 
echo "${files[0]}"