# Sistema de Gestion de Gastos Personales

### **Estudiante:** SIFUENTES ASENCIOS Elmer
### **Asignatura:** Programacion Web
### **Carrera:** Ingenieria de Sistemas

Aplicación web para control de finanzas personales desarrollada en Python (Flask) y SQLite, con validaciones y pruebas unitarias mediante `pytest`.

---

## 🛠️ Requisitos e Instalación

1. **Clonar repositorio e instalar dependencias:**
   ```bash
   git clone https://github.com
   cd gestor_gastos
   py -m venv venv
   venv\Scripts\activate
   py -m pip install -r requirements.txt
   ```

---

## 🚀 Módulos Principales

* **Login:** Acceso con usuario `admin` y contraseña `123` *(ver `imagenes/login.png`)*.
* **Registro de Gastos:** Almacenamiento en SQLite con validación de montos mayores a cero *(ver `imagenes/panel.png`)*.
* **Reporte JSON:** Endpoint en `/reporte/json` para visualizar el total acumulado *(ver `imagenes/reporte.png`)*.

---

## 🧪 Pruebas Automatizadas

Ejecutar la suite de pruebas unitarias y de integración:
```bash
py -m pytest -v
```
*(Evidencia visual en `imagenes/pruebas.png`)*

