# 📚 PyData Panama - Tutoriales de Análisis de Datos con Python

Bienvenido a **pydatapanama-tutoriales**, un repositorio colaborativo de **PyData Panama** donde cualquier persona puede contribuir con tutoriales educativos sobre herramientas fundamentales para el análisis de datos con Python. 🚀

Este repositorio está diseñado para facilitar el aprendizaje de herramientas esenciales como **NumPy, Pandas, Matplotlib y Seaborn**, a través de tutoriales prácticos y bien estructurados.

---

## 🎯 **Objetivo del repositorio**
El propósito de este repositorio es:

🔎 Centralizar material educativo en español sobre análisis de datos en Python.  
💼 Permitir que cualquier miembro de la comunidad pueda **crear y compartir tutoriales**.  
💡 Fomentar el aprendizaje colaborativo y la práctica con código real.  
📖 Servir como base de conocimiento para cualquier persona interesada en la ciencia de datos.  
🏆 **Incentivar a los contribuidores con un sistema de ranking automático.**  

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

🔎 **Ejemplos válidos:**  
📅 `01_Numpy/arrays-basicos-jasonssdev/`  
📅 `02_Pandas/dataframes-introduccion-maria123/`  
📅 `03_Matplotlib/graficos-avanzados-carlosdev/`  

🛑 **Ejemplos inválidos:**  
🛠️ `01_Numpy/mi_tutorial/` (**No tiene el usuario de GitHub**)  
🛠️ `02_Pandas/tutorial_pandas/` (**No sigue el formato requerido**)  

📌 **Si no sigues este formato, tu contribución no será reconocida en el ranking.**

---

## 🤝 **Cómo contribuir con un tutorial (Fork + Pull Request)**
📒 Sigue estos pasos para contribuir con un nuevo tutorial:

### 1️⃣ **Haz un Fork del repositorio**
Entra al repositorio en GitHub y presiona el botón [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) en la esquina superior derecha o hacienco click en [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork).

### 2️⃣ **Clona tu Fork en tu máquina local**
```bash
git clone https://github.com/tu-usuario/pydatapanama-tutoriales.git
cd pydatapanama-tutoriales
```

### 3️⃣ **Configura el repositorio remoto principal**
Para mantener tu Fork actualizado, agrega el repositorio original como `upstream`:
```bash
git remote add upstream https://github.com/pydatapanama/pydatapanama-tutoriales.git
git fetch upstream
git merge upstream/main
```

### 4️⃣ **Crea una nueva rama para tu tutorial**
```bash
git checkout -b tutorial-{herramienta}-{tu_usuario}
```

### 5️⃣ **Copia el template del tutorial**
```bash
cp -r template-{herramienta} {nombre_breve_del_tutorial}-{tu_usuario}
```

### 6️⃣ **Edita tu tutorial**
Modifica los archivos en la carpeta que creaste:
- **README.md**: Explicación del tutorial.
- **notebooks/**: Notebooks de Jupyter.
- **data/**: Datos usados en el tutorial.
- **src/**: Código auxiliar.
- **tests/**: Pruebas unitarias.

### 7️⃣ **Guarda y sube los cambios a tu Fork**
```bash
git add .
git commit -m "📚 Añadiendo tutorial sobre {tema}"
git push origin tutorial-{herramienta}-{tu_usuario}
```

### 8️⃣ **Crea un Pull Request hacia el repositorio original**
1. Ve a tu Fork en GitHub.
2. Presiona "Compare & pull request".
3. Asegúrate de que la base es `main` del repositorio original.
4. Describe tu contribución y envía el Pull Request.

### 9️⃣ **Espera revisión y Merge**
Los administradores revisarán tu PR y si cumple con los requisitos, lo integrarán al repositorio.

---

## 🌟 **¡Gracias por contribuir!**
Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

