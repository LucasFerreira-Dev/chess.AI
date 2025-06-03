"""
Se for sua primeira vez e não pegar, abra o terminal e rode o:
    Criar ambiente: python -m venv .venv
    Instalar: pip install -q -U google-genai
    
Códigos uteis:
    Criar ambiente: python -m venv .venv
    Instalar: pip install -q -U google-genai
    Desestalar: pip uninstall google-genai 
"""

#Importações
from google import genai #trás o genimi
import os #compara se existe
import webbrowser #pesquisa web
import time #para o tempo

#testa se a chave ta salva
def SalvarChave(Arquivo):
    if not os.path.exists(Arquivo):
        #chamar tutorial
        Tutorial()
        
        chave = input("Digite a sua chave de ativação da IA: ")
        with open(Arquivo, "w") as arquivo:
            arquivo.write(chave)
        print("Chave salva com sucesso")     
    else:
        with open(Arquivo, "r") as arquivo:
            chave = arquivo.read()
                        
        if not chave:  # Se estiver vazio
            #Chamar primeiro o tutorial
            Tutorial()
            
            print("Arquivo existe, mas a chave está vazia!")
            chave = input("Digite a sua chave de ativação da IA: ")
            with open(Arquivo, "w") as arquivo:
                arquivo.write(chave)
            print("Chave salva com sucesso")
        else:
            print("Chave lida com sucesso")
            
    return chave

#manda a pergunta para a IA
def Perguntar_Gemini(pergunta, chave):
    client = genai.Client(api_key=chave)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=pergunta,
    )
    return response.text

#abre qualquer link na web
def Abrir_Site(url):
    webbrowser.open(url)

#tutorial para responder dúvidas
def Tutorial():
    while True:
        print("Menu do tutorial:")
        print("\t1. Orientações")
        print("\t2. Abrir site para obter chave")
        print("\t3. Abrir site da documentação ")
        print("\t4. Sair")
        escolha = input("Escolha: ")
        
        match escolha:
            case "1":
                print("1. Entre no site para ter sua chave")
                print("2. Aperte na segunda opção o Build with the Gemini API, se não aparecer nada ta ok também")
                print("3. Aperte no +Criar chave API")
                print("4. Copie a chave criada")
                print("5. volte para a execução do código e cadastre a sua chave\n")
                time.sleep(4) #esperar o usuario ler
            case "2":
                link = "https://aistudio.google.com/apikey"
                print("Abrindo site")
                time.sleep(2)
                Abrir_Site(link)
            case "3":
                link = "https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-brf"
                print("Abrindo site")
                time.sleep(2)
                Abrir_Site(link)
            case "4":
                return
            case _:
                print("Opção invalida")        

#menu para controle e orientação
def Menu_Controle():
    print("\nMenu:")
    print("Digite 1 para acessar o tutorial para dúvidas, se de erro: ")
    print("Digite 2 para atualizar chave, se de erro: ")
    print("Digite sair para finalizar a conversa com a IA: \n")

#main principal
def main():
    #variaveis
    Arquivo = "Chave.txt"
    pergunta = " "
        
    while pergunta != "sair":
        #obter chave
        chave = SalvarChave(Arquivo)
        
        # Se o arquivo estiver vazio
        if not chave:
            #tutorial de cadastrar chave
            Tutorial()
            chave = SalvarChave(Arquivo)
        
        #menu de controle
        Menu_Controle()
        
        #desenho
        print("♙ ♚ ♕")
        print("Bem vindo ao chess.AI:")
        
        #pergunta de controle e pergunta da IA
        menu = input("\nDigite o que você deseja: ")
        
        #fluxo de controle
        match menu:
            case "1":
                Tutorial()
            case "2":
                chave = input("Digite a sua chave de ativação da IA, para atualizar: ")
                with open(Arquivo, "w") as arquivo:
                    arquivo.write(chave)
                print("Chave atualizada com sucesso")
            case "3":
                return
        
        #recebe a pergunta do menu
        pergunta = menu
        
        #chamar genimi e responde
        resposta = Perguntar_Gemini(pergunta,chave)
        os.system("cls") #limpar cmd
        print(resposta)
        
#chamar o main
if __name__ == "__main__":
    main()