# PyAudit

PyAudit é uma ferramenta de auditoria de segurança projetada para sistemas e servidores Linux. Ela verifica a presença de firewalls, softwares anti-malware, anti-rootkit, e sistemas de detecção de intrusão (IDS) instalados e ativos no sistema, informando também as versões dos softwares detectados, quando possível.

## Funcionalidades

- **Verificação de Firewall**: Identifica firewalls ativos como UFW, iptables e firewalld, exibindo a versão do software quando disponível.
- **Verificação de Anti-malware**: Detecta a presença de softwares anti-malware como ClamAV, rkhunter, chkrootkit, e Lynis.
- **Verificação de Anti-rootkit**: Verifica se há ferramentas anti-rootkit, como rkhunter e chkrootkit, instaladas e ativas.
- **Verificação de IDS (Intrusion Detection System)**: Identifica a presença de IDS como Snort e Suricata, mostrando também suas versões.

## Requisitos

- **Sistema Operacional**: Linux
- **Python**: Python 3.6 ou superior

## Instalação

1. Clone este repositório:

   git clone https://github.com/freitasec/pyaudit.git

2. Navegue até o diretório do projeto:

   cd pyaudit

3. (Opcional) Crie e ative um ambiente virtual:

   python3 -m venv venv

   
   source venv/bin/activate
   
4. Torne o script executável:

   chmod +x pyaudit.py

## Uso

1. Para executar a ferramenta, utilize o seguinte comando:

   sudo ./pyaudit.py

## Aviso legal

PyAudit foi criada com o propósito de ajudar administradores de sistemas e segurança da informação a avaliar rapidamente o status de segurança de sistemas Linux. O uso desta ferramenta deve ser realizado de forma responsável e em sistemas nos quais você tem permissão para realizar auditorias de segurança.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
