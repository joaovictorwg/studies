Um problema de programação linear PPL pode ser escrito em uma forma padrão definida como:
    minimizar     z=c1x1 + c2x2 + ... + cnxn
    sujeito a     a11x1 + a12

Forma padrão de qualquer programa linear 
    Função objetivo (maximização e minimização)
    z* = max somatorio CjXj = - min somatorio -CjXj

variaveis de folga
    cada restrição de desigualdade pode ser substituida com o acrescimo de uma variavel Yi >= 0, por uma restrição de igualdade e uma restrição trivial
    g    
        Ai1x1 + Ai2X2 + ... + AinXn >= B1 <=> 

---
# Resolução de Problema de Programação Linear (PL) pelo Método Gráfico

## PL - Resolução pelo Método Gráfico

### Considere o PPL:
Maximizar:
\[
z = 6x_1 + 8x_2
\]

Sujeito a:
\[
30x_1 + 20x_2 \leq 300
\]
\[
5x_1 + 10x_2 \leq 110
\]
\[
x_1, x_2 \geq 0
\]

### Resolução:
Resolver um PPL consiste em encontrar uma solução ótima, isto é, para um problema de maximização, consiste em determinar uma solução viável \(x^*\) tal que \(f(x^*) \geq f(x)\), para todo \(x\) viável.

#### Região viável:
\[
X = \{(x_1, x_2) \in \mathbb{R}^2 \mid 30x_1 + 20x_2 \leq 300, 5x_1 + 10x_2 \leq 110, x_1 \geq 0, x_2 \geq 0\}
\]
