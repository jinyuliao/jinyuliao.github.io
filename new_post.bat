@echo off
set /p PostName="Enter post name: "
tinker --post %PostName% > tmp.txt 2>&1
set /p Output=<tmp.txt 
%Output:~21,-1%
del tmp.txt