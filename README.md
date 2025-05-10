# SQL Injection e XSS Exploiter

Este repositório contém dois scripts para exploração de vulnerabilidades comuns em aplicações web: **SQL Injection** e **Cross-Site Scripting (XSS)**. Ambos os scripts foram desenvolvidos para testar sites e identificar vulnerabilidades. **Use-os com responsabilidade e sempre tenha permissão explícita para realizar testes de segurança.**

---

## Índice

- [SQL Injection Exploiter](#sql-injection-exploiter)
- [XSS Exploiter](#xss-exploiter)
- [Pré-Requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Aviso Legal](#aviso-legal)

---

## SQL Injection Exploiter

### Descrição

O **SQL Injection Exploiter** é um script para realizar testes de **SQL Injection** em sites. Ele utiliza diferentes payloads para tentar explorar vulnerabilidades em formulários de login e em outros pontos da aplicação.

### Funcionalidades

- **Bypass Simples**: Tenta contornar autenticações através de injeções simples.
- **Extração de Usuário/Admin**: Tenta extrair informações de usuários ou administradores.
- **Injeção de Tempo (Blind SQL)**: Testa vulnerabilidades de **SQL Injection** que utilizam tempos de resposta para determinar se a injeção foi bem-sucedida.
- **Injeção de Erro**: Explora erros no servidor para coletar informações do banco de dados.
- **Execução de Comandos**: Tenta executar comandos no servidor.
- **Modificação de Tabelas**: Tenta modificar ou excluir dados de tabelas no banco de dados.

### Como Usar

1. Execute o script Python.
2. Digite o URL do site alvo.
3. Escolha o tipo de SQL Injection a ser testado.
4. O script vai tentar cada **payload** e indicará se algum sucesso foi encontrado.

---

## XSS Exploiter

### Descrição

O **XSS Exploiter** é um script para realizar testes de **Cross-Site Scripting (XSS)** em sites. O script envia diferentes payloads para testar as vulnerabilidades de XSS refletido, armazenado, baseado em DOM e de bypass de filtros.

### Funcionalidades

- **XSS Refletido**: Testa vulnerabilidades de XSS onde o código injetado é refletido diretamente na resposta do servidor.
- **XSS Armazenado**: Testa XSS que são armazenados no servidor, como em bancos de dados ou logs.
- **XSS DOM-Based**: Testa XSS onde a vulnerabilidade ocorre no lado do cliente, no DOM.
- **Bypass de Filtros Comuns**: Testa técnicas para contornar filtros de segurança (ex: `script`, `onload`).

### Como Usar

1. Execute o script Python.
2. Digite o URL do site alvo.
3. Escolha o tipo de XSS a ser testado (Refletido, Armazenado, DOM-Based ou Bypass).
4. O script tentará cada **payload** e informará se algum sucesso for detectado.

---

## Pré-Requisitos

Antes de executar os scripts, instale as dependências necessárias:

```bash
pip install -r requirements.txt
