# -eq (equal to)
# -ne (not equal to)
# -gt (greater than)
# -lt (less than)
# -ge (greater than or equal to)
# -le (less than or equal to)
# -and
# -or


                # FOR LOOPS
for ($i=1; $i -le 5; $i++) {
    Write-Host "Iteration $($i)"
}
 

                # IF LOOPS
$age = 25

if ($age -ge 18 -and $age -le 22) {
    Write-Host "You are an adult."
} else {
    Write-Host "You are a minor."
}
         
$name1 = "Alice"
$name2 = "Bob"

if ($name1 -gt $name2) {
  Write-Host "Alice comes alphabetically after Bob (strings)"
}


                # WHILE LOOPS
$count = 1

while ($count -le 5) {
    Write-Host "Iteration $count"
    $count++
}
                