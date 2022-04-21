const botonDark = document.querySelector('.dark');
const body = document.querySelector('body');
const h1 = document.querySelector('h1');
const sales = document.querySelector('.sales');
const parrafo = document.querySelector('.descripcion');
const logo = document.querySelector('.top');
const tituloLogo = document.querySelector('.title');
const sidebar = document.querySelector('.sidebar');
const infoAdmin = document.querySelector('.info');
console.log(sidebar)
botonDark.addEventListener('click',()=>{
    body.style.backgroundColor ='#363949';
    body.style.transition='all 300ms ease';
    h1.style.color='white';
    tituloLogo.style.color='white';
    parrafo.style.color = 'white';
    logo.style.backgroundColor='#363949'
    infoAdmin.style.color = 'white';
    //sidebar.style.backgroundColor='#363949';
})