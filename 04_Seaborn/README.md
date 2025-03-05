# 📚 PyData Panama - Template para Tutoriales de Seaborn

Bienvenido a **template-seaborn**, un repositorio diseñado para que los miembros de **PyData Panama** puedan contribuir con tutoriales de Seaborn.

📌 **Objetivo:** Crear una colección de tutoriales sobre Seaborn que sean accesibles para cualquier persona interesada en la visualización de datos en Python.

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
Seaborn es una de las librerías más utilizadas en Python para la visualización de datos basada en Matplotlib, pero con funcionalidades más avanzadas y estéticas. Con este tutorial, puedes aprender:
- Introducción a Seaborn y su integración con Pandas.
- Creación de gráficos categóricos, relacionales y de distribución.
- Personalización de gráficos (colores, estilos, tamaños, etiquetas).
- Creación de mapas de calor y gráficos avanzados.
- Comparación con Matplotlib y cuándo usar Seaborn.

📌 **Cada tutorial debe tener un objetivo claro y no necesariamente debe ser uno de estos temas, además debe ser claro y didáctico.**

---

## 🔹 ¿Cómo clonar el repositorio y empezar?

Para contribuir con tu tutorial, sigue estos pasos:

### 1️⃣ Clona el repositorio
Abre tu terminal y ejecuta:
```bash
git clone git@github.com:pydatapanama/pydatapanama-tutoriales.git
cd 04_Seaborn
cp -r pydatapanama-tutoriales/04_Seaborn/template-seaborn pydatapanama-tutoriales/04_Seaborn/{nombre_breve_del_tutorial}-{nombre_usuario_github}
```

### 📌 Ejemplo real: Si el tutorial es sobre “gráficos-de-distribución” y tu nombre de usuario de Github es jasonssdev:
```bash
cp -r pydatapanama-tutoriales/04_Seaborn/template-seaborn pydatapanama-tutoriales/04_Seaborn/graficos-de-distribucion-jasonssdev
```

### 2️⃣ Crea un nuevo branch con tu nombre de usuario
```bash
git checkout -b {tutorial-seaborn-tu_usuario}
```

### 3️⃣ Agrega tu tutorial respetando la estructura del repositorio
📌 **README.md:** Explicación del contenido del tutorial.
📌 **notebooks/**: Contiene notebooks de Jupyter con código y explicaciones.
📌 **data/**: Contiene datasets (si el tutorial requiere datos para análisis).
📌 **src/**: Código fuente auxiliar (funciones, scripts).
📌 **tests/**: Pruebas unitarias (si aplica).

Ejemplo de nombre de archivo:
```plaintext
notebooks/tutorial_seaborn_basico.ipynb
```

### 4️⃣ Agrega y commitea tus cambios
```bash
git add .
git commit -m {"Añadiendo tutorial sobre gráficos de distribución en Seaborn"}
```

### 5️⃣ Sube tu branch y envía un Pull Request
```bash
git push origin {tutorial-seaborn-tu_usuario}
```
Luego, **ve a GitHub y crea un Pull Request** para que revisemos tu tutorial y lo integremos en el repositorio principal. 🚀

---

## 📌 Ejemplo práctico de Seaborn
A continuación, un ejemplo básico de cómo crear gráficos en Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset de ejemplo
df = sns.load_dataset("tips")

# Crear un gráfico de dispersión
sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex", style="time")
plt.title("Propinas en relación con el total de la cuenta")
plt.show()
```

🔹 **Este es solo un ejemplo. En tu tutorial, deberías incluir explicaciones más detalladas y gráficos personalizados para ayudar a la comprensión.**

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

