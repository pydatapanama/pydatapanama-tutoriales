# 📚 PyData Panama - Template para Tutoriales de Pandas

Bienvenido a **template-pandas**, un repositorio diseñado para que los miembros de **PyData Panama** puedan contribuir con tutoriales de Pandas.

📌 **Objetivo:** Crear una colección de tutoriales sobre Pandas que sean accesibles para cualquier persona interesada en el análisis de datos y la programación en Python.

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
📂 template-pandas/
 ├── README.md         # Explicación del tutorial
 ├── 📂 data/          # Datos utilizados en el tutorial (si aplica)
 ├── 📂 notebooks/     # Notebooks de Jupyter con el contenido del tutorial
 ├── 📂 src/           # Código fuente adicional (funciones, módulos auxiliares)
 ├── 📂 tests/         # Pruebas unitarias (si aplica)
```
📌 **No es obligatorio llenar todas las carpetas**, solo usa lo necesario para tu tutorial.

---

## 🚀 ¿Qué aprenderás en este tutorial?
Pandas es la librería más utilizada en Python para la manipulación y análisis de datos, y es clave en el ecosistema de ciencia de datos.

Al contribuir con un tutorial aquí, puedes abordar temas como:
- Introducción a Pandas y estructuras de datos (Series y DataFrames).
- Carga y manipulación de datos.
- Filtrado, indexación y selección de datos.
- Limpieza y transformación de datos.
- Agregaciones y funciones avanzadas.
- Visualización de datos con Pandas.

📌 **Cada tutorial debe tener un objetivo y no necesariamente debe ser uno de estos temas, además debe ser claro y didáctico.**

---

## 🔹 ¿Cómo clonar el repositorio y empezar?

Para contribuir con tu tutorial, sigue estos pasos:

### 1️⃣ Clona el repositorio
Abre tu terminal y ejecuta:
```bash
git clone git@github.com:pydatapanama/pydatapanama-tutoriales.git
cd 02_Pandas
cp -r pydatapanama-tutoriales/02_Pandas/template-pandas pydatapanama-tutoriales/02_Pandas/{nombre_breve_del_tutorial}-{nombre_usuario_github}
```

### 📌 Ejemplo real: Si el tutorial es sobre “dataframes-básicos” y tu nombre de usuario de Github es jasonssdev:
```bash
cp -r pydatapanama-tutoriales/02_Pandas/template-pandas pydatapanama-tutoriales/02_Pandas/dataframes-basicos-jasonssdev
```

### 2️⃣ Crea un nuevo branch con tu nombre de usuario
```bash
git checkout -b {tutorial-pandas-tu_usuario}
```

### 3️⃣ Agrega tu tutorial respetando la estructura del repositorio
📌 **README.md:** Explicación del contenido del tutorial.
📌 **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.
📌 **data/**: Contiene datasets (si el tutorial requiere datos para análisis).
📌 **src/**: Código fuente auxiliar (funciones, scripts).
📌 **tests/**: Pruebas unitarias (si aplica).

Ejemplo de nombre de archivo:
```plaintext
notebooks/tutorial_pandas_basico.ipynb
```

### 4️⃣ Agrega y commitea tus cambios
```bash
git add .
git commit -m {"Añadiendo tutorial sobre manipulación de DataFrames en Pandas"}
```

### 5️⃣ Sube tu branch y envía un Pull Request
```bash
git push origin {tutorial-pandas-tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📌 Ejemplo práctico de Pandas
A continuación, un ejemplo básico de cómo cargar y manipular datos en Pandas:

```python
import pandas as pd

# Crear un DataFrame
data = {"Nombre": ["Ana", "Luis", "Carlos"], "Edad": [23, 25, 30]}
df = pd.DataFrame(data)
print(df)

# Filtrar datos
df_filtrado = df[df["Edad"] > 24]
print("\nPersonas mayores de 24 años:")
print(df_filtrado)
```

🔹 **Este es solo un ejemplo. En tu tutorial, deberías incluir explicaciones más detalladas y gráficos para ayudar a la comprensión.**

---

## 📚 Fuentes y documentación oficial
Si necesitas referencias adicionales, consulta la documentación oficial de Pandas:
- 📌 [Pandas Docs](https://pandas.pydata.org/docs/)
- 📌 [Guía Rápida de Pandas](https://pandas.pydata.org/docs/user_guide/index.html)

---

## 🤝 Contribuciones y buenas prácticas
📌 **Formato:** Usa **Markdown** en los notebooks para explicar conceptos antes de mostrar código.
📌 **Ejemplos:** Asegúrate de incluir ejemplos que sean **prácticos y aplicables**.
📌 **Código limpio:** Sigue las buenas prácticas de programación (nombres de variables descriptivos, comentarios claros).
📌 **Ejercicios:** Agrega ejercicios para que los lectores practiquen lo aprendido.
📌 **Revisión:** Antes de enviar el PR, revisa que todo esté bien estructurado.

---

🚀 **Gracias por contribuir a PyData Panama!** Si tienes dudas, pregunta en nuestra comunidad o abre un Issue en GitHub. 🎯

