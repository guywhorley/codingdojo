rem dev-start.cmd
rem Author: Guy Whorley
rem Launch flask-venv, sass listener, app.py

@echo off
cls

rem FLASK - VENV
set VENV_HOME="C:\sw\python27\vdev\flaskp27\Scripts"
echo *** Launching venv: %VENT_HOME%\activate.bat
call %VENV_HOME%\activate.bat
echo ""

rem Launch new window
start cmd /k echo "go change the world!"

rem SASS
echo  *** Watching for .scss changes...
sass --watch ./static/css/scss/styles.scss:./static/css/styles.css
