Claro! Vamos organizar e corrigir suas anotações em um formato Markdown. Aqui está uma versão revisada:

---

# Portas

## O que são Portas?

- **Definição**: São pontos finais de comunicação em um sistema operacional. Identificam aplicações e processos em um computador.
- **Número da Porta**: Identificado por um número de 16 bits, adicionado a um endereço IP, formando o endereço de destino para uma sessão de comunicação.
- **Encaminhamento**: Pacotes de dados são enviados através da rede para um endereço de destino e, ao atingir o computador de destino, são encaminhados para o processo apropriado.

## Tipos de Portas

### Portas Bem Conhecidas (Well-Known Ports)

- **Faixa**: 0-1023
- **Uso**: Reservadas para processos de sistema (daemon) ou programas executados por usuários privilegiados.
- **Exemplos**: 
  - HTTP: 80
  - HTTPS: 443
  - FTP: 21

### Portas Registradas

- **Faixa**: 1024-49151
- **Uso**: Usadas por aplicações e serviços específicos, mas não reservadas de forma rígida.

### Portas Dinâmicas e/ou Privadas

- **Faixa**: 49152-65535
- **Uso**: Usadas temporariamente por clientes durante a comunicação com servidores.

## Verificando o Estado das Portas

### Netstat

- **Descrição**: Ferramenta de linha de comando que exibe conexões de rede TCP e UDP, tabelas de roteamento e estatísticas.
- **Comando**: `netstat -a` para listar todas as conexões e escuta portas.

### Netcat

- **Descrição**: Utilitário de rede para enviar e receber dados através de conexões TCP e UDP. Usado para depuração e criação de comunicação entre máquinas.
- **Comandos**:
  - **Modo Escuta**: `nc -lvp 1234 -e /bin/bash`
  - **Conectar-se**: `nc [endereço-do-alvo] 1234`

### Nmap

- **Descrição**: Utilitário para descoberta de hosts e análise de rede.
- **Comandos**:
  - **Varredura Completa**: `nmap -A [endereço]`
  - **Listar Scripts**: `ls /usr/share/nmap/scripts`

## IDS - Sistema de Detecção de Intrusões

- **Descrição**: Monitora ambientes computacionais em busca de eventos que possam violar regras de segurança, como atividades incomuns, malwares e invasões.
- **Função**: Coleta dados e analisa em tempo real padrões comportamentais e fluxos de dados. Pode identificar eventos maliciosos com base em padrões conhecidos de ataques.
- **Modelos**:
  - **Baseado em Host**: Analisa atividades diretamente em um único computador.
  - **Baseado em Rede**: Analisa o tráfego de rede em busca de atividades suspeitas.
- **Tipos**:
  - **Passivo**: Detecta ameaças e informa o administrador.
  - **Ativo (IPS)**: Bloqueia automaticamente atividades maliciosas, podendo utilizar técnicas como configuração de firewalls e envio de pacotes reset.

### Exemplo de IDS/IPS

- **SNORT**: Sistema de detecção e prevenção de intrusões baseado em rede, open source.

## CVE - Vulnerabilidades e Exposições Comuns

- **Descrição**: Base de dados pública para troca de informações sobre falhas de segurança.
- **Objetivo**: Padronizar nomes e informações para todas as vulnerabilidades e exposições conhecidas publicamente.

## Honeypots

- **Descrição**: Usados para enganar hackers, expondo vulnerabilidades conhecidas deliberadamente. Permite a catalogação das atividades dos hackers para análise.
- **Configuração**: Geralmente tem serviços comuns em execução, como HTTP (porta 80), FTP (porta 21), e pode ter o tráfego redirecionado para o honeypot.
- **Objetivo**: Fazer o honeypot parecer real, com arquivos e contas fictícias para engajar os hackers e monitorar suas atividades.

## Comandos Adicionais

- **Netdiscover**: Utilitário para descobrir dispositivos em uma rede local.
  - **Comando**: `sudo netdiscover -i [interface]`

## Roteiro VM

- **Referência**: "vm thales vulnhub" (Certifique-se de seguir as instruções e configurar a máquina virtual conforme necessário.)

---