#!/usr/bin/env python3

import os
import subprocess

def check_firewall():
    firewalls = {
        'ufw': 'sudo ufw status',
        'iptables': 'sudo iptables -L',
        'firewalld': 'sudo firewall-cmd --state'
    }
    for fw, command in firewalls.items():
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print(f"Firewall detectado: {fw}")
                version = subprocess.run(f"{fw} --version".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Versão do {fw}: {version.stdout.decode().splitlines()[0]}")
        except Exception as e:
            pass

def check_antimalware():
    antimalwares = {
        'clamav': 'clamscan --version',
        'rkhunter': 'rkhunter --versioncheck',
        'chkrootkit': 'chkrootkit -V',
        'lynis': 'lynis --version'
    }
    for am, command in antimalwares.items():
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print(f"Antimalware detectado: {am}")
                print(f"Versão do {am}: {result.stdout.decode().splitlines()[0]}")
        except Exception as e:
            pass

def check_anti_rootkit():
    anti_rootkits = {
        'rkhunter': 'rkhunter --versioncheck',
        'chkrootkit': 'chkrootkit -V'
    }
    for ar, command in anti_rootkits.items():
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print(f"Anti-rootkit detectado: {ar}")
                print(f"Versão do {ar}: {result.stdout.decode().splitlines()[0]}")
        except Exception as e:
            pass

def check_ids():
    ids_tools = {
        'snort': 'snort -V',
        'suricata': 'suricata --build-info'
    }
    for ids, command in ids_tools.items():
        try:
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print(f"IDS detectado: {ids}")
                print(f"Versão do {ids}: {result.stdout.decode().splitlines()[0]}")
        except Exception as e:
            pass

def main():
    print("Verificando firewall ativo...")
    check_firewall()

    print("\nVerificando software anti-malware...")
    check_antimalware()

    print("\nVerificando software anti-rootkit...")
    check_anti_rootkit()

    print("\nVerificando IDS ativo...")
    check_ids()

if __name__ == "__main__":
    main()
