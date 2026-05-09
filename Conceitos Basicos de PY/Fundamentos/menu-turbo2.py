import pandas as pd
import os
import json

# --- Configurações de Caminho ---
CAMINHO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
PASTA_HISTORICO = os.path.join(CAMINHO_SCRIPT, "historico")
ARQUIVO_JSON = os.path.join(PASTA_HISTORICO, "filmes_catalogo.json")

# Garantir que a pasta exista
os.makedirs(PASTA_HISTORICO, exist_ok=True)

# --- Variáveis Globais ---
dicionario_filmes = {}
contador = 0

class Filme:
    def adicionar(self, nome, lancamento, genero):
        return {
            "nome": nome,
            "lancamento": lancamento,
            "genero": genero
        }

gerenciador = Filme()

# --- Funções de Utilidade ---
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

# --- Lógica do Sistema ---

def adicionar_filme():
    global contador
    while True:
        limpar_tela()
        print("=== Adicionar Novo Filme ao Buffer ===")
        nome = input("Nome do filme: ").strip()
        if not nome: break

        try:
            ano = int(input("Ano de lançamento: "))
        except ValueError:
            print("Erro: Digite um ano válido.")
            pausar(); continue

        gen_raw = input("Gêneros (separados por vírgula): ")
        generos = [g.strip() for g in gen_raw.split(",") if g.strip()]

        dicionario_filmes[contador] = gerenciador.adicionar(nome, ano, generos)
        contador += 1
        
        print(f"\n✔ '{nome}' adicionado à lista de espera.")
        if input("\nAdicionar outro? (s/n): ").lower() != 's': break

def visualizar_buffer():
    limpar_tela()
    print("=== Filmes na Fila de Espera (Ainda não salvos) ===")
    if not dicionario_filmes:
        print("Lista vazia.")
    else:
        df = pd.DataFrame.from_dict(dicionario_filmes, orient="index")
        print(df)
    pausar()

def atualizar_catalogo_json():
    """Junta o que está na memória com o que está no arquivo, removendo duplicados."""
    limpar_tela()
    global dicionario_filmes, contador
    
    if not dicionario_filmes:
        print("Não há filmes novos para atualizar.")
        pausar(); return

    try:
        df_novos = pd.DataFrame.from_dict(dicionario_filmes, orient="index")
        
        if os.path.exists(ARQUIVO_JSON):
            df_antigo = pd.read_json(ARQUIVO_JSON)
            df_final = pd.concat([df_antigo, df_novos], ignore_index=True)
        else:
            df_final = df_novos

        # Remove duplicados pelo nome (ignora maiúsculas/minúsculas se desejar)
        df_final = df_final.drop_duplicates(subset=['nome'], keep='last')
        
        # Salva
        df_final.to_json(ARQUIVO_JSON, orient="records", indent=4, force_ascii=False)
        
        # LIMPEZA: Após salvar, limpamos a memória
        dicionario_filmes.clear()
        contador = 0
        
        print(f"✅ Catálogo atualizado com sucesso em: {ARQUIVO_JSON}")
    except Exception as e:
        print(f"❌ Erro ao atualizar: {e}")
    pausar()

def visualizar_catalogo_completo():
    limpar_tela()
    print("=== Catálogo Oficial (Arquivo JSON) ===")
    if os.path.exists(ARQUIVO_JSON):
        try:
            df = pd.read_json(ARQUIVO_JSON)
            if df.empty:
                print("O arquivo está vazio.")
            else:
                print(df)
                print(f"\nTotal de filmes: {len(df)}")
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
    else:
        print("Arquivo JSON ainda não foi criado.")
    pausar()

# --- Menu Principal ---
while True:
    limpar_tela()
    print("=" * 50)
    print("      SISTEMA DE GERENCIAMENTO NETFLIX TURBO")
    print("=" * 50)
    print("1 - Adicionar filmes (Memória)")
    print("2 - Ver filmes na fila de espera")
    print("3 - SALVAR/ATUALIZAR Catálogo (JSON)")
    print("4 - VER Catálogo Completo (JSON)")
    print("10 - Sair")
    print("-" * 50)
    
    op = input("Escolha: ")

    if op == "1": adicionar_filme()
    elif op == "2": visualizar_buffer()
    elif op == "3": atualizar_catalogo_json()
    elif op == "4": visualizar_catalogo_completo()
    elif op == "10": 
        print("Encerrando..."); break
    else:
        print("Opção inválida."); pausar()
        