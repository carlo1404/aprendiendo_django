# 🚀 Guía Completa de Django: Instalación y Primeros Pasos

¡Bienvenido a tu aventura con Django! Esta guía te ayudará a configurar tu primer proyecto Django de manera sencilla y divertida.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- Python (3.8 o superior)
- pip (gestor de paquetes de Python)

## 🎯 Instalación de Django

1. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual**
   - En Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Instalar Django**
   ```bash
   pip install django
   ```

## 🛠️ Crear un Nuevo Proyecto

1. **Crear el proyecto Django**
   ```bash
   django-admin startproject mi_proyecto
   cd mi_proyecto
   ```

2. **Crear una nueva aplicación**
   ```bash
   python manage.py startapp mi_app
   ```

3. **Realizar las migraciones iniciales**
   ```bash
   python manage.py migrate
   ```

## 🚀 Iniciar el Servidor de Desarrollo

1. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

2. **Visitar el sitio**
   - Abre tu navegador y ve a: http://127.0.0.1:8000/

## 📁 Estructura Básica del Proyecto

```
mi_proyecto/
    ├── manage.py
    ├── mi_proyecto/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── mi_app/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── views.py
        └── tests.py
```

## 🎨 Personalización Básica

1. **Configurar la base de datos en `settings.py`**
2. **Crear modelos en `models.py`**
3. **Definir vistas en `views.py`**
4. **Configurar URLs en `urls.py`**

## 🌟 Consejos Útiles

- Usa `python manage.py createsuperuser` para crear un usuario administrador
- Accede al panel de administración en `/admin`
- Mantén tu entorno virtual activado mientras trabajas en el proyecto
- Usa `pip freeze > requirements.txt` para guardar tus dependencias

## 🔍 Recursos Adicionales

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Tutorial de Django Girls](https://tutorial.djangogirls.org/)
- [Django para Principiantes](https://djangoforbeginners.com/)

¡Feliz desarrollo con Django! 🎉