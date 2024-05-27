# we use the @() to create lists/arrays.
# ARRAY
$names = @("mark", "taby", "lucy")

foreach ($name in $names) {
    Write-Host "hello $name"
}

# we can also create hash tables.
$hashtable = @{
    name = "mark"
    age = 10
}

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