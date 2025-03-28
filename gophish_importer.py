import requests
import csv
import json
import os
from urllib.parse import urljoin

def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje + " [s/n]: ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'

def cargar_csv(ruta_csv):
    targets = []
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                targets.append({
                    "first_name": row["First Name"],
                    "last_name": row["Last Name"],
                    "position": row["Position"],
                    "email": row["Email"]
                })
    except Exception as e:
        print(f"❌ Error al leer el CSV: {e}")
        exit(1)
    return targets

def comprobar_conexion(api_url, api_key, verify_ssl):
    try:
        response = requests.get(
            urljoin(api_url, "/api/groups/"),
            headers={"Authorization": f"Bearer {api_key}"},
            verify=verify_ssl
        )
        if response.status_code == 200:
            return True, response.json()
        else:
            print(f"❌ Error de conexión: Código {response.status_code}")
            print(response.text)
            return False, None
    except requests.exceptions.SSLError as ssl_err:
        print("⚠️ Error SSL detectado:", ssl_err)
        return None, None
    except Exception as e:
        print("❌ Error al conectar con GoPhish:", e)
        return False, None

def crear_grupo(api_url, api_key, grupo_nombre, targets, verify_ssl):
    data = {
        "name": grupo_nombre,
        "targets": targets
    }
    response = requests.post(
        urljoin(api_url, "/api/groups/"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json=data,
        verify=verify_ssl
    )
    if response.status_code == 200:
        print("✅ Grupo creado correctamente.")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print(f"❌ Error al crear el grupo: {response.status_code}")
        print(response.text)

# --- PROGRAMA PRINCIPAL ---
print("🔐 Asistente para importar usuarios en GoPhish desde un CSV")

# Pedir CSV
csv_path = input("📄 Ruta al archivo CSV: ").strip()
if not os.path.exists(csv_path):
    print("❌ El archivo no existe.")
    exit(1)

# Cargar datos
targets = cargar_csv(csv_path)

# Pedir datos de GoPhish
api_url = input("🌐 URL base de GoPhish (ej: https://localhost:3333): ").strip()
api_key = input("🔑 API Key de GoPhish: ").strip()

# Probar conexión
verify_ssl = True
ok, grupos = comprobar_conexion(api_url, api_key, verify_ssl)

if ok is None:
    # Preguntar si omitir verificación SSL
    if pedir_si_no("El certificado SSL es inválido. ¿Deseas omitir la verificación?"):
        verify_ssl = False
        ok, grupos = comprobar_conexion(api_url, api_key, verify_ssl)
    else:
        print("🔒 Abortado por error en certificado SSL.")
        exit(1)

if not ok:
    print("❌ No se pudo conectar a GoPhish con los datos proporcionados.")
    exit(1)

# Mostrar grupos existentes
grupo_nombre = input("📛 Nombre del nuevo grupo a crear: ").strip()
existe = any(grupo.get("name") == grupo_nombre for grupo in grupos)

if existe:
    print("⚠️ Ya existe un grupo con ese nombre. Por favor, elige otro.")
    exit(1)

# Crear grupo
crear_grupo(api_url, api_key, grupo_nombre, targets, verify_ssl)