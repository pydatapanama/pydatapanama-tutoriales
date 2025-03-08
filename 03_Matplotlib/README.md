# 📚 PyData Panama - Template para Tutoriales de Matplotlib

Bienvenido a **template-matplotlib**, un repositorio diseñado para que los miembros de **PyData Panama** puedan contribuir con tutoriales de Matplotlib.

📌 **Objetivo:** Crear una colección de tutoriales sobre Matplotlib que sean accesibles para cualquier persona interesada en la visualización de datos en Python.

📌 **¿Cómo funciona?**
1. **Haz un [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) del repositorio y clónalo en tu máquina local.**
2. **Sigue la estructura estándar del tutorial.**
3. **Crea tu tutorial y complementa con ejemplos prácticos.**
4. **Asegúrate de seguir las reglas de nombrado para que GitHub Actions registre tu contribución.**
5. **Envía un Pull Request (PR) con tu tutorial para ser revisado e integrado en la comunidad.**

---

## 📂 **Estructura del Tutorial**
Cada tutorial debe seguir esta estructura para mantener un formato uniforme:

```plaintext
📂 template-matplotlib/
 ├── README.md         # Explicación del tutorial
 ├── 📂 data/          # Datos utilizados en el tutorial (si aplica)
 ├── 📂 notebooks/     # Notebooks de Jupyter con el contenido del tutorial
 ├── 📂 src/           # Código fuente adicional (funciones, módulos auxiliares)
 ├── 📂 tests/         # Pruebas unitarias (si aplica)
```

📌 **No es obligatorio llenar todas las carpetas**, solo usa lo necesario para tu tutorial.

---

## 🚀 ¿Qué aprenderás en este tutorial?
Matplotlib es la librería más utilizada en Python para la creación de gráficos y visualización de datos.

Al contribuir con un tutorial aquí, puedes abordar temas como:
- Creación de gráficos básicos (barras, líneas, dispersión, histogramas).
- Personalización de gráficos (colores, etiquetas, leyendas).
- Subplots y figuras múltiples.
- Uso avanzado de Matplotlib (3D, animaciones, interactividad).
- Integración con Pandas y Seaborn.

📌 **Cada tutorial debe tener un objetivo y no necesariamente debe ser uno de estos temas, además debe ser claro y didáctico.**

---

# 🤝 **Cómo contribuir con un tutorial (Fork + Pull Request)**
📒 Sigue estos pasos para contribuir con un nuevo tutorial:

### 1️⃣ **Haz un Fork del repositorio**
Entra al repositorio en GitHub y presiona el botón [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) en la esquina superior derecha o haciendo click en [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork).

### 2️⃣ **Clona tu Fork en tu máquina local**
```bash
git clone https://github.com/tu-usuario/pydatapanama-tutoriales.git
cd pydatapanama-tutoriales
```

### 3️⃣ **Crea un nuevo branch con tu nombre de usuario**
```bash
git checkout -b tutorial-matplotlib-{tu_usuario}
```

### 4️⃣ **Copia el template del tutorial**
```bash
cp -r 03_Matplotlib/template-matplotlib 03_Matplotlib/{nombre_breve_del_tutorial}-{tu_usuario}
```

📌 **Ejemplo real:** Si el tutorial es sobre "gráficos de barras" y tu usuario es `jasonssdev`:
```bash
cp -r 03_Matplotlib/template-matplotlib 03_Matplotlib/graficos-barras-jasonssdev
```

### 5️⃣ **Agrega tu tutorial respetando la estructura del repositorio**
📌 **README.md:** Explicación del contenido del tutorial.
📌 **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.
📌 **data/**: Contiene datasets (si el tutorial requiere datos para análisis).
📌 **src/**: Código fuente auxiliar (funciones, scripts).
📌 **tests/**: Pruebas unitarias (si aplica).

Ejemplo de nombre de archivo:
```plaintext
notebooks/tutorial_matplotlib_basico.ipynb
```

### 6️⃣ **Agrega y commitea tus cambios**
```bash
git add .
git commit -m "📁 Añadiendo tutorial sobre gráficos de barras en Matplotlib"
```

### 7️⃣ **Sube tu branch y envía un Pull Request**
```bash
git push origin tutorial-matplotlib-{tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📌 Ejemplo práctico de Matplotlib
A continuación, un ejemplo básico de cómo crear un gráfico de barras en Matplotlib:

```python
import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Crear la figura
plt.bar(categorias, valores, color='skyblue')
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.title("Ejemplo de gráfico de barras en Matplotlib")
plt.show()
```

🔹 **Este es solo un ejemplo. En tu tutorial, deberías incluir explicaciones más detalladas y gráficos adicionales para ayudar a la comprensión.**

---

## 📚 Fuentes y documentación oficial
Si necesitas referencias adicionales, consulta la documentación oficial de Matplotlib:
- 📌 [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- 📌 [Guía Rápida de Matplotlib](https://matplotlib.org/stable/users/prev_whats_new/whats_new_3.4.0.html)

---

## 🤝 Contribuciones y buenas prácticas
📌 **Formato:** Usa **Markdown** en los notebooks para explicar conceptos antes de mostrar código.
📌 **Ejemplos:** Asegúrate de incluir ejemplos que sean **prácticos y aplicables**.
📌 **Código limpio:** Sigue las buenas prácticas de programación (nombres de variables descriptivos, comentarios claros).
📌 **Ejercicios:** Agrega ejercicios para que los lectores practiquen lo aprendido.
📌 **Revisión:** Antes de enviar el PR, revisa que todo esté bien estructurado.

---

🚀 **Gracias por contribuir a PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

