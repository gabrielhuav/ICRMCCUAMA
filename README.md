# Resumen de Tesis: Calibración de Hiper-Parámetros para la Detección de Noticias Falsas

## Autor
- Gabriel Hurtado Avilés

## Directores
- Dr. José Alejandro Reyes Ortiz
- Dr. Román Anselmo Mora Gutiérrez

---

## Resumen Ejecutivo

Este proyecto aborda el desafío de la detección de noticias falsas en español mediante la aplicación y comparación de dos metodologías de inteligencia artificial. Aunque las técnicas desarrolladas son aplicables a otros tipos de fraude digital, el enfoque se centra en la identificación de contenido noticioso falso o engañoso. La primera metodología explora algoritmos metaheurísticos sobre una representación TF-IDF, mientras que la segunda, adoptada tras los hallazgos iniciales, se basa en el ajuste fino de un modelo de lenguaje Transformer pre-entrenado (DistilBERT).

Para el entrenamiento, se construyó un corpus unificado de más de 61,000 noticias a partir de cuatro conjuntos de datos públicos en español y datos extraídos mediante extracción web del portal satírico "El Deforma". La calibración de hiperparámetros se realizó con una división de datos estratificada del 70% para entrenamiento, 10% para validación y 20% para pruebas.

Los resultados validan el ajuste fino como una solución de vanguardia, demostrando una eficacia superior y superando a los enfoques metaheurísticos en esta tarea.

---

## Objetivos Principales

* **Objetivo General:** Desarrollar un método computacional basado en algoritmos metaheurísticos y modelos de lenguaje para detectar noticias falsas en español, con una metodología que sea transferible a otros tipos de fraude digital.
* **Objetivos Específicos:**
    * Recopilar y procesar un conjunto de datos diverso a partir de múltiples corpus en español y enriquecerlo mediante extracción web.
    * Implementar un sistema de detección inicial utilizando técnicas de PLN y algoritmos metaheurísticos.
    * Desarrollar un sistema de detección avanzado mediante el ajuste fino de un modelo DistilBERT.
    * Realizar un análisis comparativo de rendimiento entre ambos enfoques.
    * Desarrollar un prototipo de aplicación web con Docker para demostrar la aplicabilidad práctica del modelo de mayor rendimiento.

---

## Metodología y Enfoques

La investigación se basó en una metodología evolutiva que comparó dos paradigmas distintos:

### 1. Enfoque Clásico Optimizado
* **Representación de texto:** Utilizó la técnica TF-IDF (Term Frequency-Inverse Document Frequency).
* **Optimización:** Se calibraron los hiperparámetros de un clasificador logístico binario utilizando cinco algoritmos metaheurísticos:
    * Algoritmo Genético (GA)
    * Optimización por Enjambre de Partículas (PSO)
    * Recocido Multiarranque (MSA)
    * Búsqueda Dispersa (SS)
    * Búsqueda en Vecindades Variables (VNS)
* **Contribución:** Este enfoque estableció una línea base robusta y permitió caracterizar las fortalezas y debilidades de cada algoritmo para la tarea.

### 2. Enfoque de Deep Learning (Transformer)
* **Modelo base:** Se seleccionó **DistilBERT** por su balance óptimo entre rendimiento y eficiencia, así como por su soporte multilingüe que incluye español.
* **Técnica:** Se aplicó un proceso de ajuste fino (fine-tuning) sobre el corpus unificado en español.
* **Optimización:** Se implementó una rigurosa estrategia de regularización y búsqueda de hiperparámetros utilizando `KerasTuner` para mitigar el sobreajuste.

---

## Resultados y Conclusiones

Los resultados demuestran la superioridad del enfoque Transformer:

* **Rendimiento Superior:** El modelo DistilBERT optimizado alcanzó una **exactitud del 95.2%** y un F1-Score de 0.952, superando al mejor algoritmo metaheurístico (GA) por más de 24 puntos porcentuales en exactitud.
* **Balance en la Clasificación:** El modelo Transformer mostró una detección excelente de ambas clases (noticias falsas y reales), logrando una especificidad del 94.96%, una mejora del 97.83% sobre el mejor modelo metaheurístico.
* **Implementación Práctica:** El modelo final fue integrado en una aplicación web funcional desarrollada con Flask y Docker, capaz de analizar URLs en tiempo real y clasificar su contenido como "FALSO" o "REAL".

### Visualizaciones Clave
| Convergencia de Exactitud | Matriz de Confusión (Modelo Final) |
|---|---|
| ![Gráfico de Convergencia del Modelo DistilBERT Final](Imagenes/curva_convergencia_v11_epoca_21.png) | ![Matriz de Confusión del Modelo DistilBERT Final](Imagenes/Entrenamiento/matriz_confusion_v7.png) |

---

## Limitaciones del Estudio

* **Dependencia Textual:** Los modelos se basan exclusivamente en el texto, sin analizar elementos multimodales como imágenes o videos.
* **Simplificación Binaria:** El enfoque de clasificación binaria no captura las "zonas grises" de la veracidad, donde la información puede ser parcialmente correcta o tener un sesgo interpretativo.
* **Sensibilidad de Dominio:** El rendimiento del modelo podría variar en dominios muy especializados (ej. fraude financiero o desinformación científica) ya que el corpus se enfocó principalmente en noticias generales y políticas.
* **Fronteras Difusas:** El modelo puede tener dificultades con contenido satírico ambiguo o información que depende de un contexto temporal o cultural muy específico.