# 📚 PyData Panama - Template para Tutoriales de NumPy

Bienvenido a **template-numpy**, un recurso para que los miembros de **PyData Panama** contribuyan con tutoriales de NumPy.

📌 **Objetivo:** Crear una colección de tutoriales sobre NumPy accesibles para cualquier persona interesada en el análisis de datos y la programación en Python.

📌 **Flujo de contribución:**
1. **Realiza un [Fork](https://github.com/pydatapanama/pydatapanama-tutoriales/fork) del repositorio principal.**
2. **Clona tu Fork a tu computadora local.**
3. **Crea un nuevo branch para tu tutorial.**
4. **Sigue la estructura del template y desarrolla tu tutorial.**
5. **Envía un Pull Request (PR) para que sea revisado e integrado.**

---

## 📂 **Estructura del Tutorial**
Cada tutorial debe seguir esta estructura para mantener un formato uniforme:

```plaintext
🗂 template-numpy/
 ├️ README.md         # Explicación del tutorial
 ├️ 🗂 data/          # Datos utilizados en el tutorial (si aplica)
 ├️ 🗂 notebooks/     # Notebooks de Jupyter con el contenido del tutorial
 ├️ 🗂 src/           # Código fuente adicional (funciones, módulos auxiliares)
 └️ 🗂 tests/         # Pruebas unitarias (si aplica)
```
📌 **No es obligatorio llenar todas las carpetas**, solo usa lo necesario para tu tutorial.

---

## 🚀 **Pasos para contribuir**

### 1️⃣ Haz un Fork del repositorio
Ve a la página del repositorio y haz clic en **Fork** para crear una copia en tu cuenta.

### 2️⃣ Clona tu Fork en tu computadora
```bash
git clone https://github.com/tu_usuario/pydatapanama-tutoriales.git
cd pydatapanama-tutoriales/01_Numpy
```

### 3️⃣ Crea un nuevo branch con tu usuario
```bash
git checkout -b tutorial-numpy-{tu_usuario}
```

### 4️⃣ Copia el template para tu tutorial
```bash
cp -r template-numpy {nombre_breve_del_tutorial}-{tu_usuario}
```

📌 **Ejemplo:** Si el tutorial es sobre "arrays-básicos" y tu usuario es `jasonssdev`:
```bash
cp -r template-numpy arrays-basicos-jasonssdev
```

### 5️⃣ Agrega tu contenido respetando la estructura del repositorio
- **README.md:** Explicación del contenido del tutorial.
- **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.
- **data/**: Contiene datasets (si el tutorial requiere datos para análisis).
- **src/**: Código fuente auxiliar (funciones, scripts).
- **tests/**: Pruebas unitarias (si aplica).

### 6️⃣ Agrega y commitea tus cambios
```bash
git add .
git commit -m "📝 Agregando tutorial sobre {tema}"
```

### 7️⃣ Sube tu branch y envía un Pull Request
```bash
git push origin tutorial-numpy-{tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📚 **Ejemplo práctico de NumPy**
A continuación, un ejemplo básico de cómo crear y manipular arrays en NumPy:

```python
import numpy as np

# Crear un array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Operaciones básicas
print("Suma de todos los elementos:", np.sum(arr))
print("Media de los elementos:", np.mean(arr))
print("Desviación estándar:", np.std(arr))
```

📌 **Este es solo un ejemplo.** En tu tutorial, agrega explicaciones detalladas, gráficos y ejercicios prácticos.

---

## 📚 **Fuentes y documentación oficial**
Si necesitas referencias adicionales, consulta la documentación oficial de NumPy:
- 📌 [NumPy Docs](https://numpy.org/doc/stable/)
- 📌 [Guía Rápida de NumPy](https://numpy.org/doc/stable/user/quickstart.html)

---

## 🤝 **Buenas prácticas al contribuir**
- 📌 **Formato:** Usa **Markdown** en los notebooks para explicar conceptos antes de mostrar código.
- 📌 **Ejemplos:** Asegúrate de incluir ejemplos que sean **prácticos y aplicables**.
- 📌 **Código limpio:** Sigue las buenas prácticas de programación (nombres de variables descriptivos, comentarios claros).
- 📌 **Ejercicios:** Agrega ejercicios para que los lectores practiquen lo aprendido.
- 📌 **Revisión:** Antes de enviar el PR, revisa que todo esté bien estructurado.

---

🚀 **Gracias por contribuir a PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 💯

