# replacing one output with another.
# text example
# ALL USER PROFILES : MARK WIFI
$content_user = netsh wlan show profiles | select-string "All user" | ForEach-Object{
    $_ -replace ".*:", "" # this will replace everything before the : with nothing removing it.
}

Write-Host $content_user


# DOING THE SAME FUNCTIONALITY AS CUT -D -F IN BASH.
function text_manipulation{
    param(
        [string] $word,
        [string] $delimeter,
        [int] $field
    )

    $text_split = $word.split($delimeter) # will split the text according to the delimeter.

    foreach ($item in $text_split){
        Write-Host "the items in $($word) is $item"
    }
    
    if ($field -ge $text_split.Count){
        Write-Warning "the text-split is too small "
    }else{
        Write-Host "you wanted the value $($text_split[$field])"
    }
}

text_manipulation -word "mark is a genious" -delimeter " " -field 4