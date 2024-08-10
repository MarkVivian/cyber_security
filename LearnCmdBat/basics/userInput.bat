@echo off
REM METHOD  1:
set /p name=Enter your name ? & :: Prompts the user to enter their name and stores the input in the variable `name`.
set /p age=Enter your age ?
echo Hello %name%, how are you doing at the age of %age%?
pause & :: waits for the user to press a key before closing the command prompt window.

REM METHOD 2:
:: the %1 represents the first input, %2 represents the second e.t.c.
echo %1
if "%1"=="testing" {
    echo Please provide a name as an argument when running this script.
    exit /b 
} else {
    echo you provided the input %1
}