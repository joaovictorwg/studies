# Segurança e Auditoria de Sistemas

## Vulnerabilidades

- **Vulnerabilidades de Dia Zero**: Vulnerabilidades que são desconhecidas pelas empresas de segurança e desenvolvedores, sendo conhecidas apenas pelos hackers.

## Ferramentas de Busca

- **Site para procurar vulnerabilidades**: [CVE (Common Vulnerabilities and Exposures)](https://cve.mitre.org)

## Tipos de Malware e Ameaças

- **Adware**: Propaganda que é integrada ao software.
- **Trojans**: Programas que se apresentam como úteis, mas que carregam uma carga maliciosa.
- **Exploit**: Trecho de instruções, código, comando, ou operações que exploram uma determinada vulnerabilidade ou conjunto de vulnerabilidades.
- **Flooders**: Programas usados para gerar um grande volume de dados e atacar sistemas.
- **Keyloggers**: Software para capturar as teclas digitadas pelo usuário.
- **Screenloggers**: Software semelhante aos keyloggers, mas que captura a tela.
- **Spyloggers**: Software que copia informações de um computador e as transmite para outro.
- **Vírus**: Malware que, ao ser executado, tenta se reproduzir na forma de outro código de máquina executável ou script.
- **Zumbi (Bot)**: Programa ativado em uma máquina infectada que é usado para ataques contra outras máquinas.
- **Bomba Lógica**: Código inserido em um malware por um intruso que permanece em hibernação até que uma condição predefinida ocorra, ativando uma ação não autorizada.
- **Bomba ZIP**: Arquivo compactado criado para sobrecarregar um sistema ao ser descompactado, causando instabilidade ou travamento.

## Técnicas

- **Spoofing**: Técnica usada para enganar sistemas ou usuários, fazendo parecer que uma comunicação vem de uma fonte confiável quando, na verdade, vem de uma fonte maliciosa.

## Proteção

- **Usar Gerenciadores de Senha**: Como o KeyPass, para manter senhas seguras e organizadas.
- **Usar E-mail Temporário**: Para evitar spam e proteger a privacidade em cadastros online.

## Tríade de Segurança da Informação

- **Integridade**: Refere-se à manutenção das condições originais das informações, garantindo que elas não sejam alteradas sem autorização.
- **Disponibilidade**: Propriedade de resistência a falhas (hardware, software, energia), com o objetivo de manter os serviços disponíveis pelo maior tempo possível.
  - **Estratégias**: Uso de hardware redundante que entra em funcionamento automaticamente após a falha do hardware principal.
  - **Fórmula de Disponibilidade**: 
    - Disponibilidade = MTBF / (MTBF + MTTR)
    - MTBF (Mean Time Between Failures): Tempo médio entre falhas.
    - MTTR (Mean Time to Repair): Tempo médio de recuperação.
- **Confidencialidade**: Princípio, segundo o qual, a informação será acessível para indivíduos, entidades ou processos devidamente autorizados.

## Um ataque pode ser:
- **Ativo**: Tendo por resultado a alteração dos dados (manipulação da informação)
- **Passivo** - Tendo por resultado a liberação dos dados (vazamentos em grande escala)
- **Destrutivo** - visando a negação do acesso aos dados dos serviços (ataque Dos e Ddos)
- O impacto de um incidente de segurança é medido pelas consquencias que pode causar aos processos de negocio suportados pelo ativo em questão

## Hashes Criptograficos
- **Algoritimo de hash criptográfico**: Função matemática cujo resultado é um valor de tamanho fixo, gerado a partir de uma entrada de tamanho arbitrário. Na computação Foresense, os arquivos geralmente são utilizados como parâmetro de entrada dessas funções, o que permite identificar se dois ou mais arquivos possuem conteúdos idênticos. Dado o seu atributo de unidirecionalidade, a partir de seu resultado é impraticavel produzir o parâmetro de entrada
- **Integridade**: Colisão de hashes criptograficos.
- Para ter utilidade criptografica, a função de hasing deve ter as seguintes caracteristicas
    - Unidirecionalidade: conhecido um resumo h(m) deve ser computacionalmente impossivel encontrar m a partir do resumo
    - **Difusão** o resumo h(M) deve ser uma função complexa de todos os bits da mensagem M. Se, se modficica um so bit da memsagem m o hash h(M) deveria mudar a metade de seus bits aproximadamente
    - **Resistência a colisão** :sera computacionalmente impossivel um par (M, M') de forma que h(M) = h(M')

## Esteganografia
- Termo de origem grega que signfica **esconder escrita**. Arte de esconder informações tornando-as ocultas.
- Muitas técnicas esteganográficas, por exemplo,escondem dados dentro de arquivos. Seu principal objetivo é que esses dados não sejam percebidos por terceiros.
