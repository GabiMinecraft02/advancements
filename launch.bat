@echo off
title Lancement du site Advancements - GabiMinecraft02
echo ===========================================
echo     🚀 Lancement du site Advancements
echo ===========================================

:: Vérifie si l'environnement virtuel existe
if exist "venv\Scripts\activate.bat" (
    echo Activation de l'environnement virtuel...
    call venv\Scripts\activate
) else (
    echo Aucun environnement virtuel trouvé. Flask sera lancé globalement.
)

:: Lancer Flask
echo.
echo Démarrage de Flask...
python app.py

:: Vérifie si Flask a crashé
if %errorlevel% neq 0 (
    echo ⚠️ Le serveur Flask s'est arrêté avec une erreur.
    pause
)

:: Garder la fenêtre ouverte
echo.
echo Le serveur Flask est arrêté.
pause
