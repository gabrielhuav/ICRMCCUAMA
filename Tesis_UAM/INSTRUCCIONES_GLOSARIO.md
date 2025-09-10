# Instrucciones para Compilar la Tesis con Glosario

## Pasos para generar correctamente el glosario en LaTeX:

### Compilación Automática (Recomendado)
1. Ejecutar el archivo `compilar_tesis.bat` en Windows
2. O seguir los pasos manuales a continuación

### Compilación Manual
Ejecutar los siguientes comandos en orden desde la carpeta raíz del proyecto:

```bash
# Paso 1: Primera compilación
pdflatex ICR.tex

# Paso 2: Generar archivos de glosario
makeglossaries ICR

# Paso 3: Segunda compilación (incluye el glosario)
pdflatex ICR.tex

# Paso 4: Procesar bibliografía
bibtex ICR

# Paso 5: Tercera compilación (incluye referencias)
pdflatex ICR.tex

# Paso 6: Compilación final (resuelve todas las referencias cruzadas)
pdflatex ICR.tex
```

## Verificación del Glosario

Después de la compilación, el documento debe incluir:

1. **Lista de Acrónimos y Abreviaciones** - Contiene ICR, PLN, NLP, BoW, TF-IDF, BERT, GPT, etc.
2. **Glosario de Términos** - Contiene definiciones detalladas de conceptos técnicos

## Resolución de Problemas

Si el glosario no aparece:
1. Verificar que `makeglossaries` está instalado
2. Revisar que no hay errores en los archivos `.glo` y `.glg`
3. Asegurar que `\glsaddall` está al final de `Glosario/Glosario.tex`
4. Verificar que hay referencias a términos del glosario en el texto (usando `\gls{}` o `\glspl{}`)

## Archivos Generados

Los siguientes archivos se generan durante la compilación del glosario:
- `ICR.glo` - Lista de términos del glosario
- `ICR.gls` - Glosario procesado
- `ICR.glg` - Log de makeglossaries
- `ICR.ist` - Archivo de estilo para el glosario
