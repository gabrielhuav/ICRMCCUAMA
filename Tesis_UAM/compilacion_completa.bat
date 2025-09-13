@echo off
echo ===============================================
echo COMPILACION COMPLETA DE TESIS CON GLOSARIO Y BIBLIOGRAFIA
echo ===============================================
echo.

echo [1/6] Primera compilacion pdflatex...
pdflatex ICR.tex
if errorlevel 1 (
    echo ERROR en primera compilacion pdflatex
    pause
    exit /b 1
)

echo.
echo [2/6] Generando bibliografia con bibtex...
bibtex ICR
if errorlevel 1 (
    echo ERROR en bibtex
    pause
    exit /b 1
)

echo.
echo [3/6] Generando glosario con makeglossaries...
makeglossaries ICR
if errorlevel 1 (
    echo ERROR en makeglossaries - usando metodo alternativo...
    echo Generando glosario manualmente con PowerShell...
    powershell -ExecutionPolicy Bypass -File "generar_glosario.ps1"
    if errorlevel 1 (
        echo ERROR en generacion manual del glosario
        echo Intentando con xindy...
        xindy -L spanish -C utf8 -I xindy -M "ICR" -t "ICR.glg" -o "ICR.gls" "ICR.glo"
        xindy -L spanish -C utf8 -I xindy -M "ICR" -t "ICR.alg" -o "ICR.acr" "ICR.acn"
    )
)

echo.
echo [4/6] Segunda compilacion pdflatex (resolviendo referencias)...
pdflatex ICR.tex

echo.
echo [5/6] Tercera compilacion pdflatex (finalizando enlaces)...
pdflatex ICR.tex

echo.
echo [6/6] Cuarta compilacion pdflatex (asegurando consistencia)...
pdflatex ICR.tex

echo.
echo ===============================================
echo COMPILACION COMPLETA FINALIZADA
echo ===============================================
echo Verifica el archivo ICR.pdf para confirmar que:
echo - El glosario aparece correctamente
echo - Todas las referencias bibliograficas estan resueltas
echo - Los enlaces internos funcionan
echo ===============================================

echo.
echo [LIMPIEZA] Eliminando archivos auxiliares...
powershell -Command "Remove-Item -Path '*.aux', '*.log', '*.toc', '*.lof', '*.lot', '*.out', '*.bbl', '*.blg', '*.fdb_latexmk', '*.fls', '*.glo', '*.gls', '*.glg', '*.ist', '*.xdy' -Force -ErrorAction SilentlyContinue"
powershell -Command "Get-ChildItem -Recurse -Path '.' -Include '*.aux' | Remove-Item -Force -ErrorAction SilentlyContinue"
echo Archivos auxiliares eliminados.
echo.
echo ===============================================
echo PROCESO COMPLETADO Y LIMPIEZA REALIZADA
echo ===============================================
pause
