@echo off
setlocal enabledelayedexpansion
title Entorno04 - GX + Angular Launcher

:MENU
cls
echo =======================================================
echo          ENTORNO 04 - GENEXUS ^& ANGULAR (SLATE ^& SKY)
echo =======================================================
echo.
echo 1. Iniciar Frontend (Angular 18) - http://localhost:4200
echo 2. Compilar APIs GeneXus (MSBuild)
echo 3. Abrir Frontend en el navegador
echo 4. Salir
echo.
set /p opt="Seleccione una opcion: "

if "%opt%"=="1" goto START_FRONTEND
if "%opt%"=="2" goto COMPILE_GX
if "%opt%"=="3" goto OPEN_BROWSER
if "%opt%"=="4" goto EOF

goto MENU

:START_FRONTEND
echo.
echo Iniciando Angular Development Server...
cd Apis_GX_Angular
start cmd /k "npm run start"
cd ..
pause
goto MENU

:COMPILE_GX
echo.
echo Ejecutando MSBuild para compilar las APIs de GeneXus...
cd scripts
start cmd /k "& ""C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe"" Import-NewApis.msbuild"
cd ..
pause
goto MENU

:OPEN_BROWSER
echo.
echo Abriendo aplicacion en el navegador...
start http://localhost:4200
goto MENU

:EOF
exit
