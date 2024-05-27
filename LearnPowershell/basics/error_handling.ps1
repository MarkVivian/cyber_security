# using try catch error handling.

try{
    [int] $input_data = Read-Host "enter a number: "
    Write-Host "you actually wrote $($input_data)"
}catch{
    Write-Host "why couldn't you just type a number"
}