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

let exeObj = {


    nr: 500,
  
  
    str: "palavra"
  
  
  };
  
console.log(exeObj.nr);
console.log(exeObj.str); 

let Teste = 'teste';
let teste = 'outro teste';
let TeSte = 'terceiro teste';

console.log(Teste, teste, TeSte);

let array = ['Lucas', 'Marcos', 'Pedro', 'Patricia'];

console.log(array.indexOf('Patricia'));

let nome1= 'Anna';


{


    let idade1=25;


    console.log(nome1);


    console.log(idade1);


}


console.log(nome1);


console.log(idade1);