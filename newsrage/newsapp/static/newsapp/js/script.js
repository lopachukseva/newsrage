
let upbutton = document.querySelector('.up-button');
let showtime = 200

// window.onload = () =>{
//     window.onscroll = () => {
//         if (window.scrollY > showtime){
//             upbutton.classList.add('up-button-hide')
//         }
//         if (window.scrollY < showtime){
//             upbutton.classList.remove('up-button-hide')
//         }
//     }
// }

window.onscroll = () => {
    if (window.scrollY > showtime){
        upbutton.classList.add('up-button-hide')
    }
    if (window.scrollY < showtime){
        upbutton.classList.remove('up-button-hide')
    }
}


upbutton.addEventListener('click', ()=>{
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
})
