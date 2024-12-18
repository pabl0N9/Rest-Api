(function(){
    
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Seguro de que quieres eliminar a este estudiante?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();