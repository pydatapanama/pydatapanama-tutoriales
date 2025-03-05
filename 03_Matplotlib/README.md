# 📚 PyData Panama - Template para Tutoriales de Matplotlib

Bienvenido a **template-matplotlib**, un repositorio diseñado para que los miembros de **PyData Panama** puedan contribuir con tutoriales de Matplotlib.

📌 **Objetivo:** Crear una colección de tutoriales sobre Matplotlib que sean accesibles para cualquier persona interesada en la visualización de datos en Python.

📌 **¿Cómo funciona?**
1. **Clona este repositorio como base para tu tutorial**.
2. **Sigue la estructura estándar del tutorial**.
3. **Crea tu tutorial y complementa con ejemplos prácticos**.
4. **Lo que está entre {} es para que puedas cambiarlo acorde a tu tutorial**.
5. **Envía un Pull Request (PR) con tu tutorial para ser revisado e integrado en la comunidad**.

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
Matplotlib es la librería más utilizada en Python para la visualización de datos. Con este tutorial, puedes aprender:
- Introducción a Matplotlib y sus componentes básicos.
- Creación de gráficos de líneas, barras y dispersión.
- Personalización de gráficos (colores, etiquetas, títulos, estilos).
- Subgráficos y diseño avanzado con `subplot`.
- Integración con Pandas y Seaborn.
- Guardado de gráficos en diferentes formatos.

📌 **Cada tutorial debe tener un objetivo claro y no necesariamente debe ser uno de estos temas, además debe ser claro y didáctico.**

---

## 🔹 ¿Cómo clonar el repositorio y empezar?

Para contribuir con tu tutorial, sigue estos pasos:

### 1️⃣ Clona el repositorio
Abre tu terminal y ejecuta:
```bash
git clone git@github.com:pydatapanama/pydatapanama-tutoriales.git
cd 03_Matplotlib
cp -r pydatapanama-tutoriales/03_Matplotlib/template-matplotlib pydatapanama-tutoriales/03_Matplotlib/{nombre_breve_del_tutorial}-{nombre_usuario_github}
```

### 📌 Ejemplo real: Si el tutorial es sobre “gráficos-básicos” y tu nombre de usuario de Github es jasonssdev:
```bash
cp -r pydatapanama-tutoriales/03_Matplotlib/template-matplotlib pydatapanama-tutoriales/03_Matplotlib/graficos-basicos-jasonssdev
```

### 2️⃣ Crea un nuevo branch con tu nombre de usuario
```bash
git checkout -b {tutorial-matplotlib-tu_usuario}
```

### 3️⃣ Agrega tu tutorial respetando la estructura del repositorio
📌 **README.md:** Explicación del contenido del tutorial.
📌 **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.
📌 **data/**: Contiene datasets (si el tutorial requiere datos para análisis).
📌 **src/**: Código fuente auxiliar (funciones, scripts).
📌 **tests/**: Pruebas unitarias (si aplica).

Ejemplo de nombre de archivo:
```plaintext
notebooks/tutorial_matplotlib_basico.ipynb
```

### 4️⃣ Agrega y commitea tus cambios
```bash
git add .
git commit -m {"Añadiendo tutorial sobre gráficos básicos en Matplotlib"}
```

### 5️⃣ Sube tu branch y envía un Pull Request
```bash
git push origin {tutorial-matplotlib-tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📌 Ejemplo práctico de Matplotlib
A continuación, un ejemplo básico de cómo crear gráficos en Matplotlib:

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Crear el gráfico
plt.plot(x, y, marker='o', linestyle='--', color='b', label='Crecimiento')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejemplo de Gráfico en Matplotlib")
plt.legend()
plt.show()
```

🔹 **Este es solo un ejemplo. En tu tutorial, deberías incluir explicaciones más detalladas y gráficos personalizados para ayudar a la comprensión.**

---

## 📚 Fuentes y documentación oficial
Si necesitas referencias adicionales, consulta la documentación oficial de Matplotlib:
- 📌 [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- 📌 [Guía Rápida de Matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

## 🤝 Contribuciones y buenas prácticas
📌 **Formato:** Usa **Markdown** en los notebooks para explicar conceptos antes de mostrar código.
📌 **Ejemplos:** Asegúrate de incluir ejemplos que sean **prácticos y aplicables**.
📌 **Código limpio:** Sigue las buenas prácticas de programación (nombres de variables descriptivos, comentarios claros).
📌 **Ejercicios:** Agrega ejercicios para que los lectores practiquen lo aprendido.
📌 **Revisión:** Antes de enviar el PR, revisa que todo esté bien estructurado.

---

🚀 **Gracias por contribuir a PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

