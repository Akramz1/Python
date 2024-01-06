let stars1 = document.getElementById('stars')
let moon = document.getElementById('moon')
let mountains3 = document.getElementById('mountains3')
let mountains4 = document.getElementById('mountains4')
let river = document.getElementById('river')
let boat6 = document.getElementById('boat')
let solarsystem = document.querySelector('.solarsystem')
window.onscroll = function (){
    let value = scrollY;
    stars1.style.left = value + 'px';
    moon.style.top = value * 3 + 'px';
    solarsystem.style.fontSize = value + 'px';
    if(scrollY >= 67){
        solarsystem.style.fontSize = 67 + 'px';
        solarsystem.style.position = 'fixed';
        if(scrollY >= 424){
            solarsystem.style.display = 'none';
        }
        else{
            solarsystem.style.display = 'block';
        }
        if(scrollY >= 155){
            document.querySelector('.main').style.background = 'linear-gradient(#376281,#10001f)'
        }else{
            document.querySelector('.main').style.background = 'linear-gradient(#200016,#10001f)'
        }
    }
}