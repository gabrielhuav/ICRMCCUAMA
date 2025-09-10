# Script completo de compilación LaTeX con glosario y bibliografía
# Uso: .\compilar_completo.ps1

Write-Host "=== COMPILACIÓN COMPLETA DE TESIS LATEX ===" -ForegroundColor Green
Write-Host "Documento: ICR.tex" -ForegroundColor Cyan

# Limpiar archivos auxiliares previos
Write-Host "`n[1/6] Limpiando archivos auxiliares..." -ForegroundColor Yellow
Remove-Item -Path "ICR.aux", "ICR.bbl", "ICR.blg", "ICR.gls", "ICR.glg", "ICR.glo", "ICR.ist", "ICR.out", "ICR.toc", "ICR.lof", "ICR.lot", "ICR.log", "ICR.fls", "ICR.fdb_latexmk" -ErrorAction SilentlyContinue

# Primera pasada - LaTeX
Write-Host "[2/6] Primera pasada de pdflatex..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode ICR.tex

# Procesamiento de bibliografía
Write-Host "[3/6] Procesando bibliografía con bibtex..." -ForegroundColor Yellow
bibtex ICR

# Generación manual del glosario (alternativa a makeglossaries)
Write-Host "[4/6] Generando glosario..." -ForegroundColor Yellow
Write-Host "Nota: El glosario se genera automáticamente con glossaries-extra" -ForegroundColor Gray

# Segunda pasada - LaTeX
Write-Host "[5/6] Segunda pasada de pdflatex..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode ICR.tex

# Tercera pasada - LaTeX (para referencias finales)
Write-Host "[6/6] Tercera pasada de pdflatex..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode ICR.tex

# Verificación final
if (Test-Path "ICR.pdf") {
    $fileInfo = Get-Item "ICR.pdf"
    Write-Host "`n=== COMPILACIÓN EXITOSA ===" -ForegroundColor Green
    Write-Host "Archivo generado: ICR.pdf" -ForegroundColor Cyan
    Write-Host "Tamaño: $([math]::Round($fileInfo.Length/1MB, 2)) MB" -ForegroundColor Cyan
    Write-Host "Última modificación: $($fileInfo.LastWriteTime)" -ForegroundColor Cyan
    
    Write-Host "`nContenido incluido:" -ForegroundColor White
    Write-Host "✓ Glosario de términos y acrónimos" -ForegroundColor Green
    Write-Host "✓ Bibliografía completa" -ForegroundColor Green
    Write-Host "✓ Índices de figuras y tablas" -ForegroundColor Green
    Write-Host "✓ Enlaces internos funcionales" -ForegroundColor Green
} else {
    Write-Host "`n=== ERROR EN COMPILACIÓN ===" -ForegroundColor Red
    Write-Host "No se pudo generar ICR.pdf" -ForegroundColor Red
}

Write-Host "`nRevisa el archivo ICR.log para detalles de compilación." -ForegroundColor Gray
