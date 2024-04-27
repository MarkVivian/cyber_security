function Greet {
    param (
        [string]$person
    )
    Write-Host "Hello, $person!"
}

Greet -person "Alice"
