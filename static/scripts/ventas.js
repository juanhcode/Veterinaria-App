const btnEditar = document.querySelector('.editar');
const btnEliminar = document.querySelector('.eliminar');
const celdaEditar = document.querySelectorAll('.celdaCrud');
const agregarIcono = document.querySelectorAll('.agregarIcono');


document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < celdaEditar.length; i++) {
        celdaEditar[0].style.display = 'none';  
    }
})


btnEditar.addEventListener('click', () => {
    celdaEditar[0].textContent = 'Editar';
    celdaEditar[0].style.display = 'block';
    for (let i = 0; i < agregarIcono.length; i++) {
        agregarIcono[i].classList.add('fa-solid')
        agregarIcono[i].classList.add('fa-crop');
    }
})

btnEliminar.addEventListener('click',()=>{
    celdaEditar[0].textContent = 'Eliminar';
    celdaEditar[0].style.display = 'block';
    for (let i = 0; i < agregarIcono.length; i++) {
        agregarIcono[i].classList.add('fa-regular')
        agregarIcono[i].classList.add('fa-trash-can');
    }
})

function abrir(){
    document.getElementById("elimi").style.display="block";
  }

  function cerrar(){
    document.getElementById("elimi").style.display="none";
  }

  function confirmar(){
    document.getElementById("elimi").style.display="none";
  }