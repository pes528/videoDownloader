

const LOCALHOST = 'http://127.0.0.1:3001';



document.getElementById('tiktok').addEventListener('click', ()=>{
    
    let consulta = setInterval(async ()=>{
        let resp = await fetch(LOCALHOST+'/desc');
        let re = await resp.json();
        if(re.descargado == false){
            console.log(re);
            if (document.getElementById('message').value == "Link incorrecto"){
            clearInterval(consulta)
            }else{
            document.getElementById('image_tiktok').style.animation = 'tt 1s infinite';
            document.getElementById('message').innerText = 'Descargando..';
        }
        }else{
            document.getElementById('image_tiktok').style.animation = 'none';
            document.getElementById('message').innerText = 'Descargado';

        }
    }, 1500)
});
