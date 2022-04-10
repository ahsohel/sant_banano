window.onload = (event) => {
    localStorage.getItem('cookie_box') === 'hide' ? cookieHide() : cookieShow();
}

function cookieHide(){
    console.log('monna')
    var cookie_box = document.getElementById('cookie_box');
    cookie_box.classList.remove('show');
    localStorage.setItem('cookie_box', 'hide');
}

function cookieShow(){
    var cookie_box = document.getElementById('cookie_box');
    cookie_box.classList.add('show');
    localStorage.setItem('cookie_box', 'show');
}

$(document).ready(function () {
    /********* aos animations ********/
    AOS.init({
        duration: 800,
        easing: 'ease',
        once: true
    });
});
