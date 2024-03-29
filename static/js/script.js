const upbutton = document.querySelector('.up-button');
const showtime = 200

window.onscroll = () => {
    if (window.scrollY > showtime) {
        upbutton.classList.add('up-button-hide')
    }
    if (window.scrollY < showtime) {
        upbutton.classList.remove('up-button-hide')
    }
}


upbutton.addEventListener('click', () => {
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
})


const headerNavExpand = document.querySelector('.header-navigation-expand');
const headerNavListItems = document.querySelectorAll('.header-navigation-textlink');
const headerNavList = document.querySelector('.header-navigation-list');


headerNavExpand.addEventListener('click', () => {
    if (headerNavExpand.classList.contains('reversed')) {
        headerNavExpand.classList.remove('reversed');

        headerNavListItems.forEach(element => {
            element.classList.add('header-navigation-textlink-hide');
        });
        headerNavList.style.gap = "0px";
    }
    else {
        headerNavExpand.classList.add('reversed');
        headerNavList.style.gap = "30px";
        headerNavListItems.forEach(element => {
            element.classList.remove('header-navigation-textlink-hide');
        });
    }
});