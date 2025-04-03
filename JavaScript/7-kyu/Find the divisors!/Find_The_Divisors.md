# Título: Find the divisors!

**Descrição:**
Crie uma função chamada `divisors/Divisors` isso leva um inteiro `n > 1` e retorna uma matriz com todos os divisores do número inteiro (exceto 1 e o próprio número), do menor para o maior. Se o número for primo, retorne a string '(inteiro) é primo' (`null` em C#, tabela vazia em COBOL) (uso `Either String a` em Haskell e `Result<Vec<u32>, String>` em Rust).

**Exemplos:**
```js
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
```