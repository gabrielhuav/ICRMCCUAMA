#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corregir automáticamente las comillas problemáticas en documentos LaTeX
que usan babel español.

El problema: babel español interpreta " después de puntuación como comandos especiales
La solución: Reemplazar " con comillas tipográficas españolas usando ``texto''
"""

import os
import re
import glob
from pathlib import Path

def fix_quotes_in_file(filepath):
    """
    Corrige las comillas problemáticas en un archivo LaTeX específico
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Patrón 1: Comillas después de punto, coma, dos puntos, punto y coma + espacio
        # Ejemplo: ". "palabra"" -> ". ``palabra''"
        pattern1 = r'([\.,:;]\s+)"([^"]+)"'
        matches1 = re.findall(pattern1, content)
        for match in matches1:
            old_text = f'{match[0]}"{match[1]}"'
            new_text = f'{match[0]}``{match[1]}\'\''
            content = content.replace(old_text, new_text)
            changes_made.append(f'Cambiado: {old_text} -> {new_text}')
        
        # Patrón 2: Comillas al inicio de línea o después de espacios en blanco
        # Ejemplo: ' "palabra"' -> ' ``palabra'''
        pattern2 = r'(\s+)"([^"]+)"'
        matches2 = re.findall(pattern2, content)
        for match in matches2:
            old_text = f'{match[0]}"{match[1]}"'
            new_text = f'{match[0]}``{match[1]}\'\''
            # Solo reemplazar si no se ha cambiado ya
            if old_text in content:
                content = content.replace(old_text, new_text)
                changes_made.append(f'Cambiado: {old_text} -> {new_text}')
        
        # Patrón 3: Comillas en contextos específicos como tablas o listas
        # Ejemplo: "FALSAS" -> ``FALSAS''
        specific_terms = [
            '"FALSAS"', '"REALES"', '"VERDADERO"', '"FALSO"',
            '"me gusta"', '"limitadas"', '"EXCELENTE"', '"BUENO"', '"ALERTA"',
            '"El Deforma"', '"suficientemente buenas"', '"Buenos Consejeros"', '"Malos Actores"'
        ]
        
        for term in specific_terms:
            if term in content:
                # Extraer el contenido entre comillas
                inner_content = term[1:-1]  # Quitar las comillas externas
                new_term = f'``{inner_content}\'\''
                content = content.replace(term, new_term)
                changes_made.append(f'Cambiado término específico: {term} -> {new_term}')
        
        # Patrón 4: Títulos entre comillas
        # Ejemplo: "Attention Is All You Need" -> ``Attention Is All You Need''
        pattern4 = r'"([A-Z][^"]*)"'
        matches4 = re.findall(pattern4, content)
        for match in matches4:
            old_text = f'"{match}"'
            new_text = f'``{match}\'\''
            # Solo cambiar si no está dentro de una URL o comando LaTeX ya
            if old_text in content and '\\cite{' not in content[content.find(old_text)-10:content.find(old_text)+len(old_text)+10]:
                content = content.replace(old_text, new_text)
                changes_made.append(f'Cambiado título: {old_text} -> {new_text}')
        
        # Solo escribir si hay cambios
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        else:
            return False, []
            
    except Exception as e:
        print(f"Error procesando {filepath}: {e}")
        return False, []

def find_tex_files(directory):
    """
    Encuentra todos los archivos .tex en el directorio y subdirectorios
    """
    tex_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.tex'):
                tex_files.append(os.path.join(root, file))
    return tex_files

def main():
    """
    Función principal que ejecuta la corrección en todos los archivos .tex
    """
    # Directorio base de la tesis
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Buscando archivos .tex en: {base_dir}")
    
    # Encontrar todos los archivos .tex
    tex_files = find_tex_files(base_dir)
    
    if not tex_files:
        print("No se encontraron archivos .tex")
        return
    
    print(f"Encontrados {len(tex_files)} archivos .tex")
    
    total_files_changed = 0
    total_changes = 0
    
    # Procesar cada archivo
    for tex_file in tex_files:
        print(f"\nProcesando: {os.path.relpath(tex_file, base_dir)}")
        
        file_changed, changes = fix_quotes_in_file(tex_file)
        
        if file_changed:
            total_files_changed += 1
            total_changes += len(changes)
            print(f"  ✓ Archivo modificado - {len(changes)} cambios realizados")
            
            # Mostrar los primeros 3 cambios como ejemplo
            for i, change in enumerate(changes[:3]):
                print(f"    {i+1}. {change}")
            
            if len(changes) > 3:
                print(f"    ... y {len(changes) - 3} cambios más")
        else:
            print("  - Sin cambios necesarios")
    
    print(f"\n{'='*60}")
    print(f"RESUMEN:")
    print(f"  Archivos procesados: {len(tex_files)}")
    print(f"  Archivos modificados: {total_files_changed}")
    print(f"  Total de cambios realizados: {total_changes}")
    print(f"{'='*60}")
    
    if total_files_changed > 0:
        print("\n¡Corrección completada! Ahora puedes compilar tu documento LaTeX.")
        print("Recomendación: Ejecuta la compilación para verificar que todo funciona correctamente.")
    else:
        print("\nNo se encontraron comillas problemáticas para corregir.")

if __name__ == "__main__":
    main()
