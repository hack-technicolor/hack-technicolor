@echo off
set path=%path%;C:\Program Files\GTK3-Runtime Win64\bin
rem Default Install ie 'Just Me', default folder, Don't add to path or register as system python
set AnacondaPath=%USERPROFILE%\Anaconda3
call %AnacondaPath%\Scripts\activate.bat %AnacondaPath%
mkdocs serve
