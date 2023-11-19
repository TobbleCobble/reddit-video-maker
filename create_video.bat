@echo off
cd /d "%~dp0"
:start
set choice=
set /p choice=type S for a shortform video, type L for a longform video.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto short
if '%choice%'=='l' goto long
ECHO "%choice%" is not valid, try again
ECHO.
goto start
:short
Echo Creating shortform video...
python3 askreddit/main.py
goto end
:long
Echo Creating longform video...
python3 longForm/main.py
goto end
:end
pause