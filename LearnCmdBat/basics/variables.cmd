@echo off

REM creating a variable.
set stringVariable=Hello Bitch.
set numberVariable=32


REM printing the value of the variable.
echo String : %stringVariable% 
echo number : %numberVariable%


REM there is no boolean in cmd/bat but we use:
set isTrue=1
if %isTrue%==1{
    echo This is true 
} else {
    echo This is false
}
pause 


REM calculating variables
set /a sum=5+3
set /a product=5*3
set /a quotient=15/3
set /a difference=5-3
echo Sum: %sum%
echo Product: %product%
echo Quotient: %quotient%
echo Difference: %difference%
pause


REM Arrays/Lists and looping through them.
set item[0]=Apple & :: simulates an array.
set item[1]=oranges
set item[2]=pineaples

set /a i=0
:loop
if %i% GEQ 3 goto endloop
echo Item %i% : !item[%i%]! & :: the ! isi used in loops and conditional statements where the value might change during execution.
set /a i+=1
goto loop 
:endloop
pause 