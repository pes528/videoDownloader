
# Video downloader (tiktok, youtube)
Herramienta para descargar videos desde yotube (mp3, mp4, m4a, webm) y tiktok (sin marca de agua)


## Instalacion en linux (ubuntu)

La instalacion puede variar de acuerdo
a tu sistema operativo

Detalles a tener en cuenta:
El servidor corre en el servidor local : puerto 3001, se puede hacer cambio del puerto desde app.py/app.run(localhost, port)
Tambien los archivos javascript static/scripts/youtube.js y tiktok.js /const LOCALHOST = ''; 



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
Despues de la instalacion, el servidor estara funcionando en la direccion web "http://127.0.0.1:3001" 

Para detener el servidor -> ctrl+c  

## Author
- Telegram : [@pes528](https://t.me/pes528)


