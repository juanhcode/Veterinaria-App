const campo = document.querySelectorAll('.campo');
for (let i = 0; i < campo.length; i++) {
    console.log(campo[i].children[1].type);
    campo[i].children[1].addEventListener('blur',(e)=>{
        if(e.target.value.length >= 0){
            campo[i].children[1].style.borderColor = 'red';
        }else{
            campo[i].children[1].style.borderColor = '#A2ABC2';
        }

        if(e.target.type == 'text'){
            if(e.target.value.length >= 1){
                campo[i].children[1].style.borderColor = '#A2ABC2';
            }
        }
        if(e.target.type == 'number'){
            if(e.target.value.length >= 1){
                campo[i].children[1].style.borderColor = '#A2ABC2';
            }
        }
        if(e.target.type == 'textarea'){
            if(e.target.value.length >= 1){
                campo[i].children[1].style.borderColor = '#A2ABC2';
            }
        }

    })

}

