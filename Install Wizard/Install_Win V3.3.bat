@echo off
setlocal enabledelayedexpansion

@ECHO Installation wird begonnen

REM Benutzer nach dem Installationsverzeichnis fragen
set /p "installFolder=Bitte geben Sie das Installationsverzeichnis ein: "

set "installFolder=!installFolder!"

REM Überprüfen, ob der Installationsordner existiert, andernfalls erstellen
if not exist "!installFolder!" (
    echo Der Installationsordner "!installFolder!" existiert nicht. Er wird erstellt.
    mkdir "!installFolder!"

) else (
    REM Installationsordner existiert - lösche alle vorhandenen Elemente im Ordner
    echo Der Installationsordner "!installFolder!" existiert bereits. Alle vorhandenen Elemente werden gelöscht.
    rd /s /q "!installFolder!"
    mkdir "!installFolder!"
)

REM Wechseln in das Installationsverzeichnis
cd /d "!installFolder!"

REM Klonen des Repositories und Wechseln in den gewünschten Branch
git clone --single-branch --branch "Install" "https://github.com/Tobalix/LF08-Monitoring.git" .

REM Prüfen, ob der Benutzer die Standardinstallation beibehalten möchte
set /p "keepDefault=Beibehalten der Standardinstallation? (J/N): "
if /i "!keepDefault!"=="J" (
    echo Installation ist abgeschlossen.
	pause
goto :Mail
) else if /i "!keepDefault!"=="N" (
    goto :customizeInstallation
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :end
)

REM Modul "CPU" installieren
:installCPU
set /p "installCPU=Modul 'CPU' installieren? (J/N): "
if /i "!installCPU!"=="J" (
    echo [Monitor CPU] >> config.ini
    echo CPU_LOGGING = True >> config.ini
    REM Hier weitere CPU-Optionen einfügen
) else if /i "!installCPU!"=="N" (
    echo [Monitor CPU] >> config.ini
    echo CPU_LOGGING = False >> config.ini
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :installCPU
)

REM Modul "RAM" installieren
:installRAM
set /p "installRAM=Modul 'RAM' installieren? (J/N): "
if /i "!installRAM!"=="J" (
    echo [Monitor RAM] >> config.ini
    echo RAM_LOGGING = True >> config.ini
    REM Hier weitere RAM-Optionen einfügen
) else if /i "!installRAM!"=="N" (
    echo [Monitor RAM] >> config.ini
    echo RAM_LOGGING = False >> config.ini
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :installRAM
)

REM Modul "Disk" installieren
:installDisk
set /p "installDisk=Modul 'Disk' installieren? (J/N): "
if /i "!installDisk!"=="J" (
    echo [Monitor Disk] >> config.ini
    echo DISK_LOGGING = True >> config.ini
    REM Hier weitere Disk-Optionen einfügen
) else if /i "!installDisk!"=="N" (
    echo [Monitor Disk] >> config.ini
    echo DISK_LOGGING = False >> config.ini
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :installDisk
)

REM Modul "Temp" installieren
:installTemp
set /p "installTemp=Modul 'Temp' installieren? (J/N): "
if /i "!installTemp!"=="J" (
    echo [Monitor Temp] >> config.ini
    echo TEMP_LOGGING = True >> config.ini
    REM Hier weitere Temp-Optionen einfügen
) else if /i "!installTemp!"=="N" (
    echo [Monitor Temp] >> config.ini
    echo TEMP_LOGGING = False >> config.ini
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :installTemp
)

REM Modul "Logon" installieren
:installLogon
set /p "installLogon=Modul 'Logon' installieren? (J/N): "
if /i "!installLogon!"=="J" (
    echo [Monitor Logon] >> config.ini
    echo LOGON_LOGGING = True >> config.ini
    REM Hier weitere Logon-Optionen einfügen
) else if /i "!installLogon!"=="N" (
    echo [Monitor Logon] >> config.ini
    echo LOGON_LOGGING = False >> config.ini
) else (
    echo Ungültige Eingabe. Bitte geben Sie 'J' für Ja oder 'N' für Nein ein.
    goto :installLogon
)

echo.
echo Installation abgeschlossen.

:Mail
REM Hartcodierte Werte
set "configFile=config.ini"

REM Überprüfen, ob die Konfigurationsdatei vorhanden ist
if not exist "!configFile!" (
    echo Die Konfigurationsdatei "!configFile!" wurde nicht gefunden.
    goto :end
)

REM Eingabeaufforderungen für SMTP-Konfiguration
@ECHO Aktuelle Sender-E-Mail-Adresse aus der Konfigurationsdatei:
for /f "tokens=*" %%a in ('type "!configFile!" ^| find "EMAIL_SENDER"') do (
    set "senderAddress=%%a"
    echo !senderAddress:* =!
)
echo.

@ECHO Bitte geben Sie Ihre neue Empfänger-E-Mail-Adresse ein:
set /p "receiverAddress="

@ECHO Bitte geben Sie Ihr Passwort ein (die Eingabe wird NICHT verdeckt):
set /p "password="
echo.

REM Bearbeiten der Konfigurationsdatei
(for /f "tokens=*" %%a in ('type "!configFile!"') do (
    set "line=%%a"

    REM Überprüfen, ob die Zeile den SMTP-Teil betrifft
    if "!line:~0,6!"=="[SMTP]" (
        set "editSMTP=true"
        echo [SMTP]
        echo !senderAddress!
        echo EMAIL_RECEIVER = !receiverAddress!
        echo EMAIL_PASSWORD = !password!
    ) else if defined editSMTP (
        REM SMTP-Teil wurde bearbeitet, überspringe den Rest
        set "editSMTP=false"
    ) else (
        REM Die Zeile betrifft keinen SMTP-Teil, daher unverändert übernehmen
        echo !line!
    )
)) > "temp_config.ini"

REM Umbenennen der temporären Konfigurationsdatei
move /y "temp_config.ini" "!configFile!" > nul

pip install psutil
pip install wmi

echo.
echo SMTP-Konfiguration wurde aktualisiert: "!configFile!"
pause
goto :eof

:end
endlocal
