# Ementa

- **Modelos Lineares de Otimização**
- **Programação Linear** 
- **Algoritmo Simplex**
- **Dualidade**
- **Análise de Sensibilidade**
- **Modelos de Redes**
    - Problemas de transporte
    - Designação
    - Caminho mais curto
    - Árvore geradora mínima
    - Fluxo máximo
    - Fluxo de custo mínimo
    - PERT/CPM
- **Programação Inteira**
- **Programação Não-Linear**

## Bibliografia

- N. Maculan, *Otimização Linear*

---

# Introdução

Ramo da Ciência que lida com a otimização do desempenho de sistemas.

## Otimização

- **Maximizar**:
    - Lucro
    - Satisfação
- **Minimizar**:
    - Custos
    - Riscos

# Programação Linear

## Função Objetivo

- **Minimizar**: Custo, tempo, risco, poluição.
- **Maximizar**: Lucro, qualidade, segurança.
- **Encontrar**: Qualquer solução viável que atenda a requisitos específicos.

## Restrições

- **Disponibilidade** de recursos.
- **Operacionais**: Horários de trabalho, tempo de máquina.
- **Limites**: Venda em escala.

### Problema da Mistura

- Materiais disponíveis são combinados para gerar novos produtos com características convenientes.
- Um dos primeiros problemas de otimização linear implementados com sucesso na prática.

#### Abordagens

- Ração
- Ligas metálicas
- Composição de filtros de areia

---

# Exercício

## Enunciado

Suponha que o mínimo de vitaminas necessário por dia é de 32 unidades e o mínimo de proteínas é de 36 unidades. Cada unidade de carne fornece 8 vitaminas e 6 proteínas, custando R$3,00. Cada unidade de ovo fornece 4 vitaminas e 6 proteínas, custando R$2,50.

**Pergunta:** Qual a quantidade diária de ovo ou carne necessária para suprir os requisitos nutricionais com o custo mínimo?

## Resolução do Professor

### Variáveis de Decisão

- \(x_1\): Quantidade de carne comprada
- \(x_2\): Quantidade de ovos comprados

### Custo de uma Solução

- Preço da carne: R$3,00
- Preço dos ovos: R$2,50

### Função Objetivo

\[
\text{Minimizar} \quad z = 3x_1 + 2,5x_2
\]

### Restrições

As soluções devem satisfazer os requisitos nutricionais:

| Nutrientes  | Quantidade Mínima |
|-------------|-------------------|
| Vitaminas   | 32                |
| Proteínas   | 36                |

Portanto, o modelo matemático é:
$$
\[
\begin{aligned}
\text{Minimizar} \quad & z = 3x_1 + 2,5x_2 \\
\text{sujeito a:} \quad & 8x_1 + 4x_2 \geq 32 \quad (\text{vitaminas}) \\
                        & 6x_1 + 6x_2 \geq 36 \quad (\text{proteínas}) \\
                        & x_1 \geq 0, \quad x_2 \geq 0
\end{aligned}
\]
$$
Este modelo pode ser resolvido usando métodos de programação linear, como o **Algoritmo Simplex**.

