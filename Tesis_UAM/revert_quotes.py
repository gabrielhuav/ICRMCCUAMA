#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para revertir las comillas guillemot y aplicar comillas tipográficas españolas correctas
"""

import os
import re

def fix_guillemot_quotes(filepath):
    """
    Revierte comillas guillemot y aplica comillas tipográficas españolas
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Patrón para encontrar \guillemotleft{contenido}\guillemotright{}
        pattern = r'\\guillemotleft\{([^}]+)\}\\guillemotright\{\}'
        matches = re.findall(pattern, content)
        
        for match in matches:
            old_text = f'\\guillemotleft{{{match}}}\\guillemotright{{}}'
            new_text = f'``{match}\'\''
            content = content.replace(old_text, new_text)
            changes_made.append(f'Revertido: {old_text} -> {new_text}')
        
        # También manejar casos donde ya existe guillemot y reemplazar con comillas tipográficas
        # Buscar patrones como \guillemotleft y \guillemotright por separado
        content = re.sub(r'\\guillemotleft\{\}', '``', content)
        content = re.sub(r'\\guillemotright\{\}', "''", content)
        
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
    Función principal
    """
    # Directorio base de la tesis
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Revirtiendo comillas guillemot en: {base_dir}")
    
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
        
        file_changed, changes = fix_guillemot_quotes(tex_file)
        
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
        print("\n¡Reversión completada! Ahora las comillas son tipográficas españolas estándar.")
        print("Recomendación: Ejecuta la compilación para verificar que todo funciona correctamente.")
    else:
        print("\nNo se encontraron comillas guillemot para revertir.")

if __name__ == "__main__":
    main()
