# we use the @() to create lists/arrays.
# ARRAY
$names = @("mark", "taby", "lucy")

# array of numbers.
# the range operator .. creates a range of numbers.
$numbers = @(1..10)
# IT MUST ALWAYS BE TWO DOTS.
# we can also create the array in reverse.
$numbers = @(10..1)

foreach ($name in $names) {
    Write-Host "hello $name"
}

# we can also create hash tables.
$hashtable = @{
    name = "mark"
    age = 10
}
# we can also use PSCustomObject to create hash tables.
$hashtable = [PSCustomObject]@{
    name = "mark"
    age = 10
}
# we use PSCustomObject to create objects that are easy to :
# 1. export to CSV
# 2. sort 
# 3. filter
# 4. pipeline
# see file in using command to learn more

# accessing values in an array and hash table.
Write-Host "the user $($hashtable.name) is of age $($hashtable.age)"

Write-Host "the name at position 1 is $($names[1]) and at position -1 is $($names[-1])"


# adding and removing items from an array.
# adding single value
$names += "edward"
Write-Host "we have added the name edward to $($names)"

# adding multiple values
$names += ("alern", "mugo")
Write-Host "added multiple hosts alern and mugo to $($names)"

# removing based on a condition
$names = $names | Where-Object {$_ -ne "mark"}
Write-Host "i have removed mark from $($names)"

# we can get the index of an item in the array.
$index_of_lucy = $names.IndexOf("lucy")
Write-Host "the index of lucy is $($index_of_lucy)"