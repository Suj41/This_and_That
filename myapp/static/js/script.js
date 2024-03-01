// Script for navigation bar
const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');

if (bar ){
    bar.addEventListener("click", () => {
        // JavaScript code
        nav.classList.add('active');
    })
}

if (close ){
    close.addEventListener("click", () => {
        // JavaScript code
        nav.classList.remove('active');
    })
}
