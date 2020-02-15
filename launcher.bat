@echo off
echo normal mode
color 2F
mode con:cols=60 lines=30
cls

CALL :header

echo ^
                                                            ^
               Do you want to run the game?                 ^
                        [yes/no]

set /p id=": "

if %id%==yes (
	echo neat
	start python3.8\python.exe __main__.py
) else if %id%==no (
	exit
) else (
	echo ERROR: Please answer 'yes' or 'no'
	pause
	launcher.bat
)

EXIT /B %ERRORLEVEL%

:: Functions

:header
echo ^
============================================================^
                                                            ^
                    Set-Up for programs                     ^
                                                            ^
============================================================
EXIT /B 0
