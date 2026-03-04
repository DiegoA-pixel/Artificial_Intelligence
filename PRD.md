# 🧠 PRD – Generador de Rutinas Inteligente

## 1. Descripción del Producto

Aplicación web desarrollada con Streamlit que permite generar rutinas personalizadas a partir de la edad y el objetivo del usuario.

El sistema funciona en dos modos:

- **Modo IA (online):** genera rutinas dinámicas usando una API externa.
- **Modo básico (fallback):** genera rutinas predefinidas con variaciones aleatorias cuando falla la IA.

Además, incluye una **visualización gráfica** de la distribución diaria.

---

## 2. Problema

Los usuarios que buscan rutinas rápidas:

- No siempre reciben resultados si falla la API
- Pueden abandonar la app si no obtienen respuesta
- Necesitan algo inmediato, no perfecto

---

## 3. Objetivo

Garantizar que el usuario:

- Siempre obtenga una rutina
- Tenga una experiencia fluida
- Visualice su planificación diaria

---

## 4. Alcance del Producto

El usuario puede:

- Ingresar su edad
- Seleccionar un objetivo:
  - Ganar músculo
  - Bajar de peso
  - Salud
  - Estudio
  - Productividad

El sistema:

- Intenta generar rutina con IA
- Si falla → activa modo básico automáticamente
- Muestra rutina en texto
- Genera gráfico de distribución diaria

---

## 5. Funcionalidades Clave

### 5.1 Generación con IA

- Uso de API externa (Hugging Face)
- Generación de texto dinámico
- Rutinas más detalladas (cuando funciona)

---

### 5.2 Modo Básico Mejorado

Se activa cuando:

- Falla la API
- No hay API KEY
- Timeout o error de red

Incluye:

- Plantillas predefinidas por objetivo
- Selección aleatoria (variación)
- Recomendaciones adicionales:
  - Horas de sueño
  - Consumo de agua

Esto evita que todas las respuestas sean iguales.

---

### 5.3 Visualización de Datos

- Gráfico de barras con:
  - Entrenamiento / Estudio / Descanso / Actividad
- Generado con matplotlib
- Refuerza la comprensión del usuario

---

### 5.4 Manejo de Errores

- Uso de `try/except`
- Validación de respuesta HTTP
- Fallback automático sin romper la app

Mensaje mostrado:
> ⚠️ Usando modo básico mejorado

---

## 6. Requisitos Funcionales

- RF1: El usuario debe poder ingresar edad
- RF2: El usuario debe seleccionar un objetivo
- RF3: El sistema debe generar una rutina SIEMPRE
- RF4: Debe existir fallback automático
- RF5: Debe mostrarse un gráfico
- RF6: El sistema debe responder en menos de 10 segundos

---

## 7. Requisitos No Funcionales

- Usabilidad: interfaz simple (Streamlit)
- Robustez: tolerancia a fallos de API
- Disponibilidad: alta gracias al fallback
- Rendimiento:
  - IA: hasta 10 segundos
  - Básico: menos de 1 segundo

---

## 8. Arquitectura Simplificada

- Frontend: Streamlit
- Backend lógico: Python
- API externa: Hugging Face (modelo de texto)
- Fallback local: lógica basada en listas y random

---

## 9. Casos de Uso

### Caso 1 – IA funciona

1. Usuario ingresa datos  
2. Se llama a la API  
3. Se muestra rutina generada  
4. Se muestra gráfico  

---

### Caso 2 – IA falla

1. Usuario ingresa datos  
2. API falla o no responde  
3. Se activa modo básico  
4. Se muestra rutina alternativa  
5. Se muestra gráfico  

---

## 10. Métricas de Éxito

- 100% de usuarios reciben una rutina
- Tiempo de respuesta aceptable
- App no se rompe ante errores
- Variación en resultados (modo básico)

---

## 11. Limitaciones

- Dependencia de API externa para modo IA
- Rutinas básicas no altamente personalizadas
- No hay almacenamiento de usuarios

---

## 12. Futuras Mejoras

- Guardar rutinas del usuario
- Más inputs (nivel, tiempo, equipo)
- Mejor modelo de IA
- Interfaz más avanzada
- Historial de rutinas

---

## 13. Conclusión

El sistema prioriza la disponibilidad sobre la perfección:

> Es mejor entregar una rutina básica funcional que no entregar nada.