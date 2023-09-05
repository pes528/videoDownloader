/*La funcion recibe dos parametros()
1:Id de la imagen o su contenedor al que se aplicara el estilo 'grayscale()' (decolorar)
2 :Id del contenedor del cual el mouse pasara encima 'mouseover' 
*/
const anim = (IdSombrear, id2) =>{
    let obj = document.getElementById(IdSombrear);
    let obj2 = document.getElementById(id2);
    obj.style.filter = "grayscale()"
    obj2.style.width = "15rem";
    obj2.style.height = "15rem";
    obj2.addEventListener('mouseout', ()=>{
        obj.style.filter = "none";
        obj2.style.width = "10rem"
        obj2.style.height = '10rem';
    })
  }
  
  
  let yt = document.getElementById('yout');
  yt.addEventListener('mouseover', ()=>{
    anim("tikt", "yout");
  });
  
  let tt = document.getElementById('tikt');
  tt.addEventListener('mouseover', ()=>{
    anim("yout", "tikt");
  })