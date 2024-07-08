# we can also pass input when calling the script.
param(
    [string] $user_name
)

Write-Host "the nigga who run me is $user_name"


# getting user input inside the script.
$name = Read-Host "Enter your name "
Write-Host "your name is $name"

# giving data type to an output
[int] $user_data = Read-Host "enter a number between 1 and 10"
Write-Host "the user data is $($user_data)"
if ($user_data -ge 11){
    Write-Host "you don't know how to follow instructions"
}else{
    Write-Host "i thought you would be a free thinker"
}

# to skip line we use:
Write-Host "this is on line `n this is on line 2"