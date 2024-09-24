#!/bin/bash
# how to create an array and view its members.
fruits=("Apple" "Banana" "Orange")

for fruit in "${fruits[@]}"; do
  echo "Fruit: $fruit"
done

# adding and removing items from an array
# adding an item
fruits+=(" mark")
echo "the items left are ${fruits[@]}"

# removing an item
new_array=()
for item in ${fruits[@]}; do
  if [[ $item != "Apple" ]]; then
    new_array+=($item)
  fi
done
echo "removed Apple from ${new_array[@]}"

  # OR

unset fruits[2] # removes the item at the 2nd index.
echo "${fruits[@]}"

# adding and removing files from list.
files=()
while IFS= read -r file; do
  files+=("$file")
done < <(ls | grep c)

echo "all the files" "${files[@]}" 
echo "${files[0]}"


#         USING DECLARE.
#     =========================
