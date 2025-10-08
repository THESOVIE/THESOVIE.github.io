import requests
import json
import sys

# Tu URL de GitHub Pages
URL_BASE = "https://thesovie.github.io"

def verificar_juegos_json():
    print("?? Verificando juegos.json...")
    try:
        r = requests.get(f"{URL_BASE}/juegos.json")
        if r.status_code == 200:
            try:
                datos = r.json()
                if isinstance(datos, list) and len(datos) > 0:
                    print("? juegos.json existe y es válido.")
                    return True
                else:
                    print("? juegos.json está vacío o no es un array.")
                    return False
            except json.JSONDecodeError:
                print("? juegos.json no es un JSON válido.")
                return False
        else:
            print(f"? juegos.json no encontrado (Error {r.status_code}).")
            return False
    except Exception as e:
        print(f"? Error al acceder a juegos.json: {e}")
        return False

def verificar_firebase():
    print("?? Verificando configuración de Firebase en juego.html...")
    try:
        r = requests.get(f"{URL_BASE}/juego.html")
        if r.status_code == 200:
            contenido = r.text
            if 'TU_API_KEY' in contenido or 'TU_PROYECTO' in contenido:
                print("? Firebase aún tiene valores de ejemplo (TU_API_KEY).")
                return False
            elif 'apiKey' in contenido and 'projectId' in contenido:
                print("? Firebase está configurado con credenciales reales.")
                return True
            else:
                print("? Firebase no está configurado en juego.html.")
                return False
        else:
            print(f"? No se pudo cargar juego.html (Error {r.status_code}).")
            return False
    except Exception as e:
        print(f"? Error al acceder a juego.html: {e}")
        return False

def verificar_carga_juegos():
    print("?? Verificando carga de juegos en index.html...")
    try:
        r = requests.get(f"{URL_BASE}/index.html")
        if r.status_code == 200:
            contenido = r.text
            if 'Cargando juegos...' in contenido and 'gamesContainer' in contenido:
                print("?? index.html está intentando cargar juegos (depende de juegos.json).")
                return True
            else:
                print("? index.html no tiene la lógica de carga de juegos.")
                return False
        else:
            print(f"? No se pudo cargar index.html (Error {r.status_code}).")
            return False
    except Exception as e:
        print(f"? Error al acceder a index.html: {e}")
        return False

def main():
    print("?? Verificando estado de Games Hot...\n")
    
    paso1 = verificar_juegos_json()
    paso2 = verificar_firebase()
    paso3 = verificar_carga_juegos()
    
    print("\n" + "="*50)
    if paso1 and paso2 and paso3:
        print("?? ¡Todo está configurado correctamente!")
        print("Tu web debería funcionar con contadores y juegos.")
    else:
        print("?? Problemas detectados:")
        if not paso1:
            print("  - Sube juegos.json a tu repositorio.")
        if not paso2:
            print("  - Reemplaza TU_API_KEY por tu configuración real de Firebase.")
        if not paso3:
            print("  - Asegúrate de que index.html tenga la lógica de carga.")
    print("="*50)

if __name__ == "__main__":
    main()