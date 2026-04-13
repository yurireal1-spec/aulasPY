import subprocess as sp
import os
import time
aulas_numeradas = "C:/Users/nicol/Desktop/AulasPY/Conceitos Basicos de PY/Fundamentos"

aulas = os.listdir(aulas_numeradas)

while True:
    sp.run("cls", shell=True)

    print("            === Menu de Listagem === \n")
    print('*' * 50)
    print("1 - Listar arquivos")
    print("2 - Executar Aula")
    print("3 - Listar arquivos com detalhes")
    print("4 - Sair \n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for i, aula in enumerate(aulas):
            print(f"{i} - {aula}")
        input("\nPressione Enter para continuar...")

    elif opcao == "2":
        for i, aula in enumerate(aulas):
            print(f"{i} - {aula}")

        try:
            escolha = int(input("\nDigite o número da aula: "))
            arquivo = os.path.join(aulas_numeradas, aulas[escolha])

            sp.run(["py", arquivo])
            time.sleep(20)
        except (ValueError, IndexError):
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

    elif opcao == "3":
        for arquivo in aulas:
            caminho = os.path.join(aulas_numeradas, arquivo)
            tamanho = os.path.getsize(caminho)
            print(f"{arquivo} - {tamanho} bytes")

        input("\nPressione Enter para continuar...")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")