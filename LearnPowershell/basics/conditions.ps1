# -eq (equal to)
# -ne (not equal to)
# -gt (greater than)
# -lt (less than)
# -ge (greater than or equal to)
# -le (less than or equal to)
# -and
# -or

#   EG.
#   -and

#*****************FILE OPERATIONS.******************
# Check if File Exists:
#   EG.
#       Test-Path $filePath

# Check if File is Readable:
#   EG.
#       (Get-Item $filePath).IsReadOnly -eq $false

# Check if File is Writable:
#   EG.
#       (Get-Item $filePath).IsReadOnly -eq $false

# Check if File is Executable:
#   EG.
#       (Get-Item $filePath).Attributes -band [System.IO.FileAttributes]::Normal 
#               -OR
#       (Get-Item $filePath).Attributes -band [System.IO.FileAttributes]::Archive

# Check if File is a Directory:
#   EG.
#        Test-Path $directoryPath -PathType Container

# Check if File is not a Directory:
#   EG.
#         Test-Path $filePath -PathType Leaf

# Check if File is not Empty:
#   EG.
#         (Get-Item $filePath).length -gt 0

# Check if File is a Symbolic Link:
#   EG.
#         (Get-Item $filePath).Attributes -band [System.IO.FileAttributes]::ReparsePoint

# Negate a Command:
#   EG.
#         -not (Test-Path $filePath)

# Check if File is a Block Special File (PowerShell doesn't directly support block special files):
#   EG.
#         # Not directly supported in PowerShell

# Check if File is a Character Special File (PowerShell doesn't directly support character special files):
#   EG.
#         # Not directly supported in PowerShell

# Check if File is Set-Group-ID:
#   EG.
#         # Not directly supported in PowerShell

# Check if File is Owned by the Effective Group ID:
#   EG.
#         (Get-Item $filePath).GetAccessControl().Owner -eq (Get-ADUser $env:USERNAME).SID

# Check if File has the Sticky Bit Set:
#   EG.
#         # Not directly supported in PowerShell

# Check if Two Files Refer to the Same Device and Inode Numbers:
#   EG.
#         (Get-Item $file1).PSIsContainer -eq (Get-Item $file2).PSIsContainer

# Check if File is Older Than Another File:
#   EG.
#         (Get-Item $file1).LastWriteTime -lt (Get-Item $file2).LastWriteTime

# Check if File is Newer Than Another File:
#   EG.
#         (Get-Item $file1).LastWriteTime -gt (Get-Item $file2).LastWriteTime

# Check if File has Set-User-ID Bit Set:
#   EG.
#         # Not directly supported in PowerShell

# Check if File Descriptor is Associated with a Terminal:
#   EG.
#         # Not directly supported in PowerShell

# Check if File is a Socket:
#   EG.
#         # Not directly supported in PowerShell

# Check if File Exists and has a Size Greater than Zero:
#   EG.
#         (Get-Item $filePath).length -gt 0

# Check if File is a Named Pipe (FIFO):
#   EG.
#         # Not directly supported in PowerShell

# Check if File is Owned by the Effective User ID:
#   EG.
#         (Get-Item $filePath).GetAccessControl().Owner -eq (Get-WmiObject Win32_Account -Filter "Name='$env:USERNAME'").SID

# Check if File has Been Modified Since Last Read:
#   EG.
#         (Get-Item $filePath).LastWriteTime -gt (Get-Item $filePath).LastAccessTime


                # FOR LOOPS
for ($i=1; $i -le 5; $i++) {
    Write-Host "Iteration $($i)"
}

$values = @("mark", "vivian", "wachira")

foreach ($item in $values){
    Write-Host "the items in the list is $($item)"
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


#*********************SWITCH STATEMENTS.**************
# switch supports multiple conditions for a single case by separating them with commas.
# Wildcard patterns (*, ?) and regular expressions can be used in the switch statement.
# The default case is optional and is executed if no other cases match.

#   basic structure.
# switch (test-expression) {
#     pattern1 { statements1 }
#     pattern2 { statements2 }
#     default { statements3 }
# }


$day = "Tuesday"

switch ($day) {
    "Monday" {
        Write-Host "Today is Monday"
    }
    "Tuesday" {
        Write-Host "Today is Tuesday"
    }
    "Wednesday" {
        Write-Host "Today is Wednesday"
    }
    default {
        Write-Host "Today is another day"
    }
}

# OR
$inputS = "Hello"

switch -Wildcard ($inputS) {
    "H*" { Write-Host "Starts with H" }
    "G*" { Write-Host "Starts with G" }
    "*o" { Write-Host "Ends with o" }
    default { Write-Host "No match found" }
}

                