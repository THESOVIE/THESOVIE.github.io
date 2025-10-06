import os
reemplazos = {
    "https://t.me/tu_canal": "https://t.me/+rrlCyGExPJo3MzEx",
    "https://discord.gg/tu-invite": "https://discord.gg/pzjjTbkc",
    "https://t.me/tu_canal_tutoriales": "https://t.me/+_FJ5U1pqRs1hMWJh",
    "tucorreo@gmail.com": "gameshotboss@gmail.com"
}
archivos = ["index.html", "juego.html", "vip.html", "gracias.html", "vip-access.html", "admin-vip-generator.html", "tutoriales.html", "contacto.html"]
for archivo in archivos:
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            c = f.read()
        for v, n in reemplazos.items():
            c = c.replace(v, n)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"? {archivo}")