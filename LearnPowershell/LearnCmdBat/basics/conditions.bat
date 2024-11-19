@echo off 

REM COMPARISON OPERATORS
:: -eq (equal to) : `==`
:: -ne (not equal to) : `!=`
:: -gt (greater than) : `GTR`
:: -lt (less than) : `LSS`
:: -ge (greater than or equal to) : `GEQ`
:: -le (less than or equal to) : `LEQ`


REM LOGICAL OPERATORS.
:: -and : `&&`
:: -or : `||`
:: -not : `!`


REM IF LOOP
:: --------------
set /a num1=5
set /a num2=10

if %num1% == %num2% (
    echo num1 is equal to num2
) else (
    echo num1 is not equal to num2
)

if %num1% GTR %num2% (
    echo num1 is greater than num2
) else (
    echo num1 is not greater than num2
)
pause 


set /a numb1=5
set /a numb2=10

if %numb1% LSS %numb2% && %numb2% GTR 7 (
    echo Both conditions are true
) else (
    echo One or both conditions are false
)

pause


set name=marking

if "%name%"=="marking"(
    echo the loop is working.
) else (
    echo The loop is not working.
)


REM     WHILE LOOP
::   ------------------
set /a counter=1

:loop & :: This is a label marking the start of the loop
if %counter% LEQ 5 (    & :: this checks if the counter variable is less than or equal to 5.
    echo Counter is %counter%   
    set /a counter=%counter%+1 & :: This increments the counter by 1.
    goto loop  & :: This command returns control to the :loop label, effectively creating a loop.
)

echo Done!
pause
:: The script continues to loop until the counter exceeds 5.



REM     FOR LOOPS.
::   -------------------
::  Iterate over a range of numbers using the `/L` switch.
REM   EG.
    ::for /L %%variable in (start,step,end) do (
    ::  command
    :: )
        :: %%variable is the loop variable.
        :: start is the initial value.
        :: step is the increment (or decrement).
        :: end is the final value.

@echo off
for /L %%i in (1,1,5) do (
    echo Iteration %%i
)
pause
:: The loop starts with %%i equal to 1, increments by 1, and stops when %%i is greater than 5.


:: Looping through an array of values.
@echo off
for %%color in (red green blue) do ( & :: The loop iterates over each color in the list.
    echo The color is %%color
)
pause


:: looping over files in a directory.
    ::EG
        :: for %%file in (directory\*.extension) do {
        ::  echo Found file : %%file
        ::}
for %%file in (*.bat) do (
    echo Found file: %%file
)
pause
