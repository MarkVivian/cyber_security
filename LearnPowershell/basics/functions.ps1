# normal function without any parameters.
function get_currentDate{
    Write-Host (Get-Date)
}

get_currentDate


# functions with parameters.
function get_username{
    param(
        [string] $name
    )
    Write-Host "your name is $($name)"
}

get_username "Mark Vivian"

function add_numbers{
    param(
        [int] $num1,
        [int] $num2
    )
    $sum = $num1 + $num2
    Write-Host "the sum of $($num1) and $($num2) is $($sum)"
}

add_numbers 3 5
# or 
add_numbers -num1 30 -num2 90


# functions with return values.
function rectangle_area{
    param(
        [int] $length,
        [int] $width
    )
    $area = $length * $width
    Write-Output $area
    # similar to 
    # return $area
}

$rectangle_area = rectangle_area 10 20
Write-Host $rectangle_area