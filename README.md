🔍 Analista de Logs de Erros com Google Gemini API

Uma ferramenta de automação em Python desenvolvida para analisar arquivos de log locais (`app.log`) em ambientes **Windows**. Utiliza a SDK oficial do Google GenAI com a versão **`gemini-3.6-flash`**, aplicando leitura otimizada em memória e resiliência com backoff exponencial.

---

## 🛠️ Tecnologias e Destaques do Código

* **Python 3.14+**
* **Google GenAI SDK** (`google-genai`)
* **python-dotenv** (gerenciamento seguro de variáveis de ambiente)
* **Leitura Eficiente em Byte**: Função `ler_final_do_arquivo` com `f.seek()` para carregar apenas os últimos trechos do log sem lotar a memória RAM.
* **Resiliência e Retries**: Tratamento de exceções com **backoff exponencial** (`2 ** tentativa`) para encarar picos de tráfego sem derrubar a execução.
* **Otimização de Prompt e Tokens**: Parâmetro `thinking_budget=0` e limite de tokens (`max_output_tokens=1024`) configurados para obter respostas rápidas e diretas.
* **Foco em Windows**: Instruções e comandos direcionados exclusivamente para o ambiente Windows (PowerShell/CMD/`services.msc`).

---

## 📁 Estrutura do Projeto

```text
automação/
├── .env                # Variáveis de ambiente
├── app.log             # Arquivo de log monitorado
├── main.py             # Script principal de análise de logs
├── requirements.txt    # Lista de dependências Python
└── README.md           # Documentação do projeto
