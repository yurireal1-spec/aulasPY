import subprocess as sp
import pandas as pd
import os
import shutil

dicionariofilmes={}
p=""
i=0 

class Filme:
    def adicionar(self,nome,lancamento,genero):
        return {
            "nome":nome,
            "lancamento":lancamento,
            "genero":genero 
        }

gerenciador = Filme()     
   
def carregar_dados_entrada():
    caminho_do_script = os.path.dirname(os.path.abspath(__file__))
    pasta_historico = os.path.join(caminho_do_script, "historico")
    
    if not os.path.exists(pasta_historico):
        os.makedirs(pasta_historico)
        print(f"Pasta criada em: {pasta_historico}")
    
    return pasta_historico # Retornamos o caminho para usar no resto do código

# --- CHAMADA DA FUNÇÃO ---
# Guardamos o caminho da pasta em uma variável global
caminho_pasta = carregar_dados_entrada()

while True:
    sp.run("cls", shell=True)
    print("            === Menu de Listagem === \n")
    print('*' * 50)
    print("1 - Adicionar novo filme")
    print("2 - Filmes novos (Para adicionar ao Catalogo)")
    print("3 - Atualizar Catalogo")
    print("4 - Catalogo Filmes")
    print("10 - Sair \n")

    opcao = input("Escolha um opção: ")

    if opcao == "1":
        p = ""
        while p != 'fim':
            os.system('cls')
            print("               ==Adicionar filmes==")
            n = input("Nome do filme:  ")
            l = int(input("Data de lançamento:  "))
            g = input("Genero:  ").split(",")

            dt = gerenciador.adicionar(n, l, g)
            dicionariofilmes[i] = dt
            i += 1
            print(f"\nFilme {n}, foi adicionado!")
            p = input("Digite 'fim' para parar ou Enter para continuar: ").lower()

    elif opcao == "2":
        if len(dicionariofilmes) == 0:
            print("\n\nNenhum filme cadastrado.")
        else:
            df = pd.DataFrame.from_dict(dicionariofilmes, orient="index")
            print("\nCatalogo:")
            print(df)
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "3":
        if not dicionariofilmes:
            print("\nSem dados para apresentar ou salvar....")
        else:
            try:
                df_temp = pd.DataFrame.from_dict(dicionariofilmes, orient="index")
                
                # --- AJUSTE AQUI ---
                # Criamos o caminho completo: pasta_historico + nome_do_arquivo
                caminho_final = os.path.join(caminho_pasta, "arquivo.json")
                
                df_temp.to_json(caminho_final, orient="records", indent=4, force_ascii=False)
                print(f"\n✅ Arquivo salvo em: {caminho_final}")

            except Exception as e:
                print(f"\n❌ Erro ao salvar o arquivo: {e}")
        
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "4":
        # Lógica para ler o arquivo
        caminho_final = os.path.join(caminho_pasta, "arquivo.json")
        if os.path.exists(caminho_final):
            df_lido = pd.read_json(caminho_final)
            print("\n--- Conteúdo do Arquivo JSON ---")
            print(df_lido)
        else:
            print("\nArquivo não encontrado no histórico.")
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "10":
        print("\nSaindo do sistema... Até logo!")
        break
