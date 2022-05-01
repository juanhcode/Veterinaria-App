const btnEditar = document.querySelector('.editar');
const btnEliminar = document.querySelector('.eliminar');

const table = document.querySelector('table');
const propiedad = document.querySelector('.propiedad');
const valores = document.getElementById('valores');
const celdaEditar = document.querySelector('.celdaCrud');
const btnAgregar = document.querySelector('.agregar');

const agregarIcono = document.querySelector('.agregarIcono');


document.addEventListener('DOMContentLoaded', () => {
    celdaEditar.style.display = 'none';
})

btnEditar.addEventListener('click', () => {
    celdaEditar.textContent = 'Editar';
    celdaEditar.style.display = 'block';
    console.log(agregarIcono);
    agregarIcono.classList.add('fa-solid')
    agregarIcono.classList.add('fa-crop');
    for (let i = 0; i < valores.cells.length; i++) {
        console.log(valores.cells[6]);
    }
})

btnAgregar.addEventListener('click', () => {
    celdaEditar.textContent = 'Agregar';
    celdaEditar.style.display = 'block';
    console.log(agregarIcono);
    agregarIcono.classList.add('fa-solid')
    agregarIcono.classList.add('fa-plus');
    for (let i = 0; i < valores.cells.length; i++) {
        console.log(valores.cells[6]);
    }
})

btnEliminar.addEventListener('click',()=>{
    celdaEditar.textContent = 'Eliminar';
    celdaEditar.style.display = 'block';
    agregarIcono.classList.add('fa-regular')
    agregarIcono.classList.add('fa-trash-can');
    for (let i = 0; i < valores.cells.length; i++) {
        console.log(valores.cells[6]);
    }
})