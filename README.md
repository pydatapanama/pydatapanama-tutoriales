# 📚 PyData Panama - Tutoriales de Análisis de Datos con Python

Bienvenido a **pydatapanama-tutoriales**, un repositorio colaborativo de **PyData Panama** donde cualquier persona puede contribuir con tutoriales educativos sobre herramientas fundamentales para el análisis de datos con Python. 🚀

Este repositorio está diseñado para facilitar el aprendizaje de herramientas esenciales como **NumPy, Pandas, Matplotlib y Seaborn**, a través de tutoriales prácticos y bien estructurados.

---

## 🎯 **Objetivo del repositorio**
El propósito de este repositorio es:

👉 Centralizar material educativo en español sobre análisis de datos en Python.  
👉 Permitir que cualquier miembro de la comunidad pueda **crear y compartir tutoriales**.  
👉 Fomentar el aprendizaje colaborativo y la práctica con código real.  
👉 Servir como base de conocimiento para cualquier persona interesada en la ciencia de datos.  
👉 **Incentivar a los contribuidores con un sistema de ranking automático.**  

📌 **Todos los tutoriales siguen un mismo formato**, lo que permite que sean fáciles de seguir y estructurados de manera uniforme.

---

## 🏆 **Sistema de Ranking - Gana puntos por contribuir**
Para fomentar la participación, este repositorio incluye un **ranking automático** que asigna puntos a los contribuidores:

| Acción | Puntos |
|--------|--------|
| **Crear un nuevo tutorial** | +20 puntos |
| **Modificar o mejorar un tutorial existente** | +10 puntos |

📌 **El ranking se actualiza automáticamente** cuando un Pull Request (PR) es fusionado a `main`.  
📌 Puedes consultar el **ranking actual** en el archivo [`RANKING.md`](RANKING.md).

---

## 📂 **Estructura del repositorio**
Cada herramienta tiene su propia carpeta con tutoriales organizados:
```plaintext
📂 pydatapanama-tutoriales/
 ├📂 00_Anaconda/      # Configuración del entorno
 ├📂 01_Numpy/         # Tutoriales de NumPy
 ├📂 02_Pandas/        # Tutoriales de Pandas
 ├📂 03_Matplotlib/    # Tutoriales de Matplotlib
 ├📂 04_Seaborn/       # Tutoriales de Seaborn
 ├📂 .github/workflows/   # Automatización de ranking en GitHub Actions
 ├📂 scripts/             # Código del sistema de ranking
 ├📂 RANKING.md           # Ranking de contribuidores
 ├📂 LICENSE              # Licencia open-source
 └📂 README.md            # Descripción general del repositorio
```
📌 **Cada carpeta contiene múltiples tutoriales creados por diferentes colaboradores.**

---

## 📁 **Reglas para nombrar los tutoriales correctamente**
Para que GitHub Actions detecte y asigne puntos correctamente, cada tutorial **debe seguir este formato de nombre**:

```
{nombre-breve-del-tutorial}-{usuario-github}
```

👉 **Ejemplos válidos:**  
👉 `01_Numpy/arrays-basicos-jasonssdev/`  
👉 `02_Pandas/dataframes-introduccion-maria123/`  
👉 `03_Matplotlib/graficos-avanzados-carlosdev/`  

🔴 **Ejemplos inválidos:**  
🛑 `01_Numpy/mi_tutorial/` (**No tiene el usuario de GitHub**)  
🛑 `02_Pandas/tutorial_pandas/` (**No sigue el formato requerido**)  

📌 **Si no sigues este formato, tu contribución no será reconocida en el ranking.**

---

## 🤝 **Cómo contribuir con un tutorial**
👉 Sigue estos pasos para contribuir con un nuevo tutorial:

### 1️⃣ **Clona el repositorio**
```bash
git clone git@github.com:pydatapanama/pydatapanama-tutoriales.git
cd pydatapanama-tutoriales
```

### 2️⃣ **Elige una categoría**
Dirígete a la carpeta de la herramienta sobre la que quieres crear un tutorial:
- **NumPy** → `cd 01_Numpy`
- **Pandas** → `cd 02_Pandas`
- **Matplotlib** → `cd 03_Matplotlib`
- **Seaborn** → `cd 04_Seaborn`

### 3️⃣ **Crea un nuevo branch con tu usuario**
```bash
git checkout -b tutorial-{herramienta}-{tu_usuario}
```

### 4️⃣ **Copia el template del tutorial**
```bash
cp -r template-{herramienta} {nombre_breve_del_tutorial}-{tu_usuario}
```

### 5️⃣ **Crea tu tutorial**
Edita los archivos en la carpeta que copiaste:
- **README.md**: Explicación del tutorial.
- **notebooks/**: Notebooks de Jupyter.
- **data/**: Datos usados en el tutorial.
- **src/**: Código auxiliar.
- **tests/**: Pruebas unitarias.

### 6️⃣ **Sube tu branch y haz un Pull Request**
```bash
git add .
git commit -m "📝 Añadiendo tutorial sobre {tema}"
git push origin tutorial-{herramienta}-{tu_usuario}
```

---

## 🌟 **¡Gracias por contribuir!**
Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

