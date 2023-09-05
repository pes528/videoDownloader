import subprocess, json, yt_dlp
from os import path

def changeName(titleName):
    words = """ )(*$#^&@-_=+'">%< """
    for i in words:
        titleName=titleName.replace(i, '')
    return titleName


class descarga():

    
    
    
    def __init__(self, url):
        self.title = None
        self.url = url
        self.comandos_info = ['yt-dlp', '--skip-download', '--dump-json', '--no-playlist', url]
        self.info = self.verify()


    def verify(self):
        resp = subprocess.run(self.comandos_info, capture_output=True, text=True)
        
        try:
            return json.loads(resp.stdout)
        except:
            return resp.stdout

    def downMp3(self):
        
        if self.info != '':
            self.title = self.info['title']
            config_dlpMp3 = {
                'paths': {'home':'downloads/'},
                
                'format': 'bestaudio/best',
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192',
                    }],
                'outtmpl':{
                'default':changeName(self.title),#'%(title)s.%(ext)s'.replace("'", ''),
                },
                }
    
            with yt_dlp.YoutubeDL(config_dlpMp3) as f:
                f.download([self.url])
            
            return True
        else:
            return False

    
        
    def downMp4(self, calidad):
        #opcion si queremos convertir el video en formato mp4 (el uso es opcional)
        """postProcessor = [
                    {
                        'key':'FFmpegVideoConvertor',
                        'preferedformat':'mp4',
                      
                    },]"""
        #--==========================================
        if self.info != '':
            self.title = self.info['title']
            config_dlpM4 = {
                'paths':{'home':'downloads/'},
                'format': calidad+'+bestaudio',
                'outtmpl':{
                    'default':changeName(self.title)+'.%(ext)s',
                },
            }
    
            with yt_dlp.YoutubeDL(config_dlpM4) as d:
                extVideoDescargado = d.extract_info(self.url, download=False)
                d.download([self.url])
            return (True, extVideoDescargado['ext'])
        else:
            return False

    def getTitle(self):
        return self.title

    def tiktok(self):
        config = {
            'paths':{'home':'downloads/'},
            'outtmpl':{
                'default':'tiktok_Video.%(ext)s'
            },
        }
        with yt_dlp.YoutubeDL(config) as t:
            try:
                t.download([self.url])
                return True
            except:
                return False