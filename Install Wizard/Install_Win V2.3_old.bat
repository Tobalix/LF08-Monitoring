:: Start Installation Windows

@ECHO "Installation wird begonnen"

:: Erstellen der Ordner Struktur

:: mkdir %PROGRAMDATA%\Test

:: Navigieren in Ordner Programme

@ECHO Navigiere zu Programme...
cd %PROGRAMDATA%\Test\

timeout /t 20

:: Klonen des Repositories

::git clone https://github.com/Tobalix/LF08-Monitoring.git

:: Personalisierte Installation des Monitoringtools
:: @ECHO off


@ECHO "Im folgenden Abschnitt koennen Sie die Installation personalisieren. Druecken Sie y um fortzufahren."

set /P Eingabe= "y"

@ECHO "Test"

