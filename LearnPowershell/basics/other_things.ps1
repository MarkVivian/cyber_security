# exiting loops and scripts.
$user_input = Read-Host "do not type exit"

if ($user_input -eq "exit"){
    exit
    # this will exit the script itself.
}

for ($i = 0; $i -lt 10; $i++) {
    if ($i -eq 5) {
      exit;  # Only exit this iteration if i is 5
    }
    # Do something with the current value of i
    Write-Host "the value of i is $i"
}



# writing warning 
function text_manipulation{
    param(
        [string] $word,
        [string] $delimeter,
        [int] $field
    )
    $text_split = $word.split($delimeter) # will split the text according to the delimeter.
    
    if ($field -ge $text_split.Count){
        Write-Warning "the text-split is too small " # will be a different color to the rest .
    }else{
        Write-Host "you wanted the value $($text_split[$field])"
    }
}


# skipping lines like \n in python
Write-Host "we skip lines using `n look in the code to see it"