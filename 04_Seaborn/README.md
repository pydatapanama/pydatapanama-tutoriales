# 📚 PyData Panama - Template para Tutoriales de Seaborn

Bienvenido a **template-seaborn**, un repositorio diseñado para que los miembros de **PyData Panama** puedan contribuir con tutoriales de Seaborn.

📌 **Objetivo:** Crear una colección de tutoriales sobre Seaborn que sean accesibles para cualquier persona interesada en el análisis y visualización de datos en Python.

📌 **¿Cómo funciona?**
1. **Haz un [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) del repositorio y clónalo a tu computadora.**
2. **Sigue la estructura estándar del tutorial.**
3. **Crea tu tutorial y complementa con ejemplos prácticos.**
4. **Envía un Pull Request (PR) con tu tutorial para ser revisado e integrado en la comunidad.**

---

## 📂 **Estructura del Tutorial**
Cada tutorial debe seguir esta estructura para mantener un formato uniforme:
```plaintext
📂 template-seaborn/
 ├── README.md         # Explicación del tutorial
 ├── 📂 data/          # Datos utilizados en el tutorial (si aplica)
 ├── 📂 notebooks/     # Notebooks de Jupyter con el contenido del tutorial
 ├── 📂 src/           # Código fuente adicional (funciones, módulos auxiliares)
 ├── 📂 tests/         # Pruebas unitarias (si aplica)
```
📌 **No es obligatorio llenar todas las carpetas**, solo usa lo necesario para tu tutorial.

---

## 🚀 ¿Qué aprenderás en este tutorial?
Seaborn es una de las librerías más potentes para la visualización de datos en Python. Al contribuir con un tutorial aquí, puedes abordar temas como:
- Introducción a Seaborn y su relación con Matplotlib.
- Creación de gráficos estadísticos con Seaborn.
- Personalización de gráficos y paletas de colores.
- Uso de `sns.pairplot()`, `sns.heatmap()`, `sns.boxplot()`, entre otros.
- Integración con Pandas para visualizaciones avanzadas.

📌 **Cada tutorial debe tener un objetivo claro, no necesariamente debe ser uno de estos temas, pero sí debe ser didáctico y bien explicado.**

---

# 🤝 **Cómo contribuir con un tutorial (Fork + Pull Request)**
📒 Sigue estos pasos para contribuir con un nuevo tutorial:

### 1️⃣ **Haz un Fork del repositorio**
Entra al repositorio en GitHub y presiona el botón [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) en la esquina superior derecha.

### 2️⃣ **Clona tu Fork en tu máquina local**
```bash
git clone https://github.com/tu-usuario/pydatapanama-tutoriales.git
cd pydatapanama-tutoriales
```

### 3️⃣ **Navega a la carpeta de Seaborn y copia el template**
```bash
cd 04_Seaborn
cp -r template-seaborn {nombre_breve_del_tutorial}-{tu_usuario_github}
```

### 📌 **Ejemplo real:** Si el tutorial es sobre "gráficos-de-dispersión" y tu nombre de usuario en GitHub es **jasonssdev**:
```bash
cp -r template-seaborn graficos-de-dispersion-jasonssdev
```

### 4️⃣ **Crea un nuevo branch con tu nombre de usuario**
```bash
git checkout -b tutorial-seaborn-{tu_usuario}
```

### 5️⃣ **Agrega tu tutorial respetando la estructura del repositorio**
📌 **README.md:** Explicación del contenido del tutorial.  
📌 **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.  
📌 **data/**: Contiene datasets (si el tutorial requiere datos para análisis).  
📌 **src/**: Código fuente auxiliar (funciones, scripts).  
📌 **tests/**: Pruebas unitarias (si aplica).  

Ejemplo de nombre de archivo:
```plaintext
notebooks/tutorial_seaborn_basico.ipynb
```

### 6️⃣ **Agrega y commitea tus cambios**
```bash
git add .
git commit -m "📝 Añadiendo tutorial sobre visualización con Seaborn"
```

### 7️⃣ **Sube tu branch y envía un Pull Request**
```bash
git push origin tutorial-seaborn-{tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📌 Ejemplo práctico de Seaborn
A continuación, un ejemplo básico de cómo crear un gráfico de dispersión con Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Crear un scatter plot
sns.scatterplot(x="total_bill", y="tip", hue="day", data=df)
plt.title("Propinas según el total de la cuenta")
plt.show()
```

🔹 **Este es solo un ejemplo. En tu tutorial, deberías incluir explicaciones más detalladas y personalización de gráficos para ayudar a la comprensión.**

---

## 📚 Fuentes y documentación oficial
Si necesitas referencias adicionales, consulta la documentación oficial de Seaborn:
- 📌 [Seaborn Docs](https://seaborn.pydata.org/)
- 📌 [Guía Rápida de Seaborn](https://seaborn.pydata.org/tutorial.html)

---

## 🤝 Contribuciones y buenas prácticas
📌 **Formato:** Usa **Markdown** en los notebooks para explicar conceptos antes de mostrar código.  
📌 **Ejemplos:** Asegúrate de incluir ejemplos que sean **prácticos y aplicables**.  
📌 **Código limpio:** Sigue las buenas prácticas de programación (nombres de variables descriptivos, comentarios claros).  
📌 **Ejercicios:** Agrega ejercicios para que los lectores practiquen lo aprendido.  
📌 **Revisión:** Antes de enviar el PR, revisa que todo esté bien estructurado.  

---

🚀 **Gracias por contribuir a PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

