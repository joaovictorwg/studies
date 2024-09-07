# AULA 3

## Criptografia

- **Termo de origem grega** que significa escrita secreta.
- Permite que dois indivíduos troquem mensagens confidenciais por um canal inseguro.
- A mensagem só poderá ser revelada com a presença de uma chave secreta, conhecida apenas pelo remetente e pelo destinatário (usuários autorizados).
- **Cifra de César**: A -> 3, B -> 4, C -> 5 ... Z -> 28.

### Passos para Criptografia:
1. Texto em claro -> Cifragem -> Texto Cifrado -> Decifragem -> Texto em claro

### Conceitos:

- **Texto em Claro ou Dado Decifrado:**
  - Informação inteligível ou desprotegida.
  - Informação antes de ser protegida.
  - Recuperar o texto em claro é o objetivo do perito.

- **Texto Cifrado, Criptograma ou Dado Criptografado:**
  - Informação ininteligível ou protegida.
  - Seu conteúdo só poderá ser obtido com a chave.

- **Chave:**
  - Sequência de bits utilizada em conjunto com o algoritmo criptográfico para converter o texto em claro em um criptograma.
  - Seu conteúdo deve permanecer secreto e seu tamanho varia de acordo com o algoritmo utilizado.

- **Cifra ou Algoritmo Criptográfico:**
  - Método ou algoritmo que tem como entrada o texto em claro e a chave, e como saída o criptograma (e vice-versa).
  - Processo direto é chamado de cifragem, cifrar ou criptografar.
  - Processo inverso — reverter o criptograma para texto em claro — é chamado de decifragem ou decifrar.

### Por que Utilizar Criptografia? (Uso Devido):
- Sigilo, privacidade, anonimato.
- Comércio eletrônico.
- Assinatura digital.
- Votação eletrônica.
- Moeda digital.

### Problemas (Uso Indevido):
- Redes de pornografia infantil.
- Crime organizado e crimes de colarinho branco.
- Tráfico de drogas.
- Terrorismo.
- Sequestro de dados (ransomware).
- Darknet (não confundir com deep web).

### Auguste Kerckhoffs:
- Linguista e criptologista holandês.

- **Princípio de Kerckhoffs:**
  - A segurança de um criptossistema não deve depender da manutenção de um algoritmo em segredo. A segurança depende apenas de se manter a chave em segredo.

### Propriedades de Criptografia:

- **Difusão:**
  - Dissipação das características do texto claro de tal forma que não apareçam no texto cifrado: uma letra frequente no texto em claro não resulta em estatísticas perceptíveis no texto cifrado.

- **Confusão:**
  - A relação entre o valor da chave e o texto cifrado é tão complexa que não é possível deduzir o valor da chave a partir do texto cifrado.

- **Efeito Avalanche:**
  - Pequenas modificações no texto em claro ou na chave devem gerar grandes mudanças no criptograma.

- **Aleatoriedade:**
  - O criptograma não deve apresentar padrões ou quaisquer sequências inteligíveis: deve parecer com uma sequência aleatória.

- **Segurança Computacional:**
  - O custo para quebrar é maior que o valor da informação codificada.
  - O tempo para quebrar é maior que a vida útil da informação.
  - Segurança incondicional — mesmo com tempo e poder computacional infinitos, o criptograma não pode ser decifrado.
  - Único algoritmo: One-time pad.

## Tipos de Cifras

### Cifras Clássicas (Pré-Computationais)
- **Transposição**
- **Substituição**
- Podem ser decifradas através de análise de frequência.

### Cifras Modernas

- **Cifras Simétricas:**
  - **Em algoritmos de cifra simetrica, o nome da chave é chave secreta**
  - **DES e AES**
    - **Modos de Operação**
    - **Estrutura de Feistel:** Sucessivas substituições e permutações.
    - Após 3 etapas, o texto cifrado é indistinguível de uma permutação aleatória.
    - Vantagens
            - Hardware de baixo custo
            - facilidade de uso e implementação
            - Rapidez e uso geral
        - Desvantagens
            - Distribução e armazenamento das chaves
            - problema de troca inicial de chave
            - não garante autenticidade ou não-repudio
        - Modo de operação
            - fluxo
            - bloco
  - **Advanced Encryption Standard (AES):**
    - Padrão atualmente em uso para criptografia simétrica.
    - Composto por:
      - Substituições
      - Permutações
      - XOR com a chave
    - Chaves de tamanhos variáveis:
      - AES-128, AES-192, ou AES-256
      - Blocos de 128 bits
  - **Cifras de Fluxo (Stream Ciphers):**
    - O algoritmo é aplicado bit a bit (ou byte a byte).
    - Precisam ser rápidas e simples.
    - Utilizado quando não se sabe quantos bits serão transmitidos (ex: Wi-Fi).
  - **Cifras de Bloco:**
    - (Complete o conteúdo conforme necessário.)

- **Cifras Assimétricas:**
  - **Em algoritmos de cifra assmetrica temos duas chaves, chave publica e chave privada**
  - **Diffie-Hellman**
  - **RSA**
  - Motivação: O problema do acordo de chaves
  - Conceito
    - Algoritmo criptografico no qual a cifragem e a decifragem são feitas utilizando chaves distintas: uma pública e outra privada
  - Outras denominações:
    - Criptografia de Chave Assimetrica
    - Criptofrafia de chave Publica
  - Fundamentos:
    - Fundamentada na teoria dos numeros
    - par de chaves relacionadas
      - uma deve ser divulgada: chave publica
      - outra deve ser mantida em sigilo: chave privada
  - Desvantagens:
    - Lento
- ### Concepções errôneas
  - Criptografia de chave publica não é maissegura nem mais vulneravel em relação a criptoanalise do que a criptografia simetrica
  - Na verdade, a segurança de qualquer esquema de criptografia depende
      - 1 do comprimento da chave
      - 2 do esforço
  - As cifras não são melhores do que as outras, tanto a simetrica quanto a assimetrica se complementam. 
  
## Criptoanalise
- 

### Quadro Comparativo entre Cifras Simétricas

| Nome                    | Classificação                     |
|-------------------------|----------------------------------|
| DES e variantes (3-DES) | Cifra simétrica de bloco          |
| AES                     | Cifra simétrica de bloco          |
| RC4                     | Cifra simétrica de fluxo          |
