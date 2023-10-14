const btn = document.getElementById("btn");
let contador = 0;

btn.addEventListener("click", () => {
    let container = document.querySelector(".main");   
    container.innerHTML = contador++;
    
    if(contador > 11) {
        
        btn.innerHTML = "<h1>Quebrei</h1>";
        btn.style.background = "rgb(226, 67, 67)";
        container.style.display = "none";
    }
    
})

// let x = 15

// while (x > 0) {
//     console.log(x)
//     x--
// }