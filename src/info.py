import json

#devolvera un diccionario:ejemplo {"m4a 1.06mb 139 - audio only (low)": ["codigo_id", "extension del archivo"]}
def getInfo(info:dict) -> dict:
    
        
    with open('dump.json', 'w') as f:
        json.dump(info, f, indent=4)

    with open('dump.json') as f:
        format = json.load(f)
  
    #data = []
    data = {}
    for u in format['formats']:
        try:
            mb = u['filesize']
            if (mb != None):
                mb = mb/1000000
                print(u['ext'],round(mb, 2), u['format'])
                #data.append((u['ext'],round(mb, 2), u['format']))
                #data[u['format_id']] = (u['ext'], str(round(mb, 2))+'mb', u['format'])
                
#creamos el diccionario con las keys ext, peso, formato, unidos como un string y como value tendra el codigo id del video y el formato
                data[' '.join([u['ext'], str(round(mb, 2))+'mb', u['format']])]=[u['format_id'], u['ext']]

            else:
                pass
        except KeyError:
            pass
    return (data)


