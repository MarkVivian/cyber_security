#!/bin/bash

echo "what kind of file are you extracting: "
echo "1) tar.xz"
echo "2) tar.gz"
echo "3) .zip"
echo "4) install .deb file"
read -p "choose one of the following: " type_name

type_name(){
    case "$type_name" in
        "1")
            echo ".tar.xz"
            ;;
        "2")
            echo ".tar.gz"
            ;;
        "3")
            echo ".zip"
            ;;
        "4")
            echo ".deb"
            ;;
        *)
            echo "unknown "
            ;;
    esac
}

name_type=$(type_name)

# this will list all the files according to the type chossen
file_choose_helper(){
    local files=() # array in bash

    # this will loop over all the files in the current directory.
    while IFP= read -r file; do
        files+=("$file")
    done < <(ls | grep "$name_type")
    
    # Check if any files were found
    if [ ${#files[@]} -eq 0 ]; then
    echo "No files of type $name_type found."
    return 1
    fi

    # Display the list of files and prompt the user to choose
    echo "Files of type $name_type"
    for ((i = 0; i < ${#files[@]}; i++)); do
    echo "$i   ${files[i]}"
    done

    # Prompt the user to choose a file
    read -p "Enter the number of the file to select: " file_number

    # Check if the input is a valid number
    if ! [[ "$file_number" =~ ^[0-9]+$ ]] || [ "$file_number" -ge ${#files[@]} ]; then
    echo "Invalid input. Please enter a valid number."
    return 1
    fi

    selected_file="${files[file_number]}"
    echo "$selected_file"
}

file_choose_helper

echo "$selected_file"