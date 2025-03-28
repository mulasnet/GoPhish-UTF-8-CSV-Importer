# 📥 GoPhish CSV Importer (UTF-8 friendly)

Este script en Python ha sido diseñado para importar automáticamente usuarios desde un archivo CSV a un grupo en **GoPhish**, utilizando su API REST de forma segura y guiada paso a paso.

---

## ❗ Problema que resuelve

GoPhish presenta problemas al importar archivos CSV directamente desde la opción de "Bulk Import" cuando estos contienen **caracteres especiales o tildes**, mostrándolos como:

```
Jos� P�rez
```

Esto ocurre debido a errores de codificación (ej. Latin-1 o UTF-8 con BOM). Este script soluciona ese problema importando datos correctamente codificados en **UTF-8 sin BOM** a través de la **API oficial de GoPhish**.

---

## 🧠 ¿Qué hace este script?

✅ Lee un archivo CSV codificado en UTF-8  
✅ Pregunta los datos de conexión a GoPhish  
✅ Detecta certificados SSL autofirmados  
✅ Comprueba si la API Key es válida  
✅ Verifica si el grupo ya existe  
✅ Crea el grupo con usuarios si no existe  
✅ Importa correctamente nombres con tildes, eñes, etc.

---

## 📋 Requisitos

- Python 3.6 o superior
- Módulo `requests`

Instalación de dependencias:

```bash
pip install requests
```

---

## 📁 Formato esperado del CSV

```csv
First Name,Last Name,Position,Email
José,Pérez,Analista,jose.perez@ejemplo.com
María,López,Contable,maria.lopez@ejemplo.com
```

Guarda el archivo con **codificación UTF-8 sin BOM**.

---

## 🚀 Cómo usarlo

Ejecuta el script desde terminal:

```bash
python importar_usuarios_gophish.py
```

El asistente te guiará preguntando:

- 📄 Ruta del archivo CSV  
- 🌐 URL de tu servidor GoPhish (ej. https://localhost:3333)  
- 🔑 Tu API Key  
- 🛡 Si deseas ignorar el certificado SSL si está autofirmado  
- 📛 Nombre del nuevo grupo a crear  

---

## 🧑‍💻 Ejemplo de sesión

```bash
📄 Ruta al archivo CSV: empleados.csv
🌐 URL base de GoPhish (ej: https://localhost:3333): https://localhost:3333
🔑 API Key de GoPhish: ********************
⚠️ El certificado SSL es inválido. ¿Deseas omitir la verificación? [s/n]: s
📛 Nombre del nuevo grupo a crear: Personal Marzo
✅ Grupo creado correctamente.
```

---

## 🔒 Seguridad

Este script te permite **ignorar certificados SSL no válidos** (útil para entornos de pruebas o servidores locales). **No se recomienda** desactivar la verificación SSL en entornos de producción.

---

## 🧾 requirements.txt

```
requests
```

