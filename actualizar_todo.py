import os

# Tus datos reales
reemplazos = {
    "https://t.me/tu_canal": "https://t.me/+rrlCyGExPJo3MzEx",
    "https://discord.gg/tu-invite": "https://discord.gg/pzjjTbkc",
    "https://t.me/tu_canal_tutoriales": "https://t.me/+_FJ5U1pqRs1hMWJh",
    "tucorreo@gmail.com": "gameshotboss@gmail.com"
}

# Archivos a actualizar
archivos = [
    "index.html", "juego.html", "vip.html", "gracias.html",
    "vip-access.html", "admin-vip-generator.html", "tutoriales.html", "contacto.html"
]

for archivo in archivos:
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        for viejo, nuevo in reemplazos.items():
            contenido = contenido.replace(viejo, nuevo)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"? {archivo} actualizado")