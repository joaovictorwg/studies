# Elevações de Privilégios em Sistemas Operacionais

Uma vulnerabilidade é um defeito ou problema presente na especificação, implementação, configuração ou operação de um software, hardware ou sistema que possa ser explorado para violar as propriedades de segurança do mesmo.

**Elevação ou escalonamento de privilégios** consiste no ato de explorar vulnerabilidades ou deficiências para conseguir privilégios superiores.

### Tipos de Escalonamento de Privilégios

1. **Escalonamento Vertical**: Ocorre quando um usuário ou aplicativo com privilégios inferiores acessa funções ou conteúdos reservados a usuários ou aplicativos de nível superior (ex.: usuário comum → superusuário).
   
2. **Escalonamento Horizontal**: Ocorre quando um usuário comum acessa funções ou conteúdos reservados para outros usuários no mesmo nível de privilégio (ex.: usuário → outro usuário).

### Métodos de Obtenção de Privilégios Elevados

A elevação de privilégios pode ser obtida através de:
- **Força bruta** em hashes de senhas de baixa complexidade.
- **Arquivos privados de autenticação**, como chaves SSH (`id_rsa`).
- **Vulnerabilidades de hardware**, como falhas no chipset.
- **Vulnerabilidades de kernel** do sistema operacional.
- **Vulnerabilidades de aplicações** instaladas.
- **Permissões de sudo** mal configuradas.
- **Tarefas agendadas** (`cron`) mal configuradas.
- **Permissões SUID** configuradas incorretamente.

---

## Enumeração em Sistemas Operacionais com Kernel

### Comandos para Coletar Informações do Sistema

- `uname -a`: Mostra informações detalhadas sobre o kernel e arquitetura do sistema.
- `cat /etc/issue`: Exibe a versão e informações do sistema operacional.
- `cat /proc/version`: Exibe a versão do kernel em execução no sistema.

### Comandos para Coletar Informações sobre o Usuário

- `id`: Mostra o ID do usuário atual e seus grupos.
- `whoami`: Mostra o nome do usuário atualmente logado.
- `sudo -l`: Lista os privilégios `sudo` disponíveis para o usuário atual.
- `groups`: Mostra os grupos dos quais o usuário atual faz parte.
- `cat /etc/passwd`: Exibe os usuários do sistema e suas informações.
- `cat /etc/shadow`: Exibe as senhas criptografadas dos usuários (acessível apenas por root).
- `cat /etc/group`: Exibe os grupos do sistema e os usuários pertencentes a eles.

### Comandos para Coletar Informações de Arquivos

- `cat ~/.bash_history`: Exibe o histórico de comandos executados pelo usuário atual.
- `find / -name id_rsa 2>/dev/null`: Procura por chaves privadas SSH (`id_rsa`) no sistema.
- `cat /home/user/.ssh/id_rsa`: Exibe o conteúdo da chave privada SSH de um usuário.
- `ps -aux`: Lista todos os processos em execução no sistema.
- `top`: Exibe os processos em execução e seu uso de recursos em tempo real.
- `htop`: Versão interativa e aprimorada do `top`.

### Comandos para Variáveis de Ambiente

- `env`: Exibe todas as variáveis de ambiente do sistema.

### Comandos de Rede

- `ifconfig`: Mostra as configurações de rede das interfaces de rede (substituído por `ip` em sistemas modernos).
- `iwconfig`: Mostra as configurações de rede sem fio (Wi-Fi).
- `hostname`: Exibe o nome da máquina.
- `ip a`: Mostra as interfaces de rede e seus endereços IP.
- `ss -anltup`: Mostra as conexões de rede ativas e as portas abertas no sistema.
- `route`: Exibe a tabela de roteamento de rede.
- `ping <ip>`: Envia pacotes ICMP para testar a conectividade com o IP especificado.
- `traceroute <ip>`: Mostra o caminho (hops) que os pacotes percorrem para chegar ao IP especificado.

### Comandos para Informações de Módulos do Kernel

- `lsmod`: Exibe os módulos de kernel carregados no sistema.
- `cat ~/.mysql_history`: Exibe o histórico de comandos SQL executados no MySQL (se houver).
- `cat /etc/crontab`: Mostra tarefas agendadas no sistema via `cron`.
- `snap --version`: Exibe a versão do Snapd (gerenciador de pacotes Snap).
- `sudo --version`: Exibe a versão do sudo (útil para verificar se há vulnerabilidades conhecidas nessa versão).

---

## Ferramentas para Automação da Enumeração

1. **LinPEAS**: Ferramenta de enumeração para sistemas Linux, usada para encontrar rapidamente vulnerabilidades e possíveis vetores de elevação de privilégio.
2. **LinEnum**: Ferramenta automatizada de enumeração de informações sobre o sistema e configuração que podem levar à elevação de privilégios.

### Exploit Database
- **Exploit DB**: Base de dados com exploits conhecidos que podem ser usados para explorar vulnerabilidades.

---

