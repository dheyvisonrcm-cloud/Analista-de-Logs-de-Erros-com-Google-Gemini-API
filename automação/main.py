import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A chave GEMINI_API_KEY não foi encontrada no arquivo .env!")

MODELO = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=120_000),  # 120s, em milissegundos
)


def ler_final_do_arquivo(caminho, max_chars=2000):
    """Lê só o final do arquivo, sem carregar o log inteiro na memória."""
    with open(caminho, "rb") as f:
        f.seek(0, os.SEEK_END)
        tamanho = f.tell()
        f.seek(max(0, tamanho - max_chars * 4))  # margem p/ UTF-8 multibyte
        dados = f.read()
    return dados.decode("utf-8", errors="ignore")[-max_chars:]


def analisar_log(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return

    trecho_log = ler_final_do_arquivo(caminho_arquivo)
    print(f"📄 Arquivo lido: {os.path.abspath(caminho_arquivo)} ({len(trecho_log)} caracteres)\n")

    if not trecho_log.strip():
        print("⚠️ O arquivo de log está vazio. Nada para analisar.")
        return

    prompt = f"""
        <log>
        {trecho_log}
        </log>

        Você é um especialista em DevOps e Desenvolvimento de Software.
        O log acima já está completo, não peça mais informações.
        Responda em português, exatamente neste formato:

        1. **Causa Raiz**: 1 ou 2 frases.
        2. **Nível de Gravidade**: Baixa, Média, Alta ou Crítica.
        3. **Como Resolver**: passo a passo direto e prático.
        4. Contexto: o ambiente é Windows. Dê comandos para Windows (PowerShell/cmd, services.msc), nunca para Linux.
Logs:
"""

    print(f"🤖 Enviando logs para a IA analisar ({MODELO})...\n")

    max_tentativas = 3
    for tentativa in range(1, max_tentativas + 1):
        try:
            resposta = client.models.generate_content(
                model=MODELO,
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                    max_output_tokens=1024,
                ),
            )
            texto = resposta.text
            if not texto:
                print("⚠️ A resposta veio sem texto (possível bloqueio de segurança).")
                print(resposta)
                return

            print("=" * 43)
            print(" RELATÓRIO DE ANÁLISE DE LOGS ")
            print("=" * 43 + "\n")
            print(texto)
            print("\n" + "=" * 43)
            return

        except Exception as e:
            print(f"⚠️ Falha na tentativa {tentativa}/{max_tentativas}: {type(e).__name__}: {e}")
            if tentativa < max_tentativas:
                espera = 2 ** tentativa
                print(f"   Aguardando {espera}s...\n")
                time.sleep(espera)

    print("❌ Todas as tentativas falharam.")


if __name__ == "__main__":
    pasta = os.path.dirname(os.path.abspath(__file__))
    analisar_log(os.path.join(pasta, "app.log"))