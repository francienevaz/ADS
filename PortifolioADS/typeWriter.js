let i = 0;

let tag = document.querySelector(".line");
let html = document.querySelector(".line").innerHTML;
let attr = tag.setAttribute("data", html);
let txt = tag.getAttribute("data");
let speed = 100;

function typeWriter() {
    if (i <= txt.length) {
    document.querySelector(".line").innerHTML = txt.slice(0 , i + 1);
    i++;
    setTimeout(typeWriter, speed);
    }
}

typeWriter();