
# Video downloader (tiktok, youtube)

Descarga videos desde yotube (mp3, mp4, m4a, webm) y tiktok (sin marca de agua)


## Instalacion en linux (ubuntu)

La instalacion puede variar de acuerdo
a tu sistema operativo

Detalles a tener en cuenta:
El servidor corre en tu localhost con el puerto 3001, si deseamos modificar esto se puede hace desde app.py/app.run(localhost, port)
Y los archivos javascript static/scripts/youtube.js y tiktok.js /const LOCALHOST = ''; 



```bash
  apt install ffmpeg
  git clone https://github.com/pes528/videoDownloader.git
  cd videoDownloader
  source venv/bin/activate
  pip install -r requirements.txt
  python app.py
```

## Dependencias
- Python 3.8+
- ffmpeg
- flask
- yt-dlp

## Uso
Despues de la instalacion, debes verificar que el servidor flask este funcionando correctamente (despues de seguir los pasos de instalacion)
luego abre el link "http://127.0.0.1:3001" en tu navegador y listo !1


Para detener el servidor flask, preciona ctrl+c en la consola 

