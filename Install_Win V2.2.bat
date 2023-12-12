:: Start Installation Windows
ECHO on
ECHO "Installation wird begonnen"
:: Erstellen der Ordner Struktur

mkdir %PROGRAMDATA%\Test

:: Navigieren in Ordner Programme

cd %PROGRAMDATA%\Test\

:: Klonen des Repositories

git clone https://github.com/Tobalix/LF08-Monitoring.git
