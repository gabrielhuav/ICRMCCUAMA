# ORDEN DE COMPILACION PARA TESIS CON GLOSARIO Y BIBLIOGRAFIA
# Ejecutar estos comandos en orden desde PowerShell o CMD

# 1. Primera compilación
pdflatex ICR.tex

# 2. Procesar bibliografía
bibtex ICR

# 3. Procesar glosario
makeglossaries ICR

# 4. Segunda compilación (integra bibliografía y glosario)
pdflatex ICR.tex

# 5. Tercera compilación (resuelve enlaces cruzados)
pdflatex ICR.tex

# 6. Cuarta compilación (finaliza todo)
pdflatex ICR.tex

# NOTA: Si makeglossaries falla, usar método alternativo:
# xindy -L spanish -C utf8 -I xindy -M "ICR" -t "ICR.glg" -o "ICR.gls" "ICR.glo"
# xindy -L spanish -C utf8 -I xindy -M "ICR" -t "ICR.alg" -o "ICR.acr" "ICR.acn"
