::
::
::


:: Start Installation Windows
ECHO on
ECHO "Installation wird begonnen"
:: Erstellen der Ordner Struktur
cd %windir%
cd ../
cd Program Files

MD ITECH_MONITOR
cd ITECH_MONITOR
MD LOG
MD SOURCE
MD CONFIG

:: Installiert Programm von Git
