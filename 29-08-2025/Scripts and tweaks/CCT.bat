@echo off
:: Check for administrative privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Run PowerShell command
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm 'https://christitus.com/win' | iex"
