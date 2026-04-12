const modal = document.getElementById('modal')
const content = document.getElementById('modal-content')

function openModal(){
    modal.classList.remove('hidden')
    modal.classList.add('flex')

    setTimeout(()=>{
        content.classList.remove('scale-95', 'opacity-0')
    }, 10)
}

function closeModal(){
    content.classList.add('scale-95', 'opacity-0')
    
    setTimeout(()=>{
        modal.classList.add('hidden')
        modal.classList.remove('flex')
    }, 200)
}

document.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape'){
        closeModal()
    }
})