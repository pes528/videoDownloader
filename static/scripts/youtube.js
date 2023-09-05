
const LOCALHOST = 'https://61e2-34-138-210-8.ngrok-free.app';


document.getElementById('descargar').addEventListener('click', async () =>{
    setTimeout(()=>{
        
        document.getElementById('form').innerHTML='';
        document.getElementById('form2').innerHTML='';
    }, 1500)
    
    
    let interval = setInterval(async () =>{
            let get = await fetch(`${LOCALHOST}/desc`);
            let resp = await get.json()
            if(resp.descargado == true){
                console.log(resp)

                document.getElementById('loading').innerText='LISTO';
                clearInterval(interval)
            }else{
                document.getElementById('loading').style.display='flex';
                console.log(resp)
            }
        }, 1500)
    
})


