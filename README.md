# Sistema de Gestion de Gastos Personales

### **Estudiante:** SIFUENTES ASENCIOS Elmer
### **Asignatura:** Programacion Web
### **Carrera:** Ingenieria de Sistemas

Aplicacion web para control de finanzas personales desarrollada en Python (Flask) y SQLite.

---

## 🛠️ Requisitos e Instalacion

Clona el repositorio e instala las dependencias mediante la terminal:
```bash
git clone https://github.com
cd gestor_gastos
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
```

---

## 🚀 Funcionamiento de la Aplicacion

* **Login (Admin / 123):** ![Login de la aplicacion](imagenes/login.png)
* **Panel de Registro:** ![Panel de control](imagenes/panel.png)
* **Reporte JSON (`/reporte/json`):** ![Reporte JSON](imagenes/reporte.png)

---

## 🧪 Ejecucion de Pruebas (pytest)

Ejecuta las pruebas unitarias y de rutas con:
```bash
py -m pytest -v
```
![Resultados de Pytest](imagenes/pruebas.png)
