rmdir /s /q build
rmdir /s /q dist
C:\Python27\python.exe setup.py py2exe
"C:\Program Files (x86)\NSIS\makeNSIS.exe" zlosnica.nsi
pause
