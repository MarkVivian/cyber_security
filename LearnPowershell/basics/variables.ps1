# normal variable creation.
# we declare variables using the $ sign.
$name = "john"

# the $ allows us to also call the variable inside a string.
Write-Host "your name is $($name)"

# if you wish to store a boolean we use the command.
$state = $true
Write-Host "the current state is $($state)"

# variables with parameters 
$currentDate = Get-Date -Format "yyyy-MM-dd"
Write-Host "Today is $($currentDate)"

# performing action on variables.
# putting two strings next to each other
$first_name = "Mark"
$last_name = "Vivian"

Write-Host "$first_name $last_name"

# performing calculations
$number1 = 23
$number2 = 45

$sum = 12 + 42
$number_sum = $number1 + $number2
Write-Host "the value of sum is $sum"
Write-Host "number $($number1) and $($number2) added together form $($number_sum)"

# we can also store outputs from a command.
$store_processes = Get-Process
foreach ($item in $store_processes){
    Write-Host "the process is $($item)"
}


# the $_ variable
# used when in sub item like:
$profiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object {
    # Extract profile names by removing the leading text
    $_ -replace ".*: ", ""
    # the $_ represents each output.
}


# getting the length of a string and an array.
$myArray = @("apple", "banana", "cherry")

# Get the number of elements using the .Count property
for ($i = 0; $i -lt $myArray.Count; $i++) {
  Write-Host "Item at index $i : $($myArray[$i])"
}

$myString = "This is a string"

# Get the length using the .Length property
for ($i = 0; $i -lt $myString.Length; $i++) {
  Write-Host "Character at index $i : $($myString[$i])"
}



