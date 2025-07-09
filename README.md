<div align="center">

# 🌟 Django Master Guide 🌟

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

<p align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="Django Logo" width="300">
</p>

_¡Tu guía definitiva para dominar Django!_ 🚀

[🌐 Documentación](https://docs.djangoproject.com/) |
[📚 Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) |
[🤝 Contribuir](#contribuir)

</div>

---

## 📋 Tabla de Contenidos

- [🎯 Requisitos Previos](#requisitos-previos)
- [🔧 Entorno 410](#entorno-410)
- [⚡ Instalación Rápida](#instalación-rápida)
- [🛠️ Configuración del Proyecto](#configuración-del-proyecto)
- [📱 Desarrollo](#desarrollo)
- [🌟 Características Principales](#características-principales)
- [📚 Recursos de Aprendizaje](#recursos-de-aprendizaje)

## 🎯 Requisitos Previos

<details>
<summary>Click para expandir</summary>

- ✅ Python 3.8 o superior
- ✅ pip (gestor de paquetes de Python)
- ✅ Conocimientos básicos de terminal/línea de comandos
- ✅ Editor de código (recomendado: VS Code, PyCharm)

</details>

## 🔧 Entorno 410

### ¿Qué es el Entorno 410?

El **Entorno 410** es un entorno virtual de Python específicamente configurado para este proyecto Django. Se encuentra ubicado en la carpeta `entorno_410/` y contiene todas las dependencias necesarias para ejecutar este proyecto de manera aislada.

### 🗂️ Estructura del Entorno

```plaintext
entorno_410/
├── 📂 Scripts/           # Scripts de activación
│   ├── activate          # Activación (Linux/macOS)
│   ├── activate.bat      # Activación (Windows)
│   └── Activate.ps1      # Activación (PowerShell)
├── 📂 Lib/              # Bibliotecas instaladas
│   └── 📂 site-packages/ # Paquetes Python
├── 📂 Include/           # Archivos de inclusión
└── 📄 pyvenv.cfg         # Configuración del entorno
```

### 🚀 Cómo Activar el Entorno 410

#### Windows (PowerShell/CMD)
```powershell
# PowerShell
.\entorno_410\Scripts\Activate.ps1

# CMD
.\entorno_410\Scripts\activate.bat
```

#### Linux/macOS
```bash
source entorno_410/bin/activate
```

### 📦 Dependencias Instaladas

El entorno 410 incluye las siguientes dependencias principales:

- **Django 3.0.3** - Framework web principal
- **asgiref 3.9.1** - Interfaz ASGI
- **pytz 2025.2** - Soporte de zonas horarias
- **sqlparse 0.5.3** - Parser SQL
- **pip 24.2** - Gestor de paquetes

### 🔍 Verificar Activación

Cuando el entorno esté activado, verás `(entorno_410)` al inicio de tu línea de comandos:

```bash
(entorno_410) C:\Users\Acer\OneDrive\Desktop\Django_Prueba>
```

### ⚙️ Configuración del Proyecto

Este proyecto Django está configurado con:

- **Proyecto principal**: `mi_proyecto/`
- **Aplicación**: `mi_proyecto/` (vistas y lógica)
- **Archivo de configuración**: `mi_proyecto/settings.py`
- **URLs principales**: `mi_proyecto/urls.py`

### 🎯 Funcionalidades del Proyecto

El proyecto incluye múltiples vistas de ejemplo que demuestran:

- ✅ **Vistas básicas** - Saludos y cálculos
- ✅ **Formularios HTML** - Registro, login, formularios
- ✅ **Páginas con CSS** - Headers, mains, sections
- ✅ **Templates Django** - Uso de loader, render
- ✅ **Contenido multimedia** - Videos y contenido HTML

### 🛠️ Comandos Útiles

```bash
# Activar entorno
.\entorno_410\Scripts\Activate.ps1

# Ejecutar servidor
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```

### 🔧 Solución de Problemas

#### Error de Activación en PowerShell
Si tienes problemas con la política de ejecución en PowerShell:

```powershell
# Cambiar política de ejecución (como administrador)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Verificar Instalación
```bash
# Verificar Django
python -c "import django; print(django.get_version())"

# Verificar entorno activo
echo $env:VIRTUAL_ENV
```

## ⚡ Instalación Rápida

### 1️⃣ Configuración del Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2️⃣ Instalación de Django

```bash
# Instalar Django
pip install django

# Verificar instalación
django-admin --version
```

## 🛠️ Configuración del Proyecto

### Crear Nuevo Proyecto

```bash
# Crear proyecto
django-admin startproject mi_proyecto
cd mi_proyecto

# Crear aplicación
python manage.py startapp mi_app

# Migraciones iniciales
python manage.py migrate
```

### 🌐 Iniciar el Servidor

```bash
python manage.py runserver
```

> 🌟 Visita http://127.0.0.1:8000/ en tu navegador

## 📱 Desarrollo

### 📁 Estructura del Proyecto

```plaintext
mi_proyecto/
├── 📂 manage.py
├── 📂 mi_proyecto/
│   ├── 📄 __init__.py
│   ├── 📄 settings.py   # Configuración principal
│   ├── 📄 urls.py      # URLs del proyecto
│   └── 📄 wsgi.py      # Configuración WSGI
└── 📂 mi_app/
    ├── 📄 models.py    # Modelos de datos
    ├── 📄 views.py     # Lógica de la aplicación
    └── 📄 tests.py     # Pruebas unitarias
```

## 🌟 Características Principales

### 🔐 Panel de Administración

```bash
# Crear superusuario
python manage.py createsuperuser
```

> 🔍 Accede a `/admin` para gestionar tu aplicación

### 📦 Gestión de Dependencias

```bash
# Guardar dependencias
pip freeze > requirements.txt

# Instalar dependencias
pip install -r requirements.txt
```

## 📚 Recursos de Aprendizaje

### 🎓 Tutoriales Recomendados

- [Django Girls Tutorial](https://tutorial.djangogirls.org/es/) - Perfecto para principiantes
- [MDN Django Tutorial](https://developer.mozilla.org/es/docs/Learn/Server-side/Django) - Tutorial completo
- [Real Python Django](https://realpython.com/django-web-framework/) - Tutoriales avanzados

### 💡 Consejos Pro

- ✨ Usa nombres descriptivos para tus modelos y vistas
- 🔒 Nunca compartas la SECRET_KEY
- 📝 Documenta tu código
- 🧪 Escribe pruebas unitarias

### 🤝 Contribuir

1. 🍴 Haz un fork del proyecto
2. 🔧 Crea tu rama de características
3. 💻 Haz tus cambios
4. 📤 Envía un pull request

---

<div align="center">

### 🌟 ¡Feliz Desarrollo con Django! 🌟

_Hecho con ❤️ para la comunidad de desarrolladores_

</div>