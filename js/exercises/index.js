function parOuImpar(number) {
    if (number % 2 == 0) {
        console.log(`O numero: ${number} e par!`)
    } else {
        console.log(`O numero: ${number} e impar`)
    }

    return number
}

// parOuImpar(45943);

function fatorial(number) {

    // essa verificacao e por que na condicao fatorial o fatorial de 0 e 1 
    // e o fatorial de 1 e 1 mesmo.
    if (number === 0 || number === 1) return 1;

    let inicialValue = 1;

    // dentro do laco for, inicializamos a variavel i com 2, por que o fatorial de 1 e 1 mesmo
    // logo nao faz sentido inicializar com 1, e tambem ja inicializamos a outra vazriavel com
    // 1;
    // na condicao dentro do for, podemos ler assim: 
    // enquanto i <= number execute o bloco {}, e o laco so vai parar o loop i++, quando a 
    // condicional nao for mais verdadeira.
    // por fim retornamos o valor final depois de ter feito a verificao...
    for (let i = 2; i <= number; i++) {
        console.log(`Multiplicando ${inicialValue} × ${i}`);
        inicialValue *= i;
    }

    console.log(`Resultado final: ${inicialValue}`);
    return inicialValue;
}

//fatorial(6);

// A sequência de Fibonacci é uma sequência numérica onde:

//  - cada número é a soma dos dois anteriores.



function Fibonacci(n) {
    if (n === 0) return [];
    if (n === 1) return [0];

    let sequencia = [0, 1];

    for (let i = 2; i <= n; i++) {
        let next = sequencia[i - 1] + sequencia[i - 2];

        sequencia.push(next);

        console.log(`Posição ${i}: ${next}`);
    }

    return sequencia;
}

Fibonacci(10)

