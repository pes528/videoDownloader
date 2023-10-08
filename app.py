from flask import Flask, render_template, request, send_file, redirect, jsonify

from src.down import descarga, changeName
from src.info import getInfo
import os, re
from time import sleep




app = Flask(__name__)


info=None
url = None
descargado = False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/youtube", methods=['GET', 'POST'])
def inicio():
    global descargado
    if request.method == 'GET':
        descargado = False
        os.system('rm downloads/*')
        return render_template("youtube/download.html")
    else:
        letra = request.form['link']
        #datos = DescargaMp3(letra)
        datos = None
        global info
        descargado = False
        info = descarga(letra)
        opt = None
        print(letra)
        
        if re.search("^https.*youtu", letra) == None or info.info == '':
            datos = None
            opt = None
            
        else:
            datos = info.info
            opt = getInfo(datos)
            
            
            global url
            url = letra
            
        os.system('rm -rf downloads/*')
        return render_template('youtube/result.html', datos = datos, opt=opt)


@app.route('/desc', methods=['GET'])
def carga():
    
    if descargado == False:
        return jsonify({'descargado':False})
    else:
        return jsonify({'descargado':True
        })
    
        


@app.route('/descMp3', methods = ['GET', 'POST'])
def descMp3():
    if request.method == 'POST':
         
        global descargado
        
        if info != '':
            i = descarga(url)
            resp = i.downMp3()
            if  resp == True:
                descargado = True
                sleep(2)
                mp3 = changeName(i.title)+'.mp3'
                
                carga()
                
                return send_file(f"""downloads/{mp3}""", as_attachment=True)
            else:
                return ('no se pudo descargar')
    else:
        os.system('rm -rf downloads/*') 
        descargado = False
        return redirect('/')


@app.route('/descMp4', methods=['POST'])
def descMp4():
    
    value = request.form.get('mp4')
    nom = descarga(url)
    #obtenemos los datos, getInfo nos devuelve dos datos (codigoId, extension que QUEREMOS descargar)
    
    getInf = getInfo(nom.info)
    #tratamos de descargar el video, la funcion downmp4 nos devuelve dos datos,( bool, extension del archivo OFICIAL DESCARGADO no siempre se descarga con la que habiamos elegido)
    
    desc = nom.downMp4(getInf.get(value)[0])
    if desc[0] == True:
        
        #obtenemos la extension del video que se enviara al usuario
        extension = getInf.get(value)[1]
        #nombre del video que se descargo
        nomVideo = changeName(nom.getTitle())+'.' + desc[1]

        #nombre del video sera enviado al usuario
        title = changeName(nom.getTitle())+'.'+extension
        
        #cambiamos el nombre descargado por el que queremos enviar al usuario
        os.system(f'mv downloads/{nomVideo} downloads/{title}')
        
        return send_file(f'downloads/{title}', as_attachment=True)



@app.route('/tiktok', methods=['POST', 'GET'])
def tik():

    message = ''
    global descargado
    if request.method == 'POST':
        descargado = False

        os.system('rm downloads/*')
        linkTik = request.form['linkTikTok']
        resp = descarga(linkTik)
        wwwtiktok = "^https:.*tiktok.com/" #r'www.tiktok.com'
        
        message = '' if re.search(wwwtiktok, str(linkTik)) else 'Link incorrecto'
        
        if resp.info != '' and message != 'Link incorrecto':
            message = ''
            down = resp.tiktok()
            if down == True:
                descargado = True
                carga()
                return send_file('downloads/tiktok_Video.mp4', as_attachment=True)
            else:
                return redirect('/')
        else:

            
            return render_template('tiktok/tiktok.html', message=message)
    else:
        descargado = False
        os.system('rm downloads/*')
        return render_template('tiktok/tiktok.html', message=message)


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=3001, debug=False)
