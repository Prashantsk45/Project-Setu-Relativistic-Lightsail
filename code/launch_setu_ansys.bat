@echo off
title Launch Project Setu ANSYS
set "ANSYS_LOCK=OFF"
if not exist "D:\CFD\Project Setu\ansys_run" mkdir "D:\CFD\Project Setu\ansys_run"
cd /d "D:\CFD\Project Setu\ansys_run"
start "" "C:\Program Files\ANSYS Inc\v252\ansys\bin\winx64\ANSYS252.exe" -g -dir "D:\CFD\Project Setu\ansys_run" -j "setu"
