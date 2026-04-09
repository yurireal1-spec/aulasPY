import os      # Biblioteca para interagir com o Sistema Operacional (pastas, caminhos).
import json    # Biblioteca para converter strings em dicionários Python e vice-versa.
import pandas as pd  # Biblioteca poderosa para análise e manipulação de tabelas (DataFrames).

# 1. Configurações Iniciais
# Definimos o ponto de partida. Usar o caminho absoluto evita erros de "pasta não encontrada".
diretorio_raiz = 'C:/Users/nicol/Desktop/Linux_Pratica' 

# Lista que servirá de contêiner para os dicionários de dados de cada arquivo.
dados_coletados = []  

print("Iniciando varredura recursiva...")

# os.walk(): Função geradora que "caminha" por toda a árvore de diretórios.
# Retorna uma tupla (pasta_atual, subpastas_da_pasta, arquivos_da_pasta) para cada nível.
for rota, pastas, arquivos in os.walk(diretorio_raiz):
    
    # Iteramos sobre a lista de nomes de arquivos encontrados na 'rota' atual.
    for nome_arquivo in arquivos:
        
        # os.path.splitext(): Divide o nome do arquivo em uma tupla (nome, extensão).
        # [1] pega o segundo elemento (a extensão) e .lower() padroniza para minúsculo.
        extensao = os.path.splitext(nome_arquivo)[1].lower()
        
        # Filtro lógico: Só processamos se o arquivo for de texto ou JSON.
        if extensao in [".txt", ".json"]:
            
            # os.path.join(): Une a pasta (rota) ao nome do arquivo.
            # É inteligente: no Windows usa '\', no Linux usa '/', evitando erros de sintaxe.
            caminho_completo = os.path.join(rota, nome_arquivo)
            
            # Usamos splitext novamente, mas pegamos o índice [0] para ter o nome sem o '.txt'.
            nome_identificado = os.path.splitext(nome_arquivo)[0]

            # Bloco try/except: Essencial para que um arquivo corrompido não pare todo o script.
            try:
                # open(): Abre o arquivo para leitura ('r'). 
                # encoding="utf-8": Garante a leitura correta de acentos e caracteres especiais.
                with open(caminho_completo, 'r', encoding="utf-8") as f:
                    conteudo = f.read()
                    
                    # json.loads(): (Load String) Pega o texto lido e tenta transformá-lo 
                    # em um objeto Python (dicionário ou lista).
                    dados_json = json.loads(conteudo)
                    
                    # .get(): Método de dicionário que busca uma chave.
                    # Se a chave não existir, ele retorna o valor padrão ("N/A") em vez de travar.
                    dados_coletados.append({
                        'tipo': extensao,
                        'nome': nome_identificado,
                        'id': dados_json.get("id", "N/A"),
                        'status': dados_json.get("status", "Pendente"),
                        'caminho': caminho_completo,
                    })

            # Erro específico para quando o arquivo não segue a estrutura JSON.
            except json.JSONDecodeError:
                print(f"Aviso: {nome_arquivo} ignorado (não contém JSON válido).")
                
            # Erro genérico para capturar qualquer outro problema (ex: arquivo bloqueado).
            except Exception as e:
                print(f"Erro ao processar {nome_arquivo}: {e}")

# 2. Processamento Final com Pandas
if dados_coletados:
    # pd.DataFrame(): Transforma nossa lista de dicionários em uma tabela estruturada.
    # Cada chave do dicionário vira automaticamente uma coluna.
    Tabela = pd.DataFrame(dados_coletados)
    
    # Reindexação: Passamos uma lista com a ordem desejada das colunas.
    ordem_colunas = ['id', 'nome', 'status', 'tipo', 'caminho']
    Tabela = Tabela[ordem_colunas]
    
    # to_csv(): Exporta a tabela para um arquivo físico.
    # index=False: Remove a coluna numérica de IDs do Pandas (0, 1, 2...).
    # utf-8-sig: Versão do UTF-8 que o Excel entende perfeitamente.
    Tabela.to_csv('resultado_final.csv', index=False, encoding='utf-8-sig')
    
    print("\n--- Processamento Concluído ---")
    
    # to_string(): Gera uma representação em texto da tabela para o console.
    # index=False aqui serve apenas para a estética do print.
    print(Tabela.to_string(index=False))
    
    print(f"\nSucesso! {len(dados_coletados)} registros salvos.")
else:
    print("Nenhum arquivo válido encontrado.")
    