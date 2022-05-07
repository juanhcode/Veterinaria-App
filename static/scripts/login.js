const documento = document.getElementById("documento");
console.log(documento.value);
const form = document.querySelector('form')

form.addEventListener('submit',(e)=> {
    console.log(documento.value + "" );
    localStorage.setItem('documentologin', documento.value);
})