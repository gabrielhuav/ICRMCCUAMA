#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para normalizar la terminología de hiperparámetros en documentos LaTeX.

Correcciones que realiza:
1. "Hiper-Parámetros" -> "hiperparámetros"
2. "Hiper-Parámetro" -> "hiperparámetro"
3. "hiper-parámetros" -> "hiperparámetros"
4. "hiper-parámetro" -> "hiperparámetro"
5. Variaciones con mayúsculas y minúsculas
"""

import os
import re
from pathlib import Path

def fix_hyperparameters_in_file(filepath):
    """
    Normaliza las variantes de "hiperparámetros" en un archivo LaTeX específico
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Diccionario de reemplazos: [término_incorrecto] -> término_correcto
        replacements = {
            # Variantes con mayúscula inicial
            'Hiper-Parámetros': 'Hiperparámetros',
            'Hiper-Parámetro': 'Hiperparámetro',
            'Hiper-parámetros': 'Hiperparámetros',
            'Hiper-parámetro': 'Hiperparámetro',
            
            # Variantes en minúsculas
            'hiper-parámetros': 'hiperparámetros',
            'hiper-parámetro': 'hiperparámetro',
            
            # Variantes sin tilde (por si acaso)
            'Hiper-Parametros': 'Hiperparámetros',
            'Hiper-Parametro': 'Hiperparámetro',
            'hiper-parametros': 'hiperparámetros',
            'hiper-parametro': 'hiperparámetro',
            
            # Variantes con espacio en lugar de guion
            'Hiper Parámetros': 'Hiperparámetros',
            'Hiper Parámetro': 'Hiperparámetro',
            'hiper parámetros': 'hiperparámetros',
            'hiper parámetro': 'hiperparámetro',
        }
        
        # Realizar los reemplazos
        for old_term, new_term in replacements.items():
            if old_term in content:
                occurrences = content.count(old_term)
                content = content.replace(old_term, new_term)
                changes_made.append(f'{old_term} -> {new_term} ({occurrences} veces)')
        
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
    print(f"\n{'='*60}")
    print("NORMALIZANDO TERMINOLOGÍA: Hiper-Parámetros -> hiperparámetros")
    print(f"{'='*60}\n")
    
    total_files_changed = 0
    total_changes = 0
    
    # Procesar cada archivo
    for tex_file in tex_files:
        print(f"Procesando: {os.path.relpath(tex_file, base_dir)}")
        
        file_changed, changes = fix_hyperparameters_in_file(tex_file)
        
        if file_changed:
            total_files_changed += 1
            total_changes += len(changes)
            print(f"  ✓ Archivo modificado - {len(changes)} cambios realizados")
            
            # Mostrar todos los cambios
            for i, change in enumerate(changes, 1):
                print(f"    {i}. {change}")
        else:
            print("  - Sin cambios necesarios")
        print()  # Línea en blanco para separación
    
    print(f"{'='*60}")
    print(f"RESUMEN:")
    print(f"  Archivos procesados: {len(tex_files)}")
    print(f"  Archivos modificados: {total_files_changed}")
    print(f"  Total de cambios realizados: {total_changes}")
    print(f"{'='*60}")
    
    if total_files_changed > 0:
        print("\n¡Normalización completada!")
        print("Todos los términos ahora usan la forma correcta: 'hiperparámetros'")
        print("Recomendación: Compila el documento para verificar que todo está correcto.")
    else:
        print("\nNo se encontraron términos para normalizar.")
        print("Tu documento ya usa la terminología correcta.")

if __name__ == "__main__":
    main()