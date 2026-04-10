# 🤖 Tech Monitor Bot

![Python](https://img.shields.io/badge/python-3.13-blue)
![Telegram Bot](https://img.shields.io/badge/telegram-bot-blue)
![Jira](https://img.shields.io/badge/integration-jira-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

Bot desenvolvido em **Python** para monitoramento de chamados técnicos e automação de notificações via **Telegram**, integrado com **Jira**.

---

# 📌 Sobre o projeto

O **Tech Monitor Bot** foi criado para ajudar equipes técnicas a acompanhar chamados automaticamente.

O bot consulta o **Jira**, processa os chamados e envia notificações diretamente para técnicos via **Telegram**, permitindo uma resposta mais rápida a incidentes e demandas.

---

# 🚀 Funcionalidades

- ✅ Consulta automática de chamados no Jira  
- ✅ Notificação automática para técnicos no Telegram  
- ✅ Menu interativo no bot  
- ✅ Listagem de chamados por técnico  
- ✅ Paginação de resultados  
- ✅ Scheduler automático para monitoramento  
- ✅ Estrutura modular em Python  

---

# 🏗️ Estrutura do Projeto

```
tech-monitor-bot
│
├ app
│   ├ handlers        # Handlers dos comandos do bot
│   │
│   ├ services        # Integrações (Jira, Telegram, Scheduler)
│   │
│   ├ keyboards       # Teclados interativos do Telegram
│   │
│   ├ utils           # Funções utilitárias
│   │
│   ├ config.py       # Configurações da aplicação
│   └ main.py         # Inicialização do bot
│
├ requirements.txt
├ runtime.txt
├ Procfile
├ .env.example
└ README.md
```

---

# ⚙️ Tecnologias utilizadas

- **Python 3.13**
- **PyTelegramBotAPI**
- **Jira REST API**
- **APScheduler**
- **python-dotenv**

---

# 🔧 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/tech-monitor-bot.git
```

Entre na pasta do projeto:

```bash
cd tech-monitor-bot
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuração

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```
BOT_TOKEN=seu_token_do_telegram

JIRA_URL=https://empresa.atlassian.net
JIRA_EMAIL=seu_email@empresa.com
JIRA_API_TOKEN=seu_token_jira
```

---

# ▶️ Executar o bot

Execute o projeto com:

```bash
python -m app.main
```

Saída esperada no terminal:

```
🤖 Bot Técnicos iniciado...
```

---

# 📲 Comandos do Bot

| Comando | Descrição |
|------|------|
| `/start` | Inicia o bot |
| 📋 Chamados | Lista chamados do Jira |
| 👨‍🔧 Técnicos | Mostra chamados por técnico |

---

# 🔄 Scheduler

O projeto possui um **scheduler automático** que consulta o Jira periodicamente para verificar novos chamados e disparar notificações.

---

# 🛡️ Segurança

Credenciais sensíveis são armazenadas em `.env`.

Esse arquivo **não é enviado ao GitHub** graças ao `.gitignore`.

---

# 📦 Deploy

O projeto pode ser executado em:

- VPS Linux
- Railway
- Docker
- Servidores cloud

---

# 👨‍💻 Autor

Desenvolvido por **Matheus Andrade**

---

# 📄 Licença


