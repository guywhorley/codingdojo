@echo off
cls
echo *************************************
echo ** WATCHING SASS STYLESHEETS...    **
echo *************************************
sass --watch _styles.scss:styles.css
