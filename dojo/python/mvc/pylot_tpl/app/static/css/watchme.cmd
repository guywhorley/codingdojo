@echo off
cls
echo *************************************
echo ** WATCHING SASS STYLESHEETS...    **
echo *************************************
sass --watch ./scss/styles.scss:styles.css
