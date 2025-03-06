# 📚 PyData Panama - Tutoriales de Análisis de Datos con Python

Bienvenido a **pydatapanama-tutoriales**, un repositorio colaborativo de **PyData Panama** donde cualquier persona puede contribuir con tutoriales educativos sobre herramientas fundamentales para el análisis de datos con Python. 🚀

Este repositorio está diseñado para facilitar el aprendizaje de herramientas esenciales como **NumPy, Pandas, Matplotlib y Seaborn**, a través de tutoriales prácticos y bien estructurados.

---

## 🎯 **Objetivo del repositorio**
El propósito de este repositorio es:

✅ Centralizar material educativo en español sobre análisis de datos en Python.  
✅ Permitir que cualquier miembro de la comunidad pueda **crear y compartir tutoriales**.  
✅ Fomentar el aprendizaje colaborativo y la práctica con código real.  
✅ Servir como base de conocimiento para cualquier persona interesada en la ciencia de datos.  

📌 **Todos los tutoriales siguen un mismo formato**, lo que permite que sean fáciles de seguir y estructurados de manera uniforme.

---

## 📂 **Estructura del repositorio**
Cada herramienta tiene su propia carpeta con tutoriales organizados:
```plaintext
📂 pydatapanama-tutoriales/
 ├── 📂 00_Anaconda/      # Configuración del entorno
 ├── 📂 01_Numpy/         # Tutoriales de NumPy
 ├── 📂 02_Pandas/        # Tutoriales de Pandas
 ├── 📂 03_Matplotlib/    # Tutoriales de Matplotlib
 ├── 📂 04_Seaborn/       # Tutoriales de Seaborn
 ├── .gitignore           # Archivos que no deben subirse a GitHub
 ├── LICENSE              # Licencia open-source
 ├── README.md            # Descripción general del repositorio
```
📌 **Cada carpeta contiene múltiples tutoriales creados por diferentes colaboradores.**

---

## 🤝 **Cómo contribuir con un tutorial**
¡Tu conocimiento es valioso! Sigue estos pasos para contribuir con un nuevo tutorial:

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
💡 *Es mejor hacer esto antes de modificar archivos para trabajar en una rama aislada.*  
```bash
git checkout -b tutorial-{herramienta}-{tu_usuario}
```

### 4️⃣ **Copia el template del tutorial**
Cada carpeta contiene un `template` que puedes usar para estructurar tu tutorial. Copia el template y cambia `{nombre_breve_del_tutorial}` y `{tu_usuario}` por valores personalizados:

```bash
cp -r template-{herramienta} {nombre_breve_del_tutorial}-{tu_usuario}
```

📌 **Ejemplo real para Matplotlib:**
```bash
cp -r template-matplotlib graficos-basicos-jasonssdev
```

### 5️⃣ **Crea tu tutorial**
Modifica los archivos dentro de la carpeta que copiaste:
- **README.md**: Explica el contenido de tu tutorial.
- **notebooks/**: Contiene el notebook de Jupyter con ejemplos y explicaciones.
- **data/**: Si tu tutorial usa datasets, guárdalos aquí.
- **src/**: Código auxiliar o funciones personalizadas.
- **tests/**: Pruebas unitarias (si aplican).

### 6️⃣ **Agrega y commitea tus cambios**
```bash
git add .
git commit -m "Añadiendo tutorial sobre {tema} en {herramienta}"
```

### 7️⃣ **Sube tu branch a GitHub**
```bash
git push origin tutorial-{herramienta}-{tu_usuario}
```

### 8️⃣ **Envía un Pull Request (PR)**
Ve a **GitHub** y crea un **Pull Request** para que revisemos tu tutorial y lo integremos al repositorio.

---

## 📚 **Explora los tutoriales disponibles**
Si quieres aprender, simplemente explora los tutoriales dentro de cada categoría:
- [🔢 NumPy](01_Numpy/) → Manipulación de arrays y cálculos numéricos.
- [📝 Pandas](02_Pandas/) → Procesamiento y análisis de datos tabulares.
- [📊 Matplotlib](03_Matplotlib/) → Creación de gráficos básicos y avanzados.
- [📈 Seaborn](04_Seaborn/) → Visualizaciones estadísticas sofisticadas.

---

## 🌟 **¿Cómo puedes ayudar a mejorar este repositorio?**
✅ **Crea un tutorial** y compártelo con la comunidad.  
✅ **Corrige o mejora un tutorial existente** con ejemplos o explicaciones más detalladas.  
✅ **Propón nuevas ideas** creando un Issue en GitHub.  
✅ **Comparte este repositorio** con otros interesados en aprender análisis de datos con Python.  

📢 ¡Queremos hacer crecer esta comunidad de aprendizaje colaborativo! 🚀

---

## 📜 **Licencia**
Este repositorio está bajo la **Apache License 2.0**. Puedes encontrar más detalles en:  
📌 [Apache License 2.0](http://www.apache.org/licenses/)

---

🚀 **Gracias por ser parte de PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

