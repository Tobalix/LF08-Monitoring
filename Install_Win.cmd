::
::
::


:: Start Installation Windows
ECHO on
ECHO "Installation wird begonnen"
:: Erstelen Orderner Struktur
cd %windir%
cd ../
cd Program Files

MD ITECH_MONITOR
cd ITECH_MONITOR
MD LOG
MD SOURCE
MD CONFIG

:: Installirt Programm von Git
